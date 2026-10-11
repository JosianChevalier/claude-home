---
name: write-plan
description: Use when given a spec or requirements for multi-step work, before touching code, or after brainstorming validates a design.
---

# Write Plan

"Write a plan" opens a **planning session** — a collaborative activity, not a file request. The conversation is the planning act; after calibration validates the shape, the file becomes the task's working artifact.

The plan file is an artifact for agents. The human validates from chat, at map altitude — never by reading the file.

## Session phases

**1. Calibrate — your first response, always.**
Reply with:
- Working model in 2-5 bullets.
- At most ONE question, if an answer could change scope, sequencing, architecture, or semantic contract. Name both answers and the divergence. Consequential means the answer changes which concept the plan commits the code to; scope, sequencing, and architecture follow from that. Stage naming, map style, and format are medium: yours.
- Smaller consequential points: "Assuming X unless you object."
- If nothing is consequential: say so — "No consequential unknowns; ready to write."

Your turn ends here. This response is the deliverable. Repo evidence resolves implementation questions, not domain ambiguity — a term with multiple referents in the codebase is consequential by default.

**2. Skeleton.** Write `docs/plans/YYYY-MM-DD-<topic>.md` only after a user turn following calibration. Unobjected assumptions are confirmed; do not re-ask. Start with the smallest useful skeleton: Goal, Map, Completed, current decisions/context, and staged direction.

**3. Converge.** Discuss until the model settles. Everything needed to decide comes into chat; never ask a question whose answer requires opening the file. Update the skeleton as decisions land.

**4. Working draft.** Iterate the plan as the shared model changes. Before each hand-back, update the file if a fresh session would otherwise lose a decision, finding, open thread, or real next step. Distill; do not append a transcript.

**Standing rule — every hand-back leads with the Map in chat.** From the moment the plan takes shape (skeleton onward), every response to the user OPENS with the current Map rendered directly in chat — never a pointer to the file, never "see the plan for details". The user validates direction and coherence from this rendering and iterates on it; opening the file is opt-in. Fast feedback, low cognitive load.

**5. Review.** Dispatch the **plan-reviewer** agent on the file once it is usable. It checks two mechanical things: (a) every node, at every depth, ends working, releasable, zero regression; (b) everything a node introduces is on the live path by the end of that node or the next — otherwise FAIL. Ordering only, never scope or design. Apply its fixes (reorder, split, nest) before checkpoint; surface any FAIL you disagree with to the user instead of silently overriding it.

**6. Checkpoint.** Render in chat: the Map, each stage with its north star condensed to one line, and the key decisions. Ask whether it matches. The user validates from chat, not by opening the file. The plan remains a living artifact until the work ends.

## Minimum Skeleton

Every plan needs a **Goal**, a **Map**, a **Completed** section (filled during execution), and **Stages** — a tree, not a list. Beyond that, add whatever sections the context demands — diagrams, domain context, constraints, decisions, references.

**The Map is the human's view — mandatory, never skipped.** A short summary of how the plan attacks the goal, self-sufficient: readable by someone who has not seen the code it touches. It is NOT the stage list at lower resolution — it is a different level of information: it summarizes, and may add explanations the stages don't carry (why this slicing, what depends on what, where the risk sits). Before rendering the Map, lead internally with the interrogation: **what is the best way of representing the current plan visually?** Visual form required: an ascii diagram, pseudo-code sketch, table, arrow chain (`parse -> validate -> persist`), indented list, or another compact shape that makes the structure legible at one glance. Do not default to arrows; use them only when the plan is truly linear. The Map renders the tree's shape — functional stages and how each nests; an indented list is the natural form when nesting is the point.

**The Map is a you-are-here map.** It holds the whole route — walked, current, ahead — with the position marked in the file. How it is marked is medium, yours: check marks, an arrow, a pin, whatever the Map's form carries at a glance. Done nodes never leave the Map; only their stage entries below collapse into Completed. Whenever stages are added, reordered, rewritten, dropped, or done, the Map is updated in the same edit; a stale Map is worse than none.

**Every stage opens with its north star** — one artifact that makes the stage's aim clear at one peek. Mandatory on every functional stage and every leaf; intermediate nodes carry a one-line aim. Ask separately for each: **what is the best way of representing this stage visually?** Stages may be heterogeneous: one stage may need pseudo-code, the next a dependency diagram, the next a before/after shape. Use a pseudo-code snippet, target-code fragment, ascii diagram, table, state sketch, or another compact artifact. Intent, not prescription — execution owns the details. Its job: someone lost mid-flow (the engineer peeking at the current stage's bullet, or an agent deep in a complex change) looks at the top of the stage and re-orients instantly.

Record decisions already made. Do not record unresolved questions unless the user explicitly chooses to defer them.

## Principles

**Stages form a tree.** A functional stage (`1`) returns value and information. It decomposes into technical sub-stages (`1.1`, `1.2`, `1.2.1`…) that each end working, zero regression, live — recursively, as deep as the work is layered. The leaf is what one driver finishes in one sitting without context drift; atomic commits stay below the plan. A node that cannot end green and live is too large or sliced on the wrong axis — nest it, never enlarge it.

**Node boundaries are observable saved points.** Safety invariants hold at every node end; when a node cuts through domain state, dispatch **aggregate-identification**.

**Slice across layers.** Do not plan as "database, then domain, then UI/API wiring" unless each layer-only move is a behavior-preserving reshaping node. Prefer thin end-to-end increments over architectural layer batches; layer-touching nodes are legitimate only nested inside a functional stage they serve.

**Intent at every depth.** No file lists, no step-by-step instructions — at the leaf as at the root. Depth is not detail: a leaf is narrow in scope and still stated as intent; execution owns the how.

**Expose last — the keystone stage.** A public contract (API surface, frontend contract, published naming or documentation) goes live only after the behavior behind it is effective and verified by tests. Documenting or advertising a contract *is* exposure — a plan with "Contract Naming" or API docs before the backend stages that make it real promises behavior that doesn't exist. Order: behavior effective → verified → exposed/documented → legacy removed. Sole exception: an explicitly contract-first goal, where the plan states the contract carries no implementation claim.

**Follow the workflow rhythm.** Do not mix non-trivial reshaping with behavior change in the same node. First make the change easy with a behavior-preserving reshaping node, then make the easy change with a small behavior node on prepared ground. If implementation exposes new structural debt, add a cleanup node after the behavior node.

**Change in place.** Reshaping an existing live workflow is done on the live path, as a chain of mechanical, behavior-preserving moves — each node transforms the code that runs, and stays live. Never plan a dark replacement of a live workflow followed by a "switch" stage: that is the big batch. An alternative flow (adapter, expand/contract, parallel branch behind a flag) is allowed only for the smallest atom that cannot be transformed in place without regression, and that atom goes live in the same node once parity is proven. The keystone order (dark first, expose last) is for new behavior with no existing live path.

**Just in time.** A node introduces only what is on the live path by the end of that node or the immediately next one. No node defines contracts, seams, interfaces, or helpers for later nodes to consume — those are inventory, and later nodes bend to fit the guess. If a node needs a contract, that node creates it and adopts it.

**Probe divergent alternatives.** When an alternative surfaces whose trade-offs resist discussion, dispatch the **prototyping** skill instead of arguing; findings come back into chat, and the plan records the decision.

**Prototypes inform, never commit.** A plan downstream of a prototype separates: observations from the prototype, decisions accepted, semantics still under review, implementation stages. Public/API exposure comes only after the behavior stage is effective; prototype code is evidence, never a stage.

**Mark siblings as sequential or parallel.** Parallel only when scopes do not overlap, so the user can dispatch agents accordingly.

**Leaves are synchronization points.** Inventory between leaves is measured in hours. A coarse leaf is a hidden big batch.

**Be concise but precise.** Plans are shared context between independent agents — optimize for context engineering.

**Expect evolution.** The plan is direction, not a contract. Nodes will be rewritten, reordered, nested, or dropped as reality unfolds.

## Iterating on the Plan

Update the plan when:
- We receive user feedback that changes the approach
- We choose a prototype (document the decision and selected option)
- A probe or discussion changes what the next session needs to know

Any stage change updates the Map in the same edit.

**Rule of thumb**: If the user makes a decision that affects how work will be done, update the plan immediately. If control returns to the user and the session could die, the plan must already preserve the current state.

## Examples

Two failure families: **interrogation** (the medium returned up the belt: questionnaire, forced question) and **silent choice** (a concept decided below: silent guess).

VIOLATION — same-turn write: stated an assumption, then wrote the file in the same turn. Disclosure is not validation; calibration ends the turn.

VIOLATION — questionnaire: "Before I start: 1) Which format? 2) Sequential or parallel stages? 3) Any constraints?" This is not planning, it is offloading triage onto the user. Asking a question you could have resolved by triage is a failure, not diligence.

VIOLATION — forced question: "Should stages be numbered or named?" No divergence in scope, sequencing, or architecture. Asking this signals you skipped triage and are performing caution.

VIOLATION — silent guess: user says "plan the sync feature", you pick one-way sync without saying so and deliver a polished plan. A clean artifact built on an unstated interpretation is the worst outcome: it looks done and is wrong. Worse than any question.

VIOLATION — flat plan: "Stage 1: importer end-to-end (schema, parser, validator, diff, API)". One stage, five layers, feedback at the end. Correct:

```text
1 importer never corrupts the ledger
  1.1 schema + parser, live behind the existing path
  1.2 validate + dry-run diff
    1.2.1 row validation
    1.2.2 diff report
  1.3 commit path
```

VIOLATION — dark replacement path: "Stage 1: extract resolver seam. Stage 2: extract matcher seam. Stage 3: extract merger seam. Stage 4: switch live routing to the new seams." Three stages of inventory, one big-bang integration. Correct: each stage extracts one seam from the live path and adopts it live in the same stage; there is no switch stage.

VIOLATION — future-contract inventory: "Stage 1: define the candidate-selection, scoring, and merge interfaces that stages 2–5 will implement." Stage 1 ships guesses about shapes nothing uses yet. Correct: Stage 1 introduces only the first seam it adopts; later stages create their own contracts when they consume them.

VIOLATION — stale map: a probe reordered stages 3 and 4; the stages were rewritten but the Map kept the old order. The user validated direction from an obsolete map. Map and stages change in the same edit, always.

VIOLATION — Map as forecast: stage 1.1 done, agent deleted it from the Map. The next session sees a route with no origin and cannot tell where it stands. Done nodes stay, marked done; the position moves.

Sharp (good): "Assuming 'sync' means one-way export to the CRM. If it's two-way, we need conflict resolution and the stages roughly double. Which?" — two answers, named divergence.

Correctly silent (good): spec fixes API, storage, and rollout. "No consequential unknowns; ready to write." Turn ends; the user's "go" unlocks the skeleton.

Good Map examples (choose by fit, not habit):

```text
importer never corrupts the ledger
fetch -> parse+validate -> dry-run diff -> commit path -> expose API
dry-run exists so damage is visible before anything writes
```

```text
                 +------------------+
incoming file -> | quarantine parse | -> invalid rows report
                 +------------------+
                           |
                           v
                    valid ledger diff -> reviewed commit
```

```text
for each inbound event:
  normalize into canonical command
  reject if account boundary is crossed
  save command + audit record in one transaction
```

Good Map mid-execution (one way of marking position; pick what fits the form, it just needs to say "you are here"):

```text
  1 importer never corrupts the ledger
✓   1.1 schema + parser, live behind the existing path
→   1.2 validate + dry-run diff      damage visible before anything writes
✓     1.2.1 row validation
→     1.2.2 diff report
      1.3 commit path
  2 expose API                       after 1 is verified
```

Good stage north stars (heterogeneous by stage):

```text
Stage: preserve current behavior while moving the seam

old handler -> adapter -> existing service
new handler -------^
```

```text
Stage: make duplicate submission idempotent

if submission_id already processed:
  return stored result
else:
  validate -> charge -> persist result
```

Rationale: @rationale/small-batches.md, @rationale/continuous-delivery.md, @rationale/change-in-place.md, @rationale/mechanical-refactoring.md, @rationale/workflow-rhythm.md, @rationale/collaborative-production.md, @rationale/shape-and-substance.md, @rationale/session-state-in-documents.md, @rationale/prototypes-are-probes.md, @rationale/zoom-levels.md, @rationale/transmission-belt.md, @rationale/kairos-gates.md
