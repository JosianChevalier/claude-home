---
ongoing_work_file: "Make the repo's skills, agents, commands and rules load in cloud sessions. Empty when a fresh cloud session lists ongoing-work among its skills."
rank: 3
---

# Cloud sessions run without the repo's skills

Started as a kaizen: `ongoing-work` did not load when a work file was resumed or edited, so its rules were broken (commit 393e2a9, undone in 5f8d17c).

## Root cause

- Locally, this repo is cloned *as* `~/.claude`, so `skills/`, `agents/`, `commands/`, `rules/` are found as personal config.
- A cloud session clones it to `/home/user/claude-home`. Claude Code only discovers project config under `.claude/`, and the repo has none. Only the root `CLAUDE.md` loads; everything it points to loads only if opened by hand.
- Second, smaller cause: the `ongoing-work` description ("Tracking ongoing work…") does not match the words a session uses ("Resume from X.work.md", "record it in the work file").

## Tested (headless `claude -p`, copy of the repo, 2026-10-16)

| Setup | Repo skills listed | Rules loaded |
|---|---|---|
| no `.claude/` | none | none |
| `.claude/skills -> ../skills`, `.claude/rules -> ../rules` | all five | all three |

Symlinks work. Not tested: `agents`, `commands`.

## Proposed fix

```
.claude/
├── skills   -> ../skills
├── agents   -> ../agents
├── commands -> ../commands
└── rules    -> ../rules     # only if rules should always load
```

Not the whole root as `.claude -> .`: it loops, and `CLAUDE.md` would likely load twice.

## Open

- `rules/`: linked, every rule loads in every cloud session. Is that the intent, or do rules stay loaded on pointer?
- Local clone as `~/.claude`: does the nested `~/.claude/.claude/` load anything twice when working with cwd in the repo? Unverified.
- The description gap, after the fix.

## Steps

- [ ] Decide on `rules/`. **← current**
- [ ] Add the links, commit on the working branch.
- [ ] Fresh cloud session: check `ongoing-work` is in its skill list.
- [ ] Description of `ongoing-work`: match the words sessions use.
