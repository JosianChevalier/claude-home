---
tags: [feedback-loops, cynefin, small-batches, continuous-delivery]
---

# Feedback loops

**Thesis.** XP's nested feedback loops (Beck; the diagram, Wells), redrawn for how we work now: every change is a hypothesis, and the loops that test it nest, from the code up to the domain. Continuous practices fit the loops one onto the next; agility pulls the outermost toward them.

## The loops

Several of XP's loops no longer hold for us. Pair programming and the stand-up give way to mob programming. The iteration plan gives way to continuous delivery, and to product engineering teams with full control, free to probe, sense, respond. What we see instead, from the outermost in:

1. **Domain.** The change holds in the domain we are embedded in. Feedback comes mostly from functional increments confronted with the domain: delivered to the humans who work with them, or to anything else that answers. Observability gives it, because we are not always sure what we are looking for: we are in the complex (Cynefin, Snowden), and all we know is that there will be unexpected side effects. Unknown unknowns.
2. **Activation in production.** New code, a new technical aspect, live in production. It may not change how the software behaves for its users, but it already answers on performance, problems, bugs. Technical monitoring gives it. Known unknowns.
3. **Deployed in production**, on no active path: a dark launch, a partially done feature, a flag still off. It answers whether the thing ships and runs where it will live, before anyone reaches it.
4. **Release.** Not every release is deployed. It answers whether we can package something that should work.
5. **Change on main**, a pull request merged: a hypothesis of integration.
6. **Commit**, one that should work. It answers whether we can cut slices of the product that should work: the release, at the level of a programmer instead of a team.
7. **Change.** Something we believe we can do; the compiler and the tests answer.

Tests are not placed in these loops: we mostly use ATDD, and anchor some kind of testing at nearly every level.

## Fitting the loops

Continuous deployment fits every loop from the second or third down exactly onto the one below: tiny changes, deployed continuously. Continuous delivery does it from the fourth. Agility and story slicing push the first loop closer to the ones below.

## Related

- Every change a hypothesis, and the slice that tests it: [[philosophy/batch-slicing]].
