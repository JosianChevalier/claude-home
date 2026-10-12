---
tags: [atomic-commit, small-batches, git]
---

# Atomic commit

## One logical change, whole

An atomic commit is **one logical change, and all of it**. One: a single concern, which a reader can name in a line. All of it: tested, releasable, leaving trunk in a state as good as the one before ([[philosophy/continuous-delivery]]). Both halves hold at once, or the commit is not atomic.

It is the floor of batch size ([[philosophy/small-batches]]): below the plan, the implementer's cadence. One rename. One extracted function. One moved variable. Seconds apart, a few lines each.

## Same file is not same change

The enemy of the atomic commit is proximity. A cleanup noticed nearby, a comment removed while passing, a refactoring that touches the file the feature touches: each is a second concern riding on the first. It gets a commit of its own, or a line in the plan, never a seat in this one.

Small is not the test; same concern is. A one-line fix bundled with a one-line rename is two commits.

## Why the unit matters

- **Loss.** A step that fails costs the step. The smaller it is, the less is redone, whether the failure is a red build or a rebase conflict.
- **Proof.** For a semantics-preserving move the commit is the proof unit: one move, one commit, safe before the diff existed ([[philosophy/mechanical-refactoring]]).
- **Integration.** Trunk-based development is integration at this granularity and no other: the atomic commit is what keeps the overlap window seconds wide and every state of trunk whole ([[philosophy/trunk-based-development]]).

## The skill is splitting

Seconds between commits is not a pace to hold, it is what a well-split change produces. Teams that did not integrate at this granularity were not slow at committing; they could not see the small steps inside the large one.

The splitting is learnable, and most of it is mechanical: a refactoring decomposes into moves that are each safe by construction ([[philosophy/mechanical-refactoring]]); a hard change decomposes into making the change easy, then making the easy change, taken to its extreme ([[philosophy/make-the-change-easy]]). What is left after the mechanical part is the one concern the change was about, and it is small.

## Related

- The floor of batch size, below the plan: [[philosophy/small-batches]].
- Every commit releasable: [[philosophy/continuous-delivery]].
- One move, one commit, the commit as proof unit: [[philosophy/mechanical-refactoring]].
- Make the change easy, then make the easy change: [[philosophy/make-the-change-easy]].
- Where the floor pays: [[philosophy/trunk-based-development]], [[philosophy/agentic-trunk-based-development]].
