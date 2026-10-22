---
tags: [continuous-design, ddd, domain-modeling, conceptual-integrity, feedback-loops, small-batches]
---

# Continuous design

**Thesis.** The code is the first expression of the model where tension shows, and the design stays right only by watching it at every change. This presupposes that no specification from outside says what a system does: only an expression of the model does, and code is the most precise one. Hence no spec-driven development, no black box.

## Two ways

The two claims go together as the first and second way of DevOps (Kim) do. The first, that only the model expressed says what the system does, is flow: it gets the system right the first time. The second, that the code is where tension shows first, is feedback: it keeps the design right over time, through the monitoring and the redesigns. The second is the core; it cannot be stated without the first.

## No specification from outside

Waterfall is read as slow iteration: the specification arrived late and no longer matched what the users wanted. That reading misses the ontological fault. A system cannot be specified from its inputs and outputs: that is the core of domain-driven design (Evans). What makes it behave right is how it represents the world it works with, and that is the model, which exists only as expressed ([[philosophy/model-expressions]]). The UX is one expression, the code another, and nothing from outside them states what they state.

To specify behaviour precisely enough to be beyond error is to write code: code is so far the best representation of behaviour, and behaviour is what a specification is for. The risk of spec-driven development is to hold a high-level model in schema that code holds better. Nobody specifies a system better than its code does; that is why there is no black box development.

## The feedback only code gives

The realization in code gives a feedback no other expression gives: definitive and precise, on the conceptual integrity of the model. Ubiquitous language and event storming are built for the same feedback, as early as possible ([[philosophy/ubiquitous-language]]); they carry the model part of the way, and they cannot be redone for every feature. As the application evolves, the code is what shows the tensions, and shows them first ([[philosophy/model-phenomenology]]).

The later signs are known: the agent touches half the application for one change, any change becomes painful, behaviour degrades. Each is a sign that it is already late, and the agent lowering the cost of handling it leaves the cost orders of magnitude above having seen it in the code.

## What is watched

Not every line. The code expresses the model at the appropriate level of abstraction, rid of the accidental complexity of the technical layers, and the high-level domain code is what is watched: how the model behaves, how it represents the world. This is the control we keep over what we produce, and it is held by being embedded in the model, as cognition is ([[philosophy/collaborative-production]]). Code need not be read in an IDE for that: a representation that places the design topologically and shows its snippets as one moves through it is the same watch ([[philosophy/embodied-navigation]]).

The rest follows from the model. Once the models are right, software development becomes easy: most persistence problems, deadlocks included, come from aggregates left undefined, and fade once the consistency boundary is right ([[philosophy/aggregates]]); most distributed workflows between services come from boundaries drawn wrong around the systems.

## The same economics as continuous delivery

Missing the sign means bugs sneaking in, then a redesign that risks breaking production. An agent makes a redesign cheaper, and continuous design cheaper still, by orders of magnitude; the question is the one continuous delivery asks: accept the bugs and the rework, or reduce them. Small batches are what keeps the risk low ([[philosophy/batch-size-economics]], [[philosophy/change-in-place]]). Agents shorten the mean time to recovery; the floor is further down.

## Why it went unnoticed

The problem shows only with the accumulation of features and insight; it has gone unnoticed mostly where there was money to rewrite. Code is meant to be redesigned often, not to live long. Thrown away whole and remade from zero, it sediments no learning, neither in the head nor in the code.

None of this is new to agentic development. Agents have eased the pain, which makes it less noticeable; and they accelerate the right path faster than the wrong one.

## Related

- The model exists only as expressed, and what each expression keeps: [[philosophy/model-expressions]].
- Model tension, felt in the code before it is diagnosed: [[philosophy/model-phenomenology]].
- The language the code keeps: [[philosophy/ubiquitous-language]].
- Why the spectator builds no model: [[philosophy/collaborative-production]].
- Thinking with the code by moving through it: [[philosophy/embodied-navigation]].
- The consistency boundary: [[philosophy/aggregates]].
- Small batches, and the change made where it stands: [[philosophy/batch-size-economics]], [[philosophy/change-in-place]].
