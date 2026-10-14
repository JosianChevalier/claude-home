---
tags: [atomic-commit, small-batches, git]
---

# Atomic commit

**Thesis.** The atomic commit is the smallest change that still works.

## One logical change, whole

An atomic commit is **one logical change, and all of it**. One: a single concern, which a reader can name in a line. All of it: production and its tests together, trunk releasable after it as before ([[philosophy/continuous-delivery]]). Both halves hold at once, or the commit is not atomic.

The enemy of the atomic commit is proximity. A cleanup noticed nearby, a comment removed while passing, a refactoring that touches the file the feature touches: each is a second concern riding on the first. It gets a commit of its own, or a line in the plan, never a seat in this one.

It is the floor of batch size ([[philosophy/small-batches]]): below the plan, the implementer's cadence. One rename. One extracted function. One moved variable. Seconds apart.

## Atomic and meaningful

Small is not the test. The commit must be atomic: an operation that cannot be split without breaking trunk. A rename across 12 files is one; counting lines or files measures the wrong thing. For a move the test is the diff: **glanceable**, its validity seen without reading the code ([[philosophy/mechanical-refactoring]]). Atomic for the trunk, glanceable for the reviewer.

Atomic is not enough: the commit must be meaningful, and a step is meaningful when the next step does not override it. Rename a to b, b to a, a to c is three atomic operations and one change, a to c. A step overridden right after was never a change; it folds into the step that overrides it, until the fold stands.

- Fold: an addition and its polish; a green step and the refactor that follows it; tests on one unit of behavior, which ask one functional change.
- Don't fold: a fix and a rename. Neither overrides the other, so two commits.

What stands is validated at once, by shape for a move, by the tests for a behavior.

The formal name is the **irreducible morphism** (category theory, in the spirit of Auslander–Reiten): an arrow that factors into two only trivially. A to c factors through b, trivially: a stop is trivial when the path could have been taken at once and the stop lightens no cognitive load.

## Why the unit matters

- **Loss.** A step that fails costs the step. The smaller it is, the less is redone, whether the failure is a red build or a rebase conflict.
- **Proof.** For a semantics-preserving move the commit is the proof unit: one move, one commit, one glanceable diff ([[philosophy/mechanical-refactoring]]).
- **Integration.** Trunk-based development is integration at this granularity and no other: the atomic commit is what keeps the overlap window seconds wide and every state of trunk whole ([[philosophy/trunk-based-development]]).

By hand, the atomic commit is the smallest change one can think of, taken for the epistemic action (Kirsh & Maglio, [[philosophy/mechanical-refactoring]]). Agentic, generation is cheap and the price moves to validating. It is the smallest possible change still, for another reason: to minimize cognitive waste at review, or context waste for an LLM as judge. Anything that folds is waste.

## The skill is splitting

Seconds between commits is not a pace to hold, it is what a well-split change produces. Teams that did not integrate at this granularity were not slow at committing; they could not see the small steps inside the large one.

The splitting is learnable, and most of it is mechanical: a refactoring decomposes into moves that are each safe by construction ([[philosophy/mechanical-refactoring]]); a hard change decomposes into making the change easy, then making the easy change, taken to its extreme ([[philosophy/make-the-change-easy]]). What is left after the mechanical part is the one concern the change was about, and it is small.

## Related

- The floor of batch size, below the plan: [[philosophy/small-batches]].
- Every commit releasable: [[philosophy/continuous-delivery]].
- One move, one commit, the commit as proof unit: [[philosophy/mechanical-refactoring]].
- Make the change easy, then make the easy change: [[philosophy/make-the-change-easy]].
- Where the floor pays: [[philosophy/trunk-based-development]], [[philosophy/agentic-trunk-based-development]].
