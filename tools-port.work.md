---
ongoing_work_file: "OpenCode can use the harness editing and session-notebook tools without Claude-specific paths or assumptions"
rank: 1
---

# OpenCode tool portability

## Current step

Decide the smallest platform split, then implement it:

- `rules/tools.md` hardcodes `~/.claude/tools/replace-text`; OpenCode already has native `apply_patch`, so decide whether OpenCode should omit this rule or the shared rule should prefer the native editing tool.
- `rules/session-design.md` hardcodes `~/.claude/tools/grab-notebook`, whose script requires `CLAUDE_CODE_SESSION_ID`; design an OpenCode notebook tool or plugin around OpenCode's real `sessionID`.

Keep Claude's existing scripts working. Do not include `wake-and-run`, status widgets, or compaction policy in this work.
