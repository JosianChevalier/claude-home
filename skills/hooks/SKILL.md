---
name: hooks
description: A hook to write, change or wire in this harness: a command a settings.json hook runs, on SessionStart or any other event.
---

# Hooks

## Doctrine

- Where a script lives says who calls it: `hooks/` holds what the harness runs on its events, `tools/` what agents call.
- A hook is a named script, never logic in the JSON.

## Know-how

This skill only says where a hook's script lives and how it is documented. `update-config` still writes the hook entry in `settings.json`, and `plugin-authoring` still covers hooks shipped in a plugin; load them for that part.

- The command is one path: `~/.claude/hooks/<name>` from a home settings file, `"$CLAUDE_PROJECT_DIR"/hooks/<name>` from the project's `.claude/settings.json`. A hook that only calls an agent tool calls it through `run`, as `run doc claude` does, and needs no script.
- The script is named for what it does and carries a comment header under its shebang: the event and settings file that run it, then what it is for. It has no `# platforms:` line; that line lists a tool for agents.
- The script reaches the tools through `../tools/`.
- A SessionStart hook's stdout enters the context: a hook with nothing to tell the agent sends its output to `/dev/null`.
- `hooks/CLAUDE.md` gets the script's line in the same commit, and loses it when the script goes.
- The local `settings.json` is not versioned: a hook meant for every machine goes in `settings.template.json` too.

Rationale: φharness-elements
