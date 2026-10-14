---
tags: [agentic-extreme-programming, practices, batch-size]
---

# Agentic extreme programming

**Thesis.** A coherent set of practices asks for no trade-off, agentic programming included: its practices reinforce each other, and pushing one further pays on all the others.

## Synthesis, not middle ground

The dominant intuition is that software development is trade-offs: quality against speed, review against waiting, autonomy against coherence. So we arbitrate, look for the right dosage, compensate.

XP says the reverse: turn all the knobs to 10 (Beck), turn up the good (Zuill). Good practices are complements (Milgrom & Roberts): each raises the return of the others. Testable code is better cut; better-cut code ships faster. The capability map that closes Accelerate draws it: everything enables everything.

What most readers of Accelerate missed: flow metrics and quality metrics are correlated. Teams that ship faster also fail less. Flow practices do not trade speed for quality, they give both. The usual search for a middle ground, enough speed and enough quality, looks for a trade-off the data does not show.

**Feeling pulled between two sides is the test: the set is not coherent.** The question is never which side to pull.

## The optimum is tiny

Batch size has an optimum (Reinertsen, [[philosophy/batch-size-economics]]), and it is not fixed: lower the transaction cost and the optimum follows it down. A pipeline does not pick a better truck size, it removes the truck. The optimum stops at a floor: the smallest change that still works, in software the atomic commit ([[philosophy/atomic-commit]]). An optimum on a floor is not a dosage: the knob is at 10.

The cost is made near zero, not found there: infrastructure, structure and practices are built. What is left to decide is not a trade-off between practices: nothing to choose between them, nothing to adjust so that one does not go too far. It is how far to go into them: how much is invested against how much comes back. Going deeper does not always pay enough. But what is invested in one practice pays in the others.

## Crossing the valley

Practices that depend on each other make a rugged fitness landscape (Wright, Kauffman). One adopted alone lands in a valley: trunk commits without fast tests and small steps are worse than branches. Teams try one, watch it fail, and conclude it was a trade-off.

Selection on feedback alone only climbs, and stops at the nearest peak. Crossing takes a theory: knowing why the practices work together is what holds the course while things get worse.

## Agentic

It held for XP and it holds agentic. The practices are not exactly the same set: they have been rethought for agentic programming.

Tokens, context, cognitive load, feedback time, precision and quality move together. The practices of the harness hold each other up:

- A lean context keeps the most capable model affordable as the default; a capable model errs and struggles less, which keeps the context lean ([[philosophy/model-tiers]]).
- A small context makes each decision more reliable, and a decision that holds is not paid for twice in tokens ([[philosophy/compounding-decisions]]).
- A cut in time opens a cut in space, and the reverse ([[philosophy/context-splitting]]).
- Mechanical moves presuppose side-effect-free design and produce it ([[philosophy/mechanical-refactoring]]); each is one glanceable diff, one move to a commit ([[philosophy/atomic-commit]]).

None of them is bought with another.

## Related

- The smallest batch: [[philosophy/atomic-commit]]; why it is the optimum: [[philosophy/batch-size-economics]].
- The practices on trunk: [[philosophy/trunk-based-development]], [[philosophy/agentic-trunk-based-development]].
- One instance, the design the moves presuppose and produce: [[philosophy/mechanical-refactoring]].
