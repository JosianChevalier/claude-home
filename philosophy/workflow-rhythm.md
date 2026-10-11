---
tags: [refactoring, probe-sense-respond, planning]
---

# Rationale: Workflow Rhythm

Why every functional change is two moves — make the change easy, then make the easy change (Kent Beck) — and why the rhythm repeats at every scale.

## Separating the two hard things

A change mixes two concerns: **where the code should be shaped** (structure) and **what it should do** (behavior). Done together, each obscures the other — a diff that moves code *and* changes behavior cannot be verified for either. Splitting them restores verifiability: a refactoring diff proves behavior is preserved; a behavior diff, landing on prepared ground, is small enough to prove correct.

This is separation of concerns applied to *time* rather than space: not "which module owns what" but "which commit carries what".

## Preparation lowers the cost of the change

Reshaping first is not aesthetics — it changes the economics. Implementing against a misfit structure means paying the structural cost *inside* the feature: workarounds, conversions, edge cases born from the mismatch. Paying it upfront, as a separate refactoring, makes the implementation trivial — and the total cost lower, because workarounds compound while preparations don't.

The epistemic bonus: reshaping is the cheapest probe, probe in the planning rationale's sense: what a change will reveal cannot be known before acting ([[philosophy/planning-is-everything]]). It surfaces model tension ([[philosophy/model-phenomenology]]) before the feature is half-built, while backing out is still cheap.

## Fractal, because the argument is scale-free

The two-move rhythm holds at plan scale (reshaping stages before feature stages), execution scale (atomic refactoring before TDD), and commit scale (refactoring commits before behavior commits) — because nothing in the argument mentions size. Verifiability, cost, and probing apply identically to a rename and to a plan stage; only granularity changes. A "make it easy" plan stage may itself contain refactoring → TDD cycles internally.

## Cleanup closes the loop

Implementation reveals structure that preparation couldn't foresee — the new code, once in place, shows its own misfits. Cleanup after (at every scale) harvests that revelation while it is fresh and cheap, instead of leaving it as debt for the next change's preparation phase. The rhythm is really three beats — prepare, implement, polish — with the third feeding the next cycle's first.
