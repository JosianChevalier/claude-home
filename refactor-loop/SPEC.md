# refactor-loop — spec

A script that runs the atomic-refactoring cycle headless, on a target git repo, until the code converges.

```
            ┌────────────────────────── loop ───────────────────────────┐
            │                                                           │
 start ──▶ refactorer ──▶ script checks diff ──▶ committer ──▶ script checks commit
            (claude -p)    empty? too big?        (claude -p)   one commit? clean?
            │                     │                                     │
            │                     └── reject: reset tree, stall +1      │
            │                                                           │
            └──── every N commits: watchdog (claude -p, no tools) ◀─────┘
                                   VERDICT: continue | stop
```

Source skill: `old-claude/skills/atomic-refactoring/SKILL.md`; agents `old-claude/agents/refactorer.md`, `committer.md`; wrapper `old-claude/scripts/commit.sh`.

## Division of labour

The script owns every state transition and every countable fact. Agents only say things. (patterns: scripts-own-state, recomputed-progress)

| Who        | Does                                                      | Never                          |
|------------|-----------------------------------------------------------|--------------------------------|
| script     | preconditions, lock, diff checks, reset, commit checks, stop | edit code, write commit prose |
| refactorer | ONE tiny behaviour-preserving change, then a report       | git mutation, a second change  |
| committer  | stage by name, name the commit, call `commit.sh`          | edit files, `git commit`, amend, `--no-verify`, push |
| `commit.sh`| the only path to `git commit`; validates the message      | rebase, push                   |
| watchdog   | reads the run's history, judges drift                     | tools of any kind              |

## Usage

```
loop.py <repo> [--goal TEXT] [--paths P ...] [--test-cmd CMD]
               [--max-iterations 30] [--max-stall 3] [--max-lines 80] [--max-files 6]
               [--audit-every 5] [--worker-timeout 600] [--idle-timeout 300]
               [--model-refactorer claude-opus-5-5] [--model-committer claude-haiku-5-5]
               [--model-watchdog claude-sonnet-5-5]
               [--claude-bin claude] [--run-dir DIR]
```

- `--goal` given → directed mode; absent → cleanup mode.
- `--paths` scopes the refactorer's attention; absent → the whole repo.
- `--test-cmd` is added to the refactorer's allowlist as `Bash(<CMD>*)`.
- Python 3 stdlib only. One file.

## Preconditions — exit 2

- `<repo>` is a git work tree (`.git` tested with `.exists()`, so worktrees pass).
- `git status --porcelain` is empty.
- `ANTHROPIC_API_KEY` is unset (else every worker silently bills the API). (slots-vs-budget)
- Lock: `fcntl.flock` non-blocking on `$TMPDIR/refactor-loop/locks/<sha1(repo root)>.lock`. Busy → exit 2.
- `--claude-bin` is found on PATH or as a path.

⚠️ Run it on a dedicated branch: a rejected change is reset with `git reset --hard <recorded sha> && git clean -fd`. Safe because the tree was clean at start; ignored files are untouched.

## Worker invocation

Every worker, whatever the role:

```
<claude-bin> -p <prompt> --model <M> --output-format stream-json --verbose
             --no-session-persistence <role flags>
```

- `Popen(cwd=repo, stdout=<log file>, stderr=STDOUT, start_new_session=True)`. Never PIPE.
- env: the parent's, minus `CLAUDE_CODE_SESSION_ID`, plus `REFACTOR_LOOP_ROLE=<role>`.
- Log: `<run-dir>/<iter:03>-<role>.jsonl`.
- Result: the last stream-json event with `"type": "result"`; its `result` field is the agent's final text. No result event → worker failed.
- Prompt = `prompts/common.md` + `prompts/<role>.md` + a context block built by the script. No prompt prose in Python. (prompts-as-files)

Role flags:

| role       | `--allowedTools` (one space-separated string)                                                                                  | `--disallowedTools`                                                                                       |
|------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| refactorer | `Read Edit Write Glob Grep Bash(git status*) Bash(git diff*) Bash(git log*) Bash(git show*) Bash(ls *) Bash(head *) Bash(tail *) Bash(wc *)` + test cmd | `Bash(git add*) Bash(git commit*) Bash(git -C * commit*) Bash(git reset*) Bash(git checkout*) Bash(git restore*) Bash(git stash*) Bash(git clean*) Bash(git push*)` |
| committer  | `Bash(git status*) Bash(git diff*) Bash(git log*) Bash(git add *) Bash(<abs path of commit.sh> *)`                             | `Edit Write Bash(git commit*) Bash(git -C * commit*) Bash(git push*) Bash(git reset*)`                    |
| watchdog   | none; `--tools ""` instead                                                                                                     | —                                                                                                         |

The deny list is not redundant: workers inherit the user's `settings.json` allow rules.

## commit.sh

The one place that knows how a commit is made. Ported from `old-claude/scripts/commit.sh`.

- Usage: `commit.sh "<subject>\n\n<body>"`; `\n` is expanded.
- Refuses `--no-verify`, a subject over 72 chars, a non-blank line 2, a footer not preceded by a blank line.
- Runs `git commit`; hooks run, they are the safety net.
- The old rebase-on-main step is dropped: it would rewrite the history the loop checks.
- The script passes its absolute path to the committer in the context block (`COMMIT SCRIPT:`).

## Per-worker watchdog (layered-watchdog)

Poll every second:

1. Process ended → collect the result.
2. Elapsed > `--worker-timeout` → kill.
3. `now − log mtime` > `--idle-timeout` → kill. A long silent test run freezes the log; set the idle timeout above the test suite's duration.

Kill = `os.killpg(os.getpgid(pid), SIGKILL)`, fallback `proc.kill()`, then `wait()`. A killed worker counts as failed.

## One iteration

1. Assert the tree is clean and `HEAD == last recorded sha`. Else stop `state-drift`.
2. Run the refactorer. Context block: mode, goal, paths, test cmd, `BUDGET: <max-lines> lines, <max-files> files`, last 10 commit subjects since baseline, the previous iteration's rejection reason or NEXT.
3. Parse its report from the result text, the last match of each:
   ```
   CHANGED: <one line>
   STATUS: MORE_TO_DO | NOTHING_TO_REFACTOR
   NEXT: <one line | n/a>
   ```
4. Recompute the change from git, never from the report:
   - tracked: `git diff --numstat HEAD`; untracked: `git ls-files --others --exclude-standard`, their lines counted.
   - empty diff + `NOTHING_TO_REFACTOR` → stop `converged`.
   - empty diff otherwise, or worker failed → reset, stall +1.
   - lines > `--max-lines` or files > `--max-files` → reset, stall +1, reason fed to the next refactorer.
   - The report's STATUS counts only when the diff is empty.
   - `--test-cmd` given → the script runs it (`shell=True`, cwd repo, same watchdog caps, output to `<iter:03>-tests.log`). Nonzero → reset, stall +1, reason fed to the next refactorer. The refactorer's own test run is a courtesy; this one decides.
5. Run the committer. Context block: the goal, the refactorer's CHANGED and NEXT, the script's diffstat, `COMMIT SCRIPT:` path.
6. Check the commit: `git rev-list --count prev..HEAD == 1`, `HEAD^ == prev`, tree clean. Any failure → stop `commit-check-failed`, tree left as is for the human (a pre-commit hook may have failed).
7. Record HEAD. stall = 0.
8. Oscillation: `HEAD^{tree}` already seen in this run (baseline tree included) → stop `oscillation`.
9. Every `--audit-every` commits → run the loop watchdog.

## Loop watchdog

A cheap model, no tools, everything inline in its prompt: goal, `git log --format=%s baseline..HEAD`, `git diff --stat baseline..HEAD`, plus script-computed facts (commits, stall count, total lines changed).

- Last line `VERDICT: continue|stop — <reason>`. The last match wins.
- `stop` → stop `watchdog-stop`, reason printed.
- Any error (no result, unparseable, killed at 120 s) → continue.

## Stop reasons

| reason              | exit |
|---------------------|------|
| converged           | 0    |
| max-iterations      | 1    |
| stalled             | 1    |
| oscillation         | 1    |
| watchdog-stop       | 1    |
| commit-check-failed | 1    |
| state-drift         | 1    |
| precondition        | 2    |

## Output

- stdout: one line per event, flushed: `[iter 3] refactorer: +4/-2 in 1 file — Extract removeInactive`.
- Same lines appended to `<run-dir>/run.log`.
- Last line, always: `LOOP END: <reason> (<n> commits, <baseline-short>..<head-short>)`.
- Default run dir: `$TMPDIR/refactor-loop/runs/<YYYYmmdd-HHMMSS>/`.

## Tests (blackbox-test-discipline)

- Black box: run `loop.py` as a subprocess against a `git init` tmp repo; assert on exit code, `LOOP END` line and `git log` subjects only.
- `--claude-bin tests/fake_claude.py`: a fake that writes stream-json, branches on `REFACTOR_LOOP_ROLE` and `FAKE_SCENARIO`, keeps its counters under `FAKE_STATE`.
- Every fake sleep is bounded, well above the timeout under test. Every `communicate()` has a timeout.
- Fixture: `commit.gpgsign false`, user name/email set.
