---
tags: [refactoring, atomic-commit, verification]
---

# Mechanical refactoring

**Thesis.** Refactoring costs no understanding; understanding is spent on the model, and only there.

## Safe by construction

Reading refactored code is taxing because the reader reconstructs the old behavior, the new, and compares. The cost grows with the code's complexity, and the error rate with it. It is not inevitable.

Any refactor, however large, decomposes into **moves**: rename, extract a function, inline a variable, move a side-effect-free line, delete dead code. A move is semantics-preserving by construction: equals substitute for equals, whatever they denote (Leibniz). A tool could apply or verify it. Tests confirm the move; they are not what makes it safe. The safety lives in the process, not in the reader.

Safe moves chain: proof composes. A single large step must be proven from scratch, and the only proof available is understanding the code, which is exactly what the small step was meant to spare.

## The diff is its own proof

A move is validated by the **shape** of the diff, not the meaning of the code: this is a rename, every occurrence changed, nothing else moved. The cost is one glance, whatever the code does.

Call such a diff **glanceable**: its validity is seen, not read, the way a word is recognized without being spelled. Glanceable is a property of the diff as presented, not of its size. A rename across 12 files is glanceable; the same rename interleaved with a reformat is not.

If a diff is not glanceable, it is not a move. Split it into moves that are, or admit it is something else and treat it as such.

## Limit of applicability

Substitution holds where the code is **referentially transparent**.

Side effects make the code opaque, and a move acquires preconditions (Opdyke): safe a priori once they hold, applicable after a check.

| Tier | Moves | Holds on |
|---|---|---|
| 1 | rename, extract, inline | any code, spaghetti included |
| 2 | reorder, loop to map | side-effect-free, functional-style code only |

For a tier 2 move, the check verifies the precondition: it surfaces every use of what the move touches, and its reach grows with coupling. Tier 1 moves do the groundwork until the code is side-effect-free and the check vanishes: the moves presuppose that design and produce it, practices reinforcing each other ([[philosophy/agentic-extreme-programming]]).

## The boundary: redesign

A refactor does not change the underlying model, so tests and observable behavior are preserved. A redesign changes the model and can break the tests. Behavior may still be preserved, but knowing it takes understanding the old and the new: it cannot be mechanical.

That is the boundary of the claim: moves cost no understanding as long as the model holds. Where the model changes, the work is a redesign, taken in steps of its own and alternated with the refactors that prepare it ([[philosophy/make-the-change-easy]]).

## Act first, understand after

Because moves are safe without understanding, refactoring is how understanding is acquired, not what follows it. It is an **epistemic action** (Kirsh & Maglio): an action taken to make the problem easier to think about, the way Tetris players rotate a piece on screen rather than in their heads. Faced with opaque code: rename what is legible, extract what repeats, inline what obscures, and the model surfaces.

The reverse order, read until understood then rewrite, puts the risk in the wrong place: understanding is the fallible step, and a rewrite on a partial understanding silently drops the cases the reader missed. Moves drop nothing; they never depended on the reader's model.

Rewriting is the anti-move. The tempting moment is mid-chain: "I see what this does now, let me write it properly." The clarity was produced by the chain; a rewrite trades its accumulated proof for a bet on the reader's model. Keep chaining: the clean version is reachable by moves, and arriving by moves means arriving proven.

## Agentic

Generation is cheap and validation is the price ([[philosophy/agentic-trunk-based-development]]). A glanceable diff is validated without spending any cognition on what the code means, and the commit is its proof unit ([[philosophy/atomic-commit]]).

The epistemic action moves to the agent. Dictating each move costs more than it gives: one coarse instruction, clean up in place, and the human reasons over the cleaned shape.

A cleaning pass always pays for the agents that follow. The code is context: tangled, it carves the wrong semantic valleys ([[philosophy/attractors]]); cleaned, it realigns them for every later step. Run it as its own step, a temporal cut ([[philosophy/context-splitting]]): clean, then change.

## Related

- One move, one commit, the commit as proof unit: [[philosophy/atomic-commit]].
- Refactor and redesign alternated: [[philosophy/make-the-change-easy]].
- Validation as the price: [[philosophy/agentic-trunk-based-development]].
- Practices that reinforce each other: [[philosophy/agentic-extreme-programming]].
