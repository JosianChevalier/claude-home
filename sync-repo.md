# Harness repo and multi-machine sync — design state
 
Status on 2026-10-08: prototype `.claude/` landed in `~/.claude/old-claude/` (step 2 done). Resume from "Migration process", step 3, following the MO below. OpenCode is out of scope for now: Claude Code only.
 
## Goal
 
Move the canonical harness core (this project's rationales, rules, skills, agents) into one git repository that Josian can read and edit from three places:
 
- personal laptop, Claude Code
- client laptops, on stable projects
- the web (claude.ai/code), including live tweaks during coaching
The same core must serve both Claude Code and OpenCode.
 
## Decided
 
- **The repo is `JosianChevalier/claude-home`.** Exists since 2026-06, private for now; it already is `~/.claude` with an allowlist `.gitignore`. Rename to `harness` (or similar) later. Made public only once merged and clean.
- **OpenCode v2 is the target, v1 must keep working.** Design for v2's loading paths; keep the v1 fallbacks (`CLAUDE.md` read, `OPENCODE_CONFIG_DIR`) intact rather than relying on them.
- **Plain git, three writers.** Pull with rebase at session start, small commits.
- **No plugin marketplace.** Others take inspiration; they do not install. A plugin install is also a cached copy, awkward to edit and push back.
- **No Packmind.** It is one-way (server to repos), covers only standards, commands and skills, and needs a self-hosted server.
- **Agnostic core, thin per-tool adapters.** No abstraction or generator layer for two consumers.
- **`CLAUDE.md` is the single rules file; `AGENTS.md` is a symlink to it.** (Reversed on 2026-10-08 from the earlier `@AGENTS.md` import.)
- **Folder `philosophy/`** replaces `rationale/`. Aligns with agent-tutor; the content is doctrine and framing more than ADR-style argumentation.
- **Rationale refs are wikilinks.** Form: `Rationale: [[philosophy/context-economics]]`, several comma-separated on one line. No `@` (Claude Code imports `@path` eagerly and recursively, which would pull layer 2 into every session). The `[[` is a collision-proof anchor for a future plugin; `Rationale:` keeps the attractor word and distinguishes these from other wikilinks. No `.md`. Resolution order (repo-local `philosophy/`, then global `~/.claude/philosophy/`) lives in AGENTS.md and the plugin, not in the notation. Regex: `^Rationale: (\[\[philosophy/[\w-]+\]\](, )?)+$`.
- **Merge direction: everything from this project into `~/.claude`.** The laptop's `~/.claude` is minimal (quota tooling, statusline, two skills) and its `CLAUDE.md` is already fully covered by the prototype's `AGENTS.md` and skills. Nothing to preserve from the laptop side.
- **Scope: `.claude/` only.** Everything else in the project (`agent-tutor/`, `artifact-review/`, `opencode-preload/`, `opencode-sandbox/`, `kaizen/`, `reference/`, `linkedin-post-ideas.md`) is temporary or work-in-progress, not Josian's harness.
- **Client-content guard.** Pre-commit checks on each laptop; whether pushing from a client laptop is allowed is judged per client.
## Proposed, not confirmed
 
- **Agents as thin wrappers.** Agent substance lives in a skill (shared by both tools). Each tool gets its own small agent file holding only frontmatter plus "load skill X": `~/.claude/agents/x.md` and `~/.claude/opencode/agents/x.md`.
- **Session-start pull hook** in each laptop's Claude Code `settings.json`: `git -C ~/.claude pull --rebase --autostash --quiet || true`.
- **After the move**, this project syncs from the new repo and the uploaded docs are deleted, so there is one canonical copy. `claude-home` is already attached as a second sync source.
## Migration process
 
1. Take the decisions here, in conversation. Done.
2. Zip the project's `.claude/` onto the personal laptop. The project is the canonical copy (docs were edited here only). No bulk export: one `project_read` per doc, ~100 docs; done by several sub-agents writing verbatim to disk, then zipped.
3. Integrate bit by bit into `~/.claude` following the MO below.
4. Scan for client specifics, then rename and make public.
5. Switch this project to sync from the repo only; delete the uploaded docs.
## MO for step 3 (2026-10-08)

**Backlog is the folder.** `old-claude/` is the backlog; a file leaves it when it enters the repo. Nothing enters the repo uncleaned. All ~100 files get inspected, none is skipped.

**Per file:** inspect against the harness-design rationales, then normalize: `rationale/` → `philosophy/`, `@rationale/...` refs → `Rationale: [[philosophy/...]]`, content restructured to the three-layer target. `.gitignore` is extended as each new folder lands (`AGENTS.md`, `agents/`, `rules/`, `philosophy/`, `templates/`).

**Target: three-layer harness.**

- `philosophy/` — the substrate: why we do things the way we do.
- `agents/`, `skills/`, `rules/`, etc. — the general-case design. Each file has two sections:
  - `## Doctrine` — the main attractors: heuristics, maxims, the idea we follow.
  - `## Procedure` — not fixed. Only when the thing relies on a procedure. Instructions here stay mechanical. Some skills bring knowledge (domain or other) instead.
- Doctrine is the idea; procedure is what works in 80% of cases. The limit of applicability must be understandable from the file. Doctrine is the fallback that guides the agent when the mechanical approach does not fit. This principle must be written down somewhere in the repo (philosophy).

**Order:**

1. Replace the content of `CLAUDE.md`. Done 2026-10-08; OpenCode section parked in `old-claude/AGENTS.md`.
2. Philosophy files.
3. Rules, one by one. Many are old: some already reimplemented in skills, others to move in a different form. Keep the rationale that explains *how to say* things.
4. Skills.
5. Agents.
6. Templates: things to version and share, but never loaded into context.

**Placement decisions (2026-10-08):**

- `composable-rules/` → `templates/rules/`. Opt-in rules a project loads for one bounded context via `@~/.claude/templates/rules/x.md`, never globally. Keep the set together: they cross-reference each other and `always-valid-domain.md`.
- Templates carry frontmatter (`name`, `description`, `applies-to`) as the source of truth; `templates/README.md` is generated from it by `scripts/index-templates.py`, so the index cannot drift.
- Scripts: by default packaged with the skill or agent that uses them. Reusable ones go in a shared `tools/` folder.
- `hooks/` and `settings.json`: case by case.

## What each tool reads (checked against docs, 2026-10-06)
 
| Part | Claude Code | OpenCode v1 | OpenCode v2 |
|---|---|---|---|
| Global rules | `~/.claude/CLAUDE.md` | `~/.config/opencode/AGENTS.md`, falls back to `~/.claude/CLAUDE.md` | `~/.config/opencode/AGENTS.md` only, no `CLAUDE.md` fallback |
| Skills | `~/.claude/skills` | also scans `~/.claude/skills` | also scans `~/.claude/skills` |
| Agents | `~/.claude/agents`, `name` field | own `agents/` folder only, name from file name, `permission` | same, field renamed `permissions` |
| Extra instruction files | `~/.claude/rules` | `instructions` in config | `instructions` accepted but not loaded |
| Custom config dir | n/a | `OPENCODE_CONFIG_DIR` | not documented |
 
Consequence for OpenCode v2 with `~/.claude` as the repo: two symlinks.
 
```bash
ln -s ~/.claude/AGENTS.md        ~/.config/opencode/AGENTS.md
ln -s ~/.claude/opencode/agents  ~/.config/opencode/agents
```
 
On v1, zero symlinks: the `CLAUDE.md` fallback plus `export OPENCODE_CONFIG_DIR=~/.claude/opencode`.
 
## Hazards
 
- **Public history is permanent.** Scan the dirty prototype for client specifics before flipping to public; the existing `claude-home` history counts too.
- **The client-terms denylist must stay untracked**, or the public repo publishes the client names.
- **`rules/` has no loading path in OpenCode v2.** That content must move into `AGENTS.md` or become skills.
- **"OpenCode harness levels" section of `AGENTS.md` is tool-specific.** Through the `@AGENTS.md` import, Claude Code reads it too. It belongs in the OpenCode adapter.
- **OpenCode sandbox.** The global level is `/mnt/opencode-host` inside a container; a symlink pointing outside the mount is dead there. Mount the checkout directly.
- **Stale contract text.** `two-layer-harness.md` and the `harness-improvement` skill still describe the old `Rationale: @rationale/...` form.
- **Wikilink navigation is workspace-bound.** Editors resolve `[[philosophy/x]]` only inside the open workspace; a ref to a global file does not jump from a client repo unless `~/.claude` is in the workspace. Plugin resolution is unaffected.
- **The prototype's `.claude/CLAUDE.md` carries an emoji-header rule** already dropped on the laptop. It dies in the merge.
## Unverified
 
- Whether OpenCode follows the `@AGENTS.md` import (only matters on v1, where it reads `CLAUDE.md`).
- Whether `OPENCODE_CONFIG_DIR` still works in v2.
- Whether one agent file with only `name` and `description` can serve both tools.
- Whether a web session working on another project can load the harness (a cloud session sees only its own repo, not `~/.claude`). Editing the harness from the web works by opening a session on the harness repo itself.
## Settled questions (2026-10-08)
 
1. OpenCode version — v2, retrocompatible with v1; see Decided.
2. Merge vs replace — merge everything from the project into `~/.claude`; see Decided.
3. `philosophy/` — yes; see Decided.
4. Repo — `claude-home`, to be renamed; see Decided.
5. Scope — `.claude/` only; see Decided.

