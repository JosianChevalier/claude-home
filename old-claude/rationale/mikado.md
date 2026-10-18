---
tags: [mikado, small-batches, atomic-commit, planning]
---

# Rationale: Mikado

Why a change that cannot land working is reverted, not pushed through — and why the thing that stopped it becomes the next step.

## The attempt is information; the broken state is inventory

Ellnestam and Brolund's Mikado method: try the change you want; if it breaks, note what would have to be true for it to work, revert, and go make that true first. Prerequisites form a graph rooted at the goal; leaves are done first, each one landing on a working codebase.

The split is the point. A failed attempt has produced two things: knowledge of a prerequisite the map did not list, and a codebase that no longer works. The first is the only product software development has (@rationale/planning-is-everything.md). The second is design-in-process inventory of the worst kind ([[philosophy/batch-size-economics]]): it cannot ship, it blocks every subsequent step, and it grows with every fix layered on top of it. Reverting keeps the first and drops the second at the cost of retyping a change already understood — the cheapest thing in the session.

Pushing through does the opposite: the prerequisite gets solved *inside* the broken state, entangled with the change that revealed it, and the codebase stays not-working for as long as the entanglement takes to unwind. Mechanical refactoring already says it at commit scale — a move that "needs" a tweak to compile is two commits (@rationale/mechanical-refactoring.md); Mikado says it at any scale: the tweak comes *first*, on a working base.

## Working, as the repository defines it

The invariant is that the codebase works after each step as it did before. What *working* means — compiles, existing suite green, a manual check, a deploy — and when it is committed belong to the repository's doctrine, not to the method. A legacy codebase with no suite has a weaker floor; it still has one, and the revert discipline is how the floor is not lowered further.

## Blocker and divergence are different moves

A **blocker** is the terrain needing a step the map did not list; the destination stands, the route gains a node. It lives at the medium level: the driver can name it, revert, and propose the leaf, and autopilot can absorb it. A **divergence** is the map's premise being wrong; the destination itself is in question. It lives at the concept level and returns up the belt (@rationale/transmission-belt.md). Confusing them costs in both directions: a blocker treated as divergence interrogates the mob about the route; a divergence treated as blocker has the driver redrawing the map in the code.

## The graph lives in the plan

The Mikado graph is a subtree of the plan's Map: the prerequisite nests under the stage it blocks, the recursion nests deeper. No separate artifact — the plan is already the carrier of what we learned and what we will do next (@rationale/session-state-in-documents.md).
