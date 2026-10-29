---
ongoing_work_file: "Make the repo's skills, agents, commands, rules and tools load in cloud sessions. Empty when a fresh cloud session lists ongoing-work among its skills and names grab-notebook and replace-text without being told."
rank: 3
---

# Cloud sessions run without the repo's harness

A cloud session clones this repo as a project (`/home/user/claude-home`); Claude Code then discovers config only under `.claude/`. The adapter `.claude/` holds symlinks to `agents/`, `commands/`, `rules/`, `skills/` (its README says why) and `CLAUDE.md`, which tells the agent to read any `~/.claude` path as the repo root. Locally the repo is `~/.claude` itself, so the adapter is live there too: a file in it runs in both places.

## Steps

- [ ] Tools list in the cloud. Locally `~/.claude/settings.json` has a SessionStart hook printing `tools/docs/claude.md`; no home config exists in the cloud. Add `.claude/settings.json` (already whitelisted in `.gitignore`) with a SessionStart hook running one script under `tools/` that exits silently unless `CLAUDE_CODE_REMOTE` is `true`, and prints the list otherwise. `CLAUDE_CODE_REMOTE` is documented as set to `true` in cloud sessions and unset locally (code.claude.com/docs/en/env-vars, and the hooks page); `CLAUDE_CODE_REMOTE_SESSION_ID` carries the cloud session id. Neither has been seen in a real cloud session yet. **← current**
- [ ] Fresh cloud session: `ongoing-work` in its skill list, both tools named when asked without running anything.
- [ ] Description of `ongoing-work`: match the words sessions use ("Resume from X.work.md", "record it in the work file"), which it does not today.
