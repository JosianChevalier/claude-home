---
name: harness-improvement
description: Use when the user says "kaizen" or asks to improve the harness (rules, skills, AGENTS.md). NOT for feedback about the codebase itself.
---

# Harness Improvement

"Kaizen" opens a **kaizen session** — a collaborative activity, not an edit request. The discussion is where diagnoses and fixes are forged; edits crystallize the converged set, never open the session.

## Session phases

**1. Calibrate — internal work, never shown to the user.**

- Read the foundation rationales — `attractors.md`, `context-economics.md`, `two-layer-harness.md`: they govern harness improvement in general. They stay separate files because each is reused individually elsewhere, but this skill always works with all three.
- Read `harness-target.md`: the shape the harness is being rewritten toward — philosophy, doctrine, procedure. New and rewritten rules and skills take that shape; where it differs from `two-layer-harness.md`, it is the target.
- List every violation noted during the session, even minor ones — never require the user to remind you.
- For each violation: map what happened, locate the layer-1 files to change, read ONLY the rationales those files reference (`Rationale: @...`) — ignore the rest of `rationale/` — and draft a fix.
- Group the fixes by **improvement theme** (e.g. "respecting rationales", "deliverable shape", "validation discipline") — never by fix mechanism or technical cut (gates, domain, services, db).

**2. Propose — your first response.**

The deliverable is the axis proposal, exactly this shape:

```
* axis <improvement theme>:
   * add a rationale on <concept>
   * map it in skill X and Y: they currently say "<excerpt>", change to "<proposed>"
   * add a skill on <activity>
* axis <improvement theme>:
   * ...
```

- Name violations explicitly ("the placeholder-rule-for-unseen-repo violation"), NEVER by handover item number — the user does not read handovers.
- Open questions belong in this response and in the conversation as they arise, in this form: "on topic x — here is the problem, here is how it's currently done, here is my question, with suggestions."
- **Grounding**: a proposal may only cite repo facts verified in this session. A referenced artifact or fact absent from the environment → name the mismatch and ask ("the handover references this rule, it's not here — drop it?"); never emit a placeholder.

**3. Discuss — user-steered.**

- Converge diagnosis and fix direction in chat; the user chooses what to engage and when it is settled.
- If a fix contradicts a loaded rationale, either the fix is wrong or the rationale is outdated — one must change, explicitly.
- Self-sufficient conversation: bring the touched rule/skill excerpts, options, and trade-offs into chat; never make the user open a file to answer.
- Fixes remain proposals — nothing is applied during discussion.

**4. Synthesize.** Once items are converged, present the change set as a whole: items sharing a root cause merged, interactions between fixes resolved, coherence checked against the loaded rationales. Proposals cannot be taken in isolation. Your turn ends; the user validates the set.

**Validation gate**: a set with open questions cannot be presented for validation. If the user says "execute" while questions stand, reply with the list of open questions instead of applying — never answer them yourself.

**5. Apply.** Only after validation of the whole set:

- Name the write target first. Off the real harness (e.g. a doc mirror) → say so and state the porting step the user must do.
- Per touched file, a mandatory pre-edit step: list its `Rationale: @` refs → read them → then edit. (Interim discipline; a plugin will later enforce this.)
- Make the changes and commit.

## Rework > Adding

Additivity bias is the main threat. Before adding anything new: can an existing rule, skill, or AGENTS.md be updated instead? Stale or contradictory instruction → edit or remove the source. Synthesis is where this bites: several items often collapse into one stale source. Full argument: @rationale/context-economics.md

## Layer 1 Is Terse

Per token economics and Words Are Attractors (`@rationale/context-economics.md`, `@rationale/attractors.md`), compress layer-1 guidance: carry intent in the fewest precise tokens; move rationale to `rationale/`.

## Context Architecture (opencode)

| Axis | Mechanism | Location | Loaded |
|---|---|---|---|
| **Personal** (all sessions) | Global `AGENTS.md` | `/mnt/opencode-host/AGENTS.md` (`~/.config/opencode` replacement) | always |
| **Universal** (project-wide) | Frontmatter-less rules | `.opencode/rules/*.md`, no frontmatter | always (plugin injects unconditionally) |
| **Spatial** (bounded contexts) | Glob-scoped rules | `.opencode/rules/*.md` with `globs:` frontmatter | deterministically, when a touched file matches |
| **Temporal** (activities, workflows) | Skills, composed into **sub-agents** | `skills/<name>/` and `agents/<name>.md`, global (`/mnt/opencode-host/`) or project (`.opencode/`) | per workflow step, deterministically via the step's sub-agent |
| **Epistemic** (why & how) | Rationale docs | `rationale/*.md` (global), `.opencode/rationale/*.md` (project) | only when improving the harness |

**Rule injection is deterministic** via the `opencode-rules` plugin (declared in global `opencode.json` and `tui.json`): it captures file paths from tool calls (`tool.execute.before`), matches them against each rule's `globs:`, and injects matching rules into the system prompt — surviving compaction. The TUI sidebar shows active/inactive rules live. Never remove the plugin entries or revert to prose-based loading instructions.

Devcontainer topology: `/mnt/opencode-host` is the editable global/user harness and replaces the normal `~/.config/opencode` role because the image-baked config is hardened. Repos may also have project-local `.opencode/`; currently the env-var-loaded global config can take precedence over project config, so diagnose project-level config misses as precedence issues before changing rules.

Reference direction is rule → context: each rule declares where it applies. Sharing is free — one file, N globs — so there is no inline-vs-materialized distinction and no per-subdomain AGENTS.md wiring. Keep `rationale/` outside `rules/`, or it gets injected.

Fragility note: the plugin relies on experimental opencode hooks (`experimental.chat.system.transform` et al.) — check on opencode upgrades.

Two-layer contract: @rationale/two-layer-harness.md

## Choosing the Fix

| Signal | Fix |
|---|---|
| Project domain information or documentation rule | Load `project-domain-documentation` |
| Wrong behavior during an activity/workflow | Update a **skill** |
| A gate lost to task pull (a stop, a read boundary, a hand-back skipped under the pull of the task) | Reframe the task so the gated action is its deliverable — a session, a turn rhythm, a first-turn stop |
| Wrong convention in one bounded context | Rule in `.opencode/rules/` scoped with `globs:` |
| Wrong project-wide convention | Frontmatter-less rule in `.opencode/rules/` |
| Wrong personal convention | Global `AGENTS.md` |
| Prescription right but reasoning stale | Update the **rationale** doc |

## Words Are Attractors

A precise term carves the semantic valley the agent falls into — cheaper than any gloss. Use the domain's own vocabulary; never name discarded things (negation doesn't kill an attractor). Full treatment: @rationale/attractors.md

## Writing Rules

Rules are always-on context — every token counts. Exhaust alternatives first (update existing, use a skill, context AGENTS.md).

- **If it does not apply project-wide, it must carry `globs:`** — a frontmatter-less rule is always-on; unscoped rules enforce wrong standards where they don't belong.
- **Globs over keywords.** `keywords:` fire on prompt wording — brittle and prone to over-broad matches; reserve for genuinely topical rules and avoid common words. `match: all` for AND logic across conditions.
- **One concept per file, cohesive files** — a fix should require reading and editing exactly one rule file. Lead with the constraint, then a brief why; deep argumentation goes to `rationale/`.
- Examples only when ambiguous without one; pick the one that best incarnates the principle — abstract rule first, then illustration.
- Name after the concept, not the symptom.

## Writing Skills

Skills are discovered by the `skill` tool from **name + description alone** — matching precision is everything.

- **The description is the trigger.** Write it with the exact words a session will contain at trigger time, and state when NOT to invoke. A vague description never fires; an over-broad one fires wrongly. Apply Words Are Attractors at full strength.
- Frontmatter: `name` + `description` required (description ≤1024 chars); name is lowercase-hyphenated and must match the folder name.
- Two flavors, same structure: **workflow** (steps + exit criteria) and **context** (ongoing guidance, no end).
- Always true regardless of activity → it's a rule, not a skill.
- Self-contained: enough context to execute; `@` refs if needed.

## Sub-Agents: Units of the Temporal Axis

Each step of a workflow runs as its own sub-agent, carrying ONLY the skills and information that step needs — e.g. TDD dispatches to a test-writer, a green implementor, a refactorer, each with its own minimal context. Skills are composable precisely because sub-agents load them deterministically.

- The workflow skill is the **orchestrator**: it defines the sequence and dispatches each step to its sub-agent instead of executing everything in one context.
- Composition mechanisms: the agent definition (`agents/<step>.md`, frontmatter `mode: subagent`, body = system prompt) **preloads** skills via a `skills:` frontmatter list — their content is in context from the first turn; the rules plugin's `agent:` frontmatter scopes rules to specific sub-agents. Step sub-agents get preloaded skills, never on-demand discovery — the orchestrator may use the `skill` tool, steps must not choose.
- When designing or fixing a workflow skill, ask per step: what is the minimal skill set and context for THIS step? Anything more leaks another step's concerns into it.

## Checklist

1. Existing rule/skill covers this? → update it
2. Permanent constraint → rule; activity-dependent → skill
3. Applies everywhere → global; else → composable rule / context AGENTS.md / skill
4. Foundation + touched-file rationales loaded, and still coherent with the fix?
5. If harness artifacts were created or changed, end by reminding the user to restart opencode; the running session keeps already-loaded config, rules, agents, and skills.

## Examples

VIOLATION — isolated apply: applied one item's fix while two others were still open; a later root cause subsumed it and the commit had to be reworked. Proposals cannot be taken in isolation — synthesis precedes application.

Meta-kaizen — when improving this skill itself, read: @rationale/collaborative-production.md, @rationale/shape-and-substance.md
