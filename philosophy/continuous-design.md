---
tags: [continuous-design, ddd, domain-modeling, conceptual-integrity, feedback-loops, small-batches, spec-driven-development, constraints]
---

# Continuous design

**Thesis.** Code does not only express the model, it executes it: it is the most precise specification of the running software, and, while iterating on the design, the best place to watch for the degradation of conceptual integrity.

```
code does not only express the model, it executes it
   │
   ├──▶ it is the spec ──▶ specified from within
   │                       behaviour expressed where the domain
   │                       logic expresses the use case,
   │                       constraint shaped inside
   │                       ✗ waterfall, spec-driven, black-box:
   │                         specified from outside
   │
   └──▶ tension shows there first ──▶ watch the high-level
                                      domain code at every change
                                           │
                                           ▼
                              small batches: the economics of CD
                              agents accelerate the right path
```

## Code executes the model

The code is the design (Reeves). More: it is the specification of the model the software holds, because unlike every other expression of the model (φmodel-expressions) it does not only express it, it executes it. The model the software holds is not always the one the stakeholders hold, programmers included; that gap is the issue, and the watch on the domain code is for it.

The model sits at the heart of the software (Evans), so a system is not specified from its inputs and outputs. What makes it behave right is how it represents the world it works with, the model, and no specification from outside the model states it; to specify behaviour precisely enough to be beyond error is to write code, the best representation of behaviour there is.

Waterfall failed on this, and nobody dug deep enough to see it: its failure was read as feedback arriving too late, and the cure as iterating faster. The fault was ontological, the specification from outside, and iterating faster on it leaves it in place. Spec-driven development holds in schema, from outside, a model the code holds whole; black-box development leaves nobody at the code where the model runs. Both repeat the fault.

## Specified from within

The engineer embedded in the model specifies the application from within the code, not from outside it in a ticket. Tests are code: a good test is the executable specification, more precise than any specification written outside the code and, to the engineer, more readable. The acceptance test is written wherever the domain logic expresses the use case, often the driving port, in one bounded context, so it is a test on the model and part of it; the end-to-end test, the whole deployable service from its entry point, is another thing. Below it, outside-in TDD: each object specified from its own outside by tests at the inner loops (φfeedback-loops).

## Express the behaviour, shape the constraint

Behaviour comes from the design: the model the code holds defines how the world around it works, so it defines how the application behaves. The tests specify the constraints that should drive the model, and they are not enough: on Snowden's constraint pairs (φconstraint-types), they sit opposite the design.

| Snowden's pair | tests, the specification | design |
|---|---|---|
| governing / enabling | governing: rules the behaviour must keep | enabling: lets the software evolve and adapt to the domain |
| external / internal | exoskeleton, set from outside | endoskeleton, structuring from inside |
| containing / connecting | contains: clear boundary conditions | connects the concepts: adaptive, little visibility |

The spec has holes, and the design, executed, fills every one: it drives the behaviour of everything left unspecified, since nothing can be specified whole. Its connections are what the tests do not show: that is why the design is watched in the code. So the behaviour a design happens to give is not to be suffered: the behaviour wanted is expressed first, in the acceptance test, and the constraint that allows it is shaped inside, consciously.

That is the loop of acceptance-test-driven development, make it work, make it right, make it fast (Beck): make it work is passing the test roughly, making it right is the design, making it fast follows. As detail comes, a new test; as features come, the base layers are asked whether they still fit: the model exploration whirlpool (Evans).

## Watch the domain code at every change

Modeling does not stop where coding starts. The model flows into the code and keeps constraining it to the last change; each change is steered by what the code answers, and the answer reshapes the model in turn. That answer is a feedback no other expression gives, definitive and precise, on the conceptual integrity of the model. Ubiquitous language and event storming are built for the same feedback, as early as possible (φubiquitous-language); they carry the model part of the way, and they cannot be redone for every feature. Tension comes from two sides, the domain moving and the model as a whole constraining each part added to it, a second-order constraint (Juarrero), and the code is where it shows first (φmodel-phenomenology).

The later signs are known: the agent touches half the application for one change, any change becomes painful, behaviour degrades. Each is a sign that it is already late, and an agent lowers the cost of handling them, yet that cost stays orders of magnitude above having seen the tension in the code.

What is watched is not every line. The code expresses the model at the appropriate level of abstraction, rid of the accidental complexity of the technical layers, and the high-level domain code is what is watched: where the domain logic expresses the use case, the code that reads as the user story, for how the model behaves and how it represents the world. This is the control we keep over what we produce, held by being embedded in the model, as cognition is (φcollaborative-production). It need not be an IDE: a representation that places the design topologically and shows its snippets as one moves through it is the same watch (φembodied-navigation).

## The same economics as continuous delivery

The rest follows from the model. Once the models are right, software development becomes easy: most technical problems are modeling problems surfacing in the technical layers. Two examples: persistence and concurrency trouble comes from consistency boundaries left undefined (φaggregates); distributed workflows between services come from boundaries drawn wrong around the systems.

Missing the sign, the design overloads and scleroses: it stops letting the software evolve, holds until a change exceeds what it was shaped for, then breaks all at once. In the code, that is bugs sneaking in, then a redesign that risks breaking production. An agent makes a redesign cheaper, and continuous design stays cheaper by orders of magnitude; the question is the one continuous delivery asks: accept the bugs and the rework, or reduce them. Small batches are what keeps the risk low (φbatch-size-economics, φchange-in-place), and too much specification loses the flow.

The cost of a design left unwatched shows only with the accumulation of features and insight, and it has gone unnoticed mostly in organisations large and inefficient enough to tolerate waste: in lean terms, muda nobody sees. There, code is rewritten rather than redesigned. Code is meant to be redesigned often, not to live long; thrown away whole and remade from zero, it sediments no learning, neither in the head nor in the code.

## Agents accelerate the right path

None of this is specific to agentic development. Agents have eased the pain, which makes it less noticeable, and they accelerate the right path faster than the wrong one, for two reasons. A good design prevents waste in context, so an agent works better on it (φcontext-economics). And the fundamentals of flow have not changed, batch size economics and the DORA metrics: an agent's speed pays when it shortens the flow of small batches, not when it ships bigger ones (φbatch-size-economics, φagentic-extreme-programming). Agents make building fast, but the cost of a bad design was never in building it; it is in its consequences. Think good architecture is expensive? Try bad architecture (Foote & Yoder).

## Related

- The model exists only as expressed, and what each expression keeps: φmodel-expressions.
- Model tension, felt in the code before it is diagnosed: φmodel-phenomenology.
- The language the code keeps: φubiquitous-language.
- Why the spectator builds no model: φcollaborative-production.
- Thinking with the code by moving through it: φembodied-navigation.
- The consistency boundary: φaggregates.
- Snowden's types of constraints, tests and design on opposite sides: φconstraint-types.
- Small batches, and the change made where it stands: φbatch-size-economics, φchange-in-place.
- Waste in context, and the practices that hold each other up: φcontext-economics, φagentic-extreme-programming.
