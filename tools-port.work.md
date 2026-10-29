---
ongoing_work_file: "OpenCode can use the harness editing and session-notebook tools without Claude-specific paths or assumptions"
rank: 1
---

# OpenCode tool portability


## Current step

Give OpenCode a session notebook. `grab-notebook` needs `CLAUDE_CODE_SESSION_ID`; OpenCode has a real `sessionID` in its custom tools (`tool/*.ts`) and plugins. Decide the shape, then document it in `tools/docs/opencode.md`.

- Claude side: a SessionStart hook receives the session id on stdin, so the notebook path could be put in context without the env variable; only if the two sides end up sharing a shape.
- The cloud adapter `.claude/` has no `settings.json`, so the hook does not run there: cloud-skills.work.md territory.


Keep Claude's existing scripts working. Do not include `wake-and-run`, status widgets, or compaction policy in this work.
