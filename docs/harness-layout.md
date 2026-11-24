# Harness layout

```text
Harness repository
|-- Shared      rules/*.md, skills/, agents/, commands/, tools/run
|-- Claude      CLAUDE.md, rules/claude/, settings.template.json
|-- OpenCode    AGENTS.md, opencode-rules/, plugins/, opencode.template.json
|-- Project     .claude/ and .opencode/ adapters -> canonical root files
`-- On demand   philosophy/ (rationale), docs/ (guides)
```

Install this repository at `~/.claude` for Claude Code or `~/.config/opencode` for OpenCode. These are alternative home installations, not evidence that both clients are active. Paths below are relative to the repository root.

## Rule ownership and loading

- **Shared:** edit `rules/*.md`. Claude loads rules recursively, including `rules/claude/`; OpenCode's explicit `rules/*.md` glob is nonrecursive.
- **Claude only:** edit `rules/claude/*.md`. OpenCode's configured rule globs exclude this subtree.
- **OpenCode only:** edit `opencode-rules/*.md`, outside Claude's rule tree.
- **Client guidance:** root `CLAUDE.md` and `AGENTS.md` are distinct, not interchangeable.

The home OpenCode `opencode.json` and its tracked template explicitly load `~/.config/opencode/rules/*.md`, `~/.config/opencode/opencode-rules/*.md`, and `~/.config/opencode/tools/docs/opencode.md`. The project adapter `.opencode/opencode.json` loads the same repository-relative paths plus `.opencode/AGENTS.md`.

## Project adapters

`.claude/rules -> ../rules` exposes shared and nested Claude rules. Both adapters link `skills/`, `agents/`, and `commands/` to the canonical root directories; `.opencode/` also links `plugins/`. Edit the canonical files, not copies.

`.opencode/AGENTS.md -> ../.claude/CLAUDE.md` supplies project-only harness-maintenance instructions, distinct from root client guidance. The adapters apply when this repository is the project, not when it supplies home configuration for work elsewhere. Details: [Claude adapter](../.claude/README.md), [OpenCode adapter](../.opencode/README.md).

## Configuration and tools

`settings.template.json` and `opencode.template.json` are tracked starting points for local `settings.json` and `opencode.json`; the latter is untracked here. Edit templates for distributable defaults, local files for installation-specific configuration.

`tools/run` is the shared dispatcher. OpenCode calls it through `tools/run.ts` and explicitly loads `tools/docs/opencode.md`; the Claude template's SessionStart hook invokes `~/.claude/tools/run doc claude`. See [tool loading](../tools/README.md).

`philosophy/` holds on-demand rationale, not automatically loaded instructions. This guide describes the configured layout, not a runtime loading test.
