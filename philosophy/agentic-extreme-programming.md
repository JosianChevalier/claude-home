---
tags: [agentic-extreme-programming, practices, batch-size]
---

# Agentic extreme programming

**Thesis.** A coherent set of practices asks for no trade-off: its practices reinforce each other, and pushing one further pays on all the others.

## Synthesis, not middle ground

The dominant intuition is that software development is trade-offs: quality against speed, review against waiting, autonomy against coherence. So we arbitrate, look for the right dosage, compensate.

XP says the reverse: turn all the knobs to 10 (Beck), turn up the good (Zuill). Good practices are complements (Milgrom & Roberts): each raises the return of the others. Testable code is better cut; better-cut code ships faster. The capability map that closes Accelerate draws it: everything enables everything.

It held for XP and it holds agentic, with the same practices. That is the point of this file: agentic work needs no new balance, it turns the same knobs further.

Feeling pulled between two sides is the test: the set is not coherent. The question is never which side to pull.

## The optimum is tiny

Batch size has an optimum (Reinertsen): transaction cost against holding cost. The curve is not fixed. Lower the transaction cost and the optimum follows it down, in software to the atomic commit ([[philosophy/atomic-commit]]). A pipeline does not pick a better truck size, it removes the truck.

The cost is made near zero, not found there: infrastructure, structure and practices are built. That is the one trade-off left: how much to invest against what it gives back. Going deeper does not always pay enough. But what is invested in one practice pays in the others.

## Crossing the valley

Practices that depend on each other make a rugged fitness landscape (Wright, Kauffman). One adopted alone lands in a valley: trunk commits without fast tests and small steps are worse than branches. Teams try one, watch it fail, and conclude it was a trade-off.

Selection on feedback alone only climbs, and stops at the nearest peak. Crossing takes a theory: knowing why the practices work together is what holds the course while things get worse.

## Agentic

Tokens, context, cognitive load, feedback time, precision and quality move together. Each practice of the harness pays on several at once:

- A small context costs less and is more precise ([[philosophy/context-economics]]).
- A precise term pulls harder per token than its explanation ([[philosophy/attractors]]).
- A message written for a reader with nothing open spares the human and stays short ([[philosophy/conversation-as-interface]]).
- Fewer decisions asked of the agent means fewer errors and less to validate ([[philosophy/compounding-decisions]]).
- A glanceable diff is validated without understanding ([[philosophy/mechanical-refactoring]]), on a commit small enough to be one ([[philosophy/atomic-commit]]).

None of them is bought with another.

## Related

- The smallest batch: [[philosophy/atomic-commit]].
- The practices on trunk: [[philosophy/trunk-based-development]], [[philosophy/agentic-trunk-based-development]].
- One instance, the design the moves presuppose and produce: [[philosophy/mechanical-refactoring]].
