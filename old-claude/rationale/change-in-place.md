---
tags: [refactoring, planning, continuous-delivery, small-batches]
---

# Rationale: Change In Place

Why reshaping an existing live path is done *on* the live path, by chaining mechanical moves, and why a dark replacement path is the big batch in disguise.

## The default: transform, never rebuild alongside

An existing live workflow is changed by transforming it where it stands: a chain of semantics-preserving moves (@rationale/mechanical-refactoring.md), each one live the moment it lands. The path from old shape to new shape is a sequence of always-valid programs — the code never leaves production, it just changes shape under it.

The alternative — build the new shape beside the old one, then switch — looks safe because the new code is dark (@rationale/continuous-delivery.md). Operationally it is. Economically it is design-in-process inventory (@rationale/small-batches.md): every unadopted seam is a bet whose outcome is unknown until the switch, and the switch is where all the deferred integration risk lands at once. Little's law applies — lead time = work in process ÷ throughput — so each dark seam lengthens the time before *anything* is validated in production. A multi-stage dark replacement is a big batch wearing a keystone costume.

## Alternative flows only at the smallest atom

Sometimes a step cannot be made in place without regression: the new behavior needs a different shape at a boundary the old callers depend on. Then, and only then, use an alternative flow — expand/contract, an adapter, a parallel branch behind a flag. Two constraints:

- **Smallest atomicity.** The alternative flow covers the one atom that cannot be transformed in place — not the function around it, not the workflow around that.
- **Adopted in the same stage.** The atom goes live in the stage that introduces it, once parity is proven. It is never left dark for a later "switch" stage.

The keystone order (dark first, expose last) is for *new* behavior with no existing live path. Replacing existing behavior is not new behavior; it is refactoring, and refactoring is in place.

## Just in time: no inventory before consumption

Nothing is created before the thing that consumes it. A contract, a seam, an interface, a helper exists only when a caller is about to use it — Poppendieck's *last responsible moment*: decide when the cost of waiting exceeds the cost of deciding, not earlier. "Stage 1 defines the seams stages 2–5 will use" is inventory: those seams are guesses about shapes not yet needed, and the later stages will bend to fit them instead of the reverse.

The test for any stage: **everything it introduces is on the live path by the end of that stage, or the next one.** If not, the stage is building inventory.

## Escape hatch, made explicit

"New code runs as fast as possible" does not mean "never dark". A behavior change that must not be user-visible yet goes live behind a flag or toggle — reachable, exercised, invisible. Dark code is legitimate for the thinnest possible keystone of new behavior, and for a single atom awaiting parity within its own stage. It is not legitimate as a place to accumulate a replacement.
