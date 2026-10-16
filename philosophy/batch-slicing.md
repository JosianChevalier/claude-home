---
tags: [batch-slicing, elephant-carpaccio, small-batches, planning]
---

# Batch slicing

**Thesis.** Batch slicing is finding the next hypothesis to validate, and cutting the smallest slice that can test it. First the hypotheses of value, about the domain and the user: functional increments that only production can verify. Under them, technical hypotheses.

## Hypotheses of value

A user story is a bet that users want it. Only production settles the bet. So the cut looks for the next hypothesis, and for the thinnest increment that reaches production to test it. Each piece is used as soon as it lands. Elephant carpaccio (Cockburn) names this level.

The usual bad cuts:

- **All of CRUD when only read is used.** Create, update and delete get built before read has shown anyone wants the data.
- **A whole layer before moving up.** Nothing is tested until the top layer lands.

## Technical hypotheses

Under each increment of value, a technical level. A change can cross many layers; one step for all of them is the big batch again, one level down. So the increment splits into technical slices, each ending green and deployed. Their bet is narrower: the app still works. They bank no value.

The increment of value owns the plan; technical slices serve it. Layer steps with no increment above them are the bad cut "a whole layer before moving up".

A reshape is a technical slice.

## Slicing deeper

A slice that seems too big to cut further often hides a redesign: cross the valley in steps ([[philosophy/make-the-change-easy]]). The intermediate models are more or less coherent; the point is getting from one hill to the next.

## The step

A step is one slice, at either level. A north star defines it and guides it across the tiny sub-agents below. The step is the human's unit of thought.

## Related

- Why small: [[philosophy/batch-size-economics]].
- Crossing the valley: [[philosophy/make-the-change-easy]].
- The floor below the step: [[philosophy/atomic-commit]].
