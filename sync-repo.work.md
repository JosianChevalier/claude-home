---
ongoing_work_file: "Migrate the prototype .claude/ into this repo. Empty when old-claude/ is empty, the repo is scanned, renamed and public, and the project syncs from it."
rank: 1
---

# Harness repo and multi-machine sync

Work file of the migration. OpenCode is out of scope for now: Claude Code only. Current step is marked in Steps.

## Steps

- [x] Migration 1: decisions, in conversation.
- [x] Migration 2: prototype `.claude/` zipped onto the laptop, in `old-claude/`.
- [ ] Migration 3: integrate bit by bit, MO below. **← current**
  - [x] 3.1 `CLAUDE.md` replaced; OpenCode section parked in `old-claude/AGENTS.md`.
  - [ ] 3.2 Philosophy. **← current**
    - [ ] `context-economics`: cut the OpenCode section ("Rule → context (AOP)", `globs:`/opencode-rules in loading policy), or defer to 3.3. Decide first.
    - [x] `session-state-in-documents` landed 2026-10-10, to review.
    - [ ] Backlog `old-claude/rationale/`, 15 files, each with an old counterpart to import. Four already have wikilinks pointing at them from `philosophy/`: `compounding-decisions`, `model-expressions`, `shape-and-substance`, `workflow-rhythm`.
      - [x] `shape-and-substance` landed 2026-10-11: the belt test projected onto documents.
      - [ ] `model-expressions` moved 2026-10-11, iterating. Done: the appendix cut to the spork, tension pointed at `model-phenomenology` (first use, in the caveat). The example kept whole (the loss per medium needs showing). The caveat says compensation locally, a trade-off; the general line is in the root-cause item below. The spork (from the session "philosophy files in context" of 2026-10-10) moved out 2026-10-11 to `model-phenomenology`, section "Rivalry and the spork": rivalry named there (the type projects more than one fitting concept; goes up to the holder of the horizon), silent choice and the spork as the two ways of settling below; the misfit sentence and the detector dropped, both expressions' vocabulary. Shape pass done 2026-10-11.
      - DDD cluster, `ddd` tag on each: `model-phenomenology` (what a model is), `model-expressions` (where it exists), `aggregates` (its consistency boundary); `rules/design-first` hangs off them in 3.3. A later file on what a model is, if any, points at `model-phenomenology`.
      - [x] `aggregates` landed 2026-10-12: the enforcement ladder (structure / ordered saves / shared unit of work) removed as a persistence concern dressed as design; the aggregate holds its invariants itself, by structure or at minimum by its code, and is saved whole in one call, atomicity being the repository's modality. Observer is any domain code holding the aggregate, so invariants hold after each operation, in memory. Example's SQL cross-row case replaced by a status-dependent field (nullable + check as symptom, sum type as the form, Wlaschin named). Plan-stage graft on continuous delivery dropped.
      - [x] `workflow-rhythm` landed 2026-10-12: the probe sentence (reshaping is the cheapest probe, surfaces model tension early) owned here; `planning-is-everything` holds a copy, to shrink to a pointer at its turn. Three scales kept as written, not an abstraction-ladder sighting (no absorption between scales).
      - [x] `compounding-decisions` landed 2026-10-12: a check shortens the chain to what it misses, it does not reset it; validators multiply their miss rates only when independent, same-family validators share biases. Raising `p` added as the other lever: kaizen's work, and how a decision earns its removal (path to commodity).
      - [ ] Then the rest of the backlog, fewest outgoing links first: `rationale_guest-codebase` (0 out) **← next**, `study-making` (1), `small-batches` (1 out, 5 in), `mechanical-refactoring` (2), `change-in-place`, `continuous-delivery` (3), `prototypes-are-probes`, `planning-is-everything` (4), `mikado`, `walkthrough-narrative` (5).
    - [ ] `zoom-levels`: a section on form, the second lever beside scale: each piece of information in the medium that carries it cheapest (the doctrine line landed in `rules/writing.md` 2026-10-11, pointer already there). Reshape in the same pass: title still says "Rationale:".
    - [ ] To confirm: the Lakatos line in `three-layer-harness`.
    - [x] Reading session on Ashby, Beer, Snowden: answered 2026-10-11, landed in `metis-kairos` (recursion restated as subsidiarity; Snowden a neighbour, not a restatement).
    - [ ] Edge of chaos: dropped from `three-layer-harness` layer 1, returns elsewhere, differently.
    - [ ] `attractors`, definition: an attractor is a term in the weights, shared knowledge, pulling the same for every reader. What is written in a file or said earlier in a session is not one: it pulls the agent that read it and nobody else, and the file names that as the hazard. One paragraph, under Load the expertise; decided 2026-10-11, text not yet agreed.
    - [ ] Root cause versus compensation needs a philosophy file: CLAUDE.md asks "root cause, or compensation?" and `attractors` (Reorient before compensating) states it, neither has a home to point at. Compensation is legitimate when the root cause is out of reach, no ownership (a grammar, a neighbouring system) or not yet treated: local, a trade-off said as such, never spreading; medication for the symptom. First said locally in `model-expressions`' caveat.
  - [ ] 3.3 Rules, one by one. Many are old: some already live in skills, others change form. Keep the rationale on *how to say* things.
    - [x] `rules/conversation` landed 2026-10-10, first rule of the new repo; `.gitignore` whitelists `rules/`.
    - [x] Home for the session-anchoring know-how (philosophy in `session-state-in-documents`): the `ongoing-work` skill, Doctrine section.
  - [ ] 3.4 Skills.
    - [ ] `aggregate-identification` and `invariant-enforcement`: the ladder they rest on was removed from `philosophy/aggregates` 2026-10-12. The first keeps its derivation steps, loses the hand-off "each safety property climbs the enforcement ladder"; the second (structure vs ordering vs transaction for an aggregate invariant) has no premise left, likely deleted.
    - [ ] Model tensions as a kairos gate (the gate after a model change in `kairos-gates`), once `model-phenomenology` holds rivalry: done 2026-10-11.
    - [ ] `harness-improvement`: re-enter the ref-form contract and "load the rationale before diagnosing"; it still reads `two-layer-harness`/`harness-target` (lines 14-15, 80).
    - [ ] `wake-and-run`: `## Procedure` header, no Doctrine. Rewrite to the current shape.
  - [ ] 3.5 Agents.
  - [ ] 3.6 Templates.
- [ ] Migration 4: scan for client specifics, rename, make public.
- [ ] Migration 5: the project syncs from the repo only; delete the uploaded docs. Then delete this file.

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
## MO for step 3 (2026-10-08)

**Inspection is a review in conversation.** Findings per file go on the table; the file is written after the decision.

**Backlog is the folder.** `old-claude/` is the backlog; a file leaves it when it enters the repo. Nothing enters the repo uncleaned. All ~100 files get inspected, none is skipped.

**Per file:** inspect against the harness-design rationales, then normalize: `rationale/` → `philosophy/`, `@rationale/...` refs → `Rationale: [[philosophy/...]]`, content restructured to the three-layer target. `.gitignore` is extended as each new folder lands (`AGENTS.md`, `agents/`, `rules/`, `philosophy/`, `templates/`).

**Target: three-layer harness.**

- `philosophy/` — the substrate: why we do things the way we do.
- `agents/`, `skills/`, `rules/`, etc. — the general-case design. Each file has two sections:
  - `## Doctrine` — the main attractors: heuristics, maxims, the idea we follow.
  - Know-how — the rest of the file, after the doctrine, sectioned when useful. Procedures, heuristics, checklists, knowledge: no fixed header, not always a procedure.
- Doctrine is what must always be true, the intent; know-how is what works in 80% of cases. The limit of applicability must be understandable from the file. Doctrine is the fallback that guides the agent when the mechanical approach does not fit. This principle must be written down somewhere in the repo (philosophy).

**Philosophy file, migration flow (2026-10-12):**

The reader came from `/clear` and has opened nothing. A message is written from what they hold: this conversation, and nothing read through a tool. A word met in a file this session does not go into a message unless the message quotes it or gives its meaning in the same sentence. Fifteen sessions failed on this point alone; the rest of the flow below exists to make it hold.

Before the first message, silent: read in full `philosophy/harness-shape`, `harness-elements`, `three-layer-harness`, `harness-direction`, `kaizen`, `attractors`; then the old file and every file pointing at it. The file must hold what the files pointing at it say it holds; a gap there is an issue like any other.

The opening turn, in this order and nothing else:

1. The file, in one line of ordinary words: what question it answers, which skills or rules lean on it.
2. How many issues, each named in plain words on one line.
3. The first issue: the old sentence quoted whole, the sentence it now contradicts quoted whole with its file named, the proposed change in edit marks.

Each following turn is one issue, in the shape of point 3. The decision just taken is restated in one line first. A rival reading goes on the table as a second reading, never written in.

Silent in the conversation, recorded in the commit message: folder, frontmatter, link form, backlog removal, mapping row.

Two commits per file. First substance: the mechanical moves and the decisions. Second shape, for the least load on the reader (rules/writing.md): title without "Rationale:", Thesis line, Related, paragraphs that breathe. The diffs separate substance from shape.

Another session may hold uncommitted edits; stage only the files you changed.

Order of the backlog: fewest outgoing links first, mutual pairs adjacent, one cluster at a time.

**Vocabulary, migration and review alike:**

- No skill named or quoted from a philosophy file; an example stays anonymous.
- A named reference (Lakatos, Boyd, Brand, Juarrero) stays one line: it is in the weights.
- Pointer targets are rationales: say rationale, not philosophy, where the pointer is meant.
- Wardley terms as attractors where the path down appears: genesis, custom-built, commodity, commodification.
- Pareto attractors where the usual-case split appears, Pareto named at the first use; never "four in five".
- A file born here has no old counterpart: say where in old-claude its material came from.
- Em-dashes stay: the old punctuation is kept. The no-em-dash rule is for artifacts sent outside (posts, PDFs), not harness files.
- A wikilink to a file still in the backlog is not a hazard.
- A section heading says what the section holds, in plain words; a label coined by the old file goes.
- In conversation, plain words: a thing is said, a term beside it at most, never instead of it.
- The well (local reading, shallow basin for the veteran) is Juarrero's landscape seen from the engineer's side; defined in model-phenomenology.

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
## Mapping old → new

Reference copy: `old-claude-reference/`. Compare with `git diff --no-index old-claude-reference/<old> <new>`. Refs normalized to wikilinks everywhere (MO); only moves, drops and pendings are noted.

| Old | New | Moved, dropped, pending |
|---|---|---|
| `rationale/transmission-belt.md` | `philosophy/transmission-belt.md` | |
| `rationale/collaborative-production.md` | `philosophy/collaborative-production.md` | |
| `rationale/zoom-levels.md` | `philosophy/zoom-levels.md` | |
| `rationale/context-economics.md` | `philosophy/context-economics.md` | OpenCode section still in, pending (3.2) |
| `rationale/harness-target.md` | `philosophy/harness-shape.md` | layer table → `three-layer-harness`; kaizen triage → `kaizen` |
| `rationale/harness-elements.md` | `philosophy/harness-elements.md` | OpenCode preload mention dropped |
| `rationale/two-layer-harness.md` | `philosophy/three-layer-harness.md` | contract and kaizen sections → `kaizen` or dropped; edge of chaos dropped, returns elsewhere (3.2) |
| `rationale/kairos-gates.md` | `philosophy/kairos-gates.md` | belt kairos and strain signal → `metis-kairos` |
| `rationale/session-state-in-documents.md` | `philosophy/session-state-in-documents.md` | `planning-is-everything` ref inlined |
| `rationale/type-and-concept.md` | `philosophy/model-phenomenology.md` | renamed 2026-10-11 (the phenomenology of the model, DDD cluster), `ddd` tag; supplies-never-adjudicates paragraph born here (promised by kairos-gates); the well defined (shallow basins, unaware transition); "coding language" → "vocabulary" |
| `rationale/model-expressions.md` | `philosophy/model-expressions.md` | moved as is 2026-10-11, iterated in conversation; spork section moved to `model-phenomenology` |
| `rationale/shape-and-substance.md` | `philosophy/shape-and-substance.md` | lifecycle → pointer to `session-state-in-documents`; shape question put under the belt test; "reviewer of guessed commitments" named silent choice |
| `rationale/aggregates.md` | `philosophy/aggregates.md` | enforcement ladder removed, compensation sentence with it; Observable saved points → Always valid (observer is domain code); example case replaced; continuous-delivery ref dropped with its sentence |
| `rationale/workflow-rhythm.md` | `philosophy/workflow-rhythm.md` | probe sentence owned here, pointers to `planning-is-everything` (why acting is the way to know) and `model-phenomenology` (model tension); three scales kept, no ladder pointer |
| `rationale/compounding-decisions.md` | `philosophy/compounding-decisions.md` | checkpoint sentence corrected (shortens, not resets; independence caveat); `p` lever added, pointers to `kaizen` and `harness-direction` |
| `rationale/attractors.md` | `philosophy/attractors.md` | widened from words to context; pink-elephant exception (observed basin, pejorative name) and Reorient before compensating added; aphorism aligned in harness-shape, kaizen |
| `skills/handover/SKILL.md` | `skills/handover/SKILL.md` | rewritten |
| — | `philosophy/kaizen.md`, `conversation-continuity.md`, `harness-direction.md`, `metis-kairos.md`, `abstraction-ladder.md`, `change-inertia.md` | new, no old counterpart |
