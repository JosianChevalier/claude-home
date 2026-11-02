---
ongoing_work_file: "OpenCode's new sessions inherit HARNESS_TMPDIR=/tmp/opencode and real tool calls verify state continuity; empty when launch configuration and restart verification are done."
rank: 0
---

# Shared temporary storage and container setup

## Scope

Implement `HARNESS_TMPDIR` support in `tools/grab-notebook` and `philosophy/navigation/explore.py`. Each harness supplies its own directory through its inherited launch environment; shared scripts do not encode the harness name.

For OpenCode in this container, use `HARNESS_TMPDIR=/tmp/opencode`. The local `opencode.json` already allows `/tmp/opencode` and `/tmp/opencode/**`; no wider temporary-directory allowance is needed. Set the variable at container/session launch, or before launching OpenCode in a terminal. An export cannot change the environment of an already running OpenCode process.

Claude's launcher adaptation is separate work in `claude-temp-storage.work.md`. Leave that setup to Claude; coordinate the rollout so changing shared scripts does not silently break callers that have not set the variable yet. Agent prompts and conversational rules are outside this task.

## Remaining work

- [ ] Set `HARNESS_TMPDIR=/tmp/opencode` in the external OpenCode container/session launcher, or `export HARNESS_TMPDIR=/tmp/opencode` in the terminal **before** starting OpenCode. No container launcher lives in this checkout; the current process cannot inherit a newly exported variable. Restart into a fresh session after configuring the launcher, rather than switching the root of an active session. ← next
- [ ] In that fresh session, call `grab-notebook` twice through the real tool and run `philosophy/navigation/navigation.sh explore start`, followed by a returned link through the real subprocess path. Check that both state files are under `/tmp/opencode` and persist across calls. Then remove this work file.

## Script contract

Both scripts use `HARNESS_TMPDIR` when nonempty and retain the original `/tmp` paths when unset, so active Claude and OpenCode sessions without the new launch setting still find their state. A configured root must be absolute, have existing non-symlink parents, and be a directory owned by the invoking OS user; its mode is set to `0700` on each use. Existing symlinks or unowned state files are rejected. New files are mode `0600`. The scripts do not migrate existing state: change the environment only at a fresh-session boundary, or preserve the old session without changing its variable.

Local checks: `python3 -B -m unittest discover -s tools/tests -p test_harness_temp_storage.py -v` passes for both roots, reuse, exploration read/write, legacy fallback, unsafe directories and symlinked files. `/tmp/opencode` is owned by `node` (uid 1000), now mode `0700`; `/tmp` is on container overlay storage, while `/workspace` is on a separate host mount. Container lifetime and the actual external launcher remain to be verified outside the repo.

## Boundaries

Container-local `/tmp` is normally isolated from the host unless mounted, but its contents are disposable. Directory permissions isolate other ordinary users, not processes running under the same account or privileged administrators. OpenCode external-directory permissions govern tool approval, not shell filesystem isolation.

The tree already contains uncommitted agent-configuration and AGENTS.md changes. Preserve them and keep this implementation scoped. The local `opencode.json` is git-ignored; the template is tracked. Other agent work remains in `opencode-agents.work.md`.
