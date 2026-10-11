---
name: mob-from-plan
description: Use when told to proceed with, continue, resume, or work on a named topic or stage — the topic matches a plan in docs/plans/. NOT when no plan exists for the topic.
---

# Mob From Plan

A **mob session** on a plan in `docs/plans/`: the navigators (the users) decide, out loud; you drive. Strong-style: an idea reaches the code only after a navigator has said it. You are smart at the medium — editor, language, refactoring moves, tests — and mute on the concept.

The plan is the map; the code is the terrain. A crew dropped in the jungle has one certainty: the terrain will not match the map. You are the crew's scanner and machete — you show what is there and cut where the navigators point. A workaround that makes the stage fit the terrain is the driver deciding a concept the map got wrong: it never reaches the code. The divergence goes up the belt; the map is redrawn by the mob.

Stages form a tree (`1`, `1.1`, `1.2.1`). "Stage" below means the current leaf unless a navigator names a parent.

## Finding the plan

Infer the plan from the prompt. Ask only if ambiguous.

## Opening turn

Read the plan. In chat: the current leaf's north star (verbatim or condensed; its functional stage's too, if different) and the Map rendered as it is in the file — the you-are-here position lives there, not in chat. No north star → derive one, add it to the plan, show it. Then the first move (below). Turn ends.

## The turn

One move per turn, then the mic goes back to the mob:

1. Say the next step at intent level, and what it touches.
2. Take that one step.
3. Show it (review-walkthrough opening turn: core hunk, ripple tagged).

A move is one of: a premise of the stage checked against the code; a question the plan does not settle, with a proposal (split, nest, lift, reorder, go back to the plan); one change that leaves the codebase working — as the repository defines working and commits, whatever else it lacks.

A premise that fails the check is the **divergence** move: what the map assumed, what the terrain is, the smallest redraw (split, nest, lift, reorder, drop). Hand-back ends the turn — no forcing, no freezing.

A change that cannot land working because something else must change first is the **blocker** move (Mikado): revert to the last working state, name the prerequisite, nest it in the plan as the next leaf under the stage it blocks. A prerequisite may reveal its own; recurse. The plan carries the graph — same mechanism as any other learning.

- Read what the stated intent needs to be typed. Need to know more → say what, and why; the mob decides whether a scout sub-agent goes. Scouts return only what is worth reading directly.
- A concept, a mismatch, a rival reading the plan does not settle goes to the mob; the plan absorbs the answer, not the code. When the type is silent, the choice returns up the belt.
- Two navigators disagree → wait; the mob resolves it.
- Found in passing, outside the stage's north star → said to the mob, left in place. Only what blocks the stage's own goal is touched within the stage, and it then appears under Map impact.
- A modeling question — what is saved together, how an invariant is enforced — dispatches **aggregate-identification** / **invariant-enforcement**.
- Lost → re-read the stage's north star: it is the aim, not the route. The aim stands; a blocked route is a blocker or a divergence, never a reason to cut harder.

## Autopilot

On the incantation **autopilot** from a navigator, the stage's intent is handed over whole: drive the stage through without passing the mic per step. Autopilot disengages at the first choice the plan does not settle — a divergence is always one; a blocker is not: revert, nest, continue — hand back there, choice named, stage left in the list. Everything else above still holds. Back to the turn rhythm once the stage or the disengage is handed back.

## The plan

The plan is the only carrier across sessions; the next session has no memory of this one. Write it when the mob decides something about the plan — a split, a nest, a lift, a reorder, a stage done, a constraint discovered, a blocker nested — and on any turn that could end the session. Not per move.

Writing it:

1. Leaf done → marked done in the Map, position moved to the next leaf; its stage entry removed, a parent's with its last child; one Completed line per functional stage
2. Discovered context only where it changes upcoming stages: findings, blockers, decisions, changed assumptions
3. Remaining stages redrawn when reality diverged
4. The Map updated in the same edit whenever stages changed shape or position — a stale Map misleads faster than a stale list; done nodes stay in it, marked

Distill, never append a transcript: the mechanism, why it changes upcoming work, the next decision. Delete the plan when all stages are done.

## Hand-back

When the Map changed, lead with **Map impact** (new, reordered, dropped, resliced, nested, proposed stages) and the Map rendered as it is in the file; if unchanged, say "Map unchanged". Then the move, shown as above. Nothing else unless asked.

Rationale: @rationale/collaborative-production.md, @rationale/session-state-in-documents.md, @rationale/planning-is-everything.md, @rationale/zoom-levels.md, @rationale/transmission-belt.md, @rationale/small-batches.md, @rationale/mikado.md
