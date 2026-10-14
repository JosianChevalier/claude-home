---
tags: [refactoring, small-batches, conceptual-integrity, probe-sense-respond, planning]
---

# Make the change easy

**Thesis.** Make the change easy, then make the easy change (Kent Beck) answers one question: how do I make small steps? It is a rhythm, not two phases: the pair repeats, and each of its two moves opens into the pair again, until every step is small.

## Never two steps

A new feature has to go in. Making the change easy is redesigning, so that the design holds the feature nicely. Making the easy change is implementing the feature in the new design.

But the redesign is not that simple. It takes the pair in turn: making the change easy is refactoring, and the easy change is the redesign.

```
a feature
├ make the change easy: redesign, so the design holds the feature
│  ├ make the change easy: refactor
│  └ make the easy change: the redesign
└ make the easy change: the feature, in the new design
```

There are never only two steps. The feature goes in small steps as well, and so does the refactoring ([[philosophy/mechanical-refactoring]]). The pair is fractal: it holds for a plan as for a commit, because nothing in the argument mentions size.

And the pair repeats. One refactor and one redesign do not get there: refactor, redesign, refactor, redesign, and keep going.

## Finding the path

A redesign changes the code from one concept to another, and through the steps in between its conceptual integrity is broken (Brooks, [[philosophy/model-phenomenology]]): that is the valley (Kauffman).

A refactor keeps the concept, so it never goes down into the valley. Refactoring first leaves the redesign fewer broken steps to walk.

So the path goes through models that are not the target. Each keeps some level of conceptual integrity, and the code morphs progressively from one to the next:

```
model ─ refactor, redesign ─▶ model ─ refactor, redesign ─▶ model ─ … ─▶ target
                              not the target                not the target
```

Making the change easy is finding that path, one that can be done in small steps: each step reaches an adjacent possible, and the depth of the valley to walk in is kept to the least.

That is all the aphorism is about. It is the same small step as the atomic commit ([[philosophy/atomic-commit]]), small batches ([[philosophy/small-batches]]) and continuous delivery ([[philosophy/continuous-delivery]]).

## One kind of step at a time

A step is one of three kinds ([[philosophy/mechanical-refactoring]]):

| Step | Changes | Tests | Validated by |
|---|---|---|---|
| Refactor | nothing: the model holds | preserved | the shape of the diff |
| Redesign | the model | can break | understanding |
| Feature | what the code does | change with it | the tests |

Done together, each obscures the other — a diff that moves code *and* changes behavior cannot be verified for either. Taken apart, each is verified its own way, and what lands on prepared ground is small enough to prove correct.

This is separation of concerns applied to *time* rather than space: not "which module owns what" but "which commit carries what".

## Preparing first costs less

Reshaping first is not aesthetics — it changes the economics. Implementing against a misfit structure means paying the structural cost *inside* the feature: workarounds, conversions, edge cases born from the mismatch. Paying it upfront, as a separate step, makes the implementation trivial — and the total cost lower, because workarounds compound while preparations don't.

The epistemic bonus: reshaping is the cheapest probe, since what a change will reveal cannot be known before acting ([[philosophy/planning-is-everything]]). It surfaces model tension ([[philosophy/model-phenomenology]]) before the feature is half-built, while backing out is still cheap.

## The change shows what to clean next

Implementation reveals structure that preparation couldn't foresee — the new code, once in place, shows its own misfits. Cleaning up right after harvests that revelation while it is fresh and cheap, instead of leaving it as debt.

So the pair alternates and has no last step: the cleanup after one change is the making easy of the next.

## Related

- Refactor and redesign, and the line between them: [[philosophy/mechanical-refactoring]].
- The small step itself: [[philosophy/atomic-commit]], [[philosophy/small-batches]], [[philosophy/continuous-delivery]].
- Why acting is the only way to know: [[philosophy/planning-is-everything]].
- Model tension, the felt misfit that reshaping surfaces: [[philosophy/model-phenomenology]].
- The aphorism as doctrine, this file as its pointer: [[philosophy/harness-shape]].
