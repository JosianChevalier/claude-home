---
tags: [continuous-design, ddd, domain-modeling, conceptual-integrity, feedback-loops, small-batches, spec-driven-development]
---

# Continuous design

**Thesis.** Code does not only express the model, it executes it: it is the model's specification, written from within. It is also where tension shows first, so the design stays right by watching the high-level domain code at every change.

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

The code is the design (Reeves). More: it is the specification of the model the software holds, because unlike every other expression of the model ([[philosophy/model-expressions]]) it does not only express it, it executes it. The model the software holds is not always the one the stakeholders hold, programmers included; that gap is the issue, and the watch on the domain code is for it.

The model sits at the heart of the software (Evans), so a system is not specified from its inputs and outputs. What makes it behave right is how it represents the world it works with, the model, and no specification from outside the model states it; to specify behaviour precisely enough to be beyond error is to write code, the best representation of behaviour there is.

Waterfall failed on this, and nobody dug deep enough to see it: its failure was read as feedback arriving too late, and the cure as iterating faster. The fault was ontological, the specification from outside, and iterating faster on it leaves it in place. Spec-driven development holds in schema, from outside, a model the code holds whole; black-box development leaves nobody at the code where the model runs. Both repeat the fault.

## Specified from within

The engineer embedded in the model specifies the application from within the code, not from outside it in a ticket. Tests are code: a good test is the executable specification, more precise than Gherkin and more readable. The acceptance test is written wherever the domain logic expresses the use case, often the driving port, in one bounded context, so it is a test on the model and part of it; the end-to-end test, the whole deployable service from its entry point, is another thing. Below it, each object is specified from its own outside by tests at lower loops.

## Express the behaviour, shape the constraint

Behaviour comes from the design: the model the code holds defines how the world around it works, so it defines how the application behaves. The model is an enabling constraint on behaviour (Snowden): a structure, a core, and what every specification shapes whether or not the writer knows it. Not knowing it is how the results come out wrong. So the behaviour a design happens to give is not to be suffered: the behaviour wanted is expressed first, at the port, and the constraint that allows it is shaped inside, consciously.

That is the loop of acceptance-test-driven development, make it work, make it right, make it fast (Beck): the test roughly fit is the first step, making it right is the design, making it fast follows. As detail comes, a new test; as features come, the base layers are asked whether they still fit: the model exploration whirlpool (Evans).

## Watch the domain code at every change

Modeling does not stop where coding starts. The model flows into the code and keeps constraining it to the last change; each change is steered by what the code answers, and the answer reshapes the model in turn. That answer is a feedback no other expression gives, definitive and precise, on the conceptual integrity of the model. Ubiquitous language and event storming are built for the same feedback, as early as possible ([[philosophy/ubiquitous-language]]); they carry the model part of the way, and they cannot be redone for every feature. Tension comes from two sides, the domain moving and the model as a whole constraining each part added to it, a second-order constraint (Juarrero), and the code is where it shows first ([[philosophy/model-phenomenology]]).

The later signs are known: the agent touches half the application for one change, any change becomes painful, behaviour degrades. Each is a sign that it is already late, and the agent lowering the cost of handling it leaves the cost orders of magnitude above having seen it in the code.

What is watched is not every line. The code expresses the model at the appropriate level of abstraction, rid of the accidental complexity of the technical layers, and the high-level domain code is what is watched: the domain service behind the driving port, the code that reads as the user story, for how the model behaves and how it represents the world. This is the control we keep over what we produce, held by being embedded in the model, as cognition is ([[philosophy/collaborative-production]]). It need not be an IDE: a representation that places the design topologically and shows its snippets as one moves through it is the same watch ([[philosophy/embodied-navigation]]).

## The same economics as continuous delivery

The rest follows from the model. Once the models are right, software development becomes easy: most technical problems are modeling problems surfacing in the technical layers. Two examples: persistence and concurrency trouble comes from consistency boundaries left undefined ([[philosophy/aggregates]]); distributed workflows between services come from boundaries drawn wrong around the systems.

Missing the sign means bugs sneaking in, then a redesign that risks breaking production. An agent makes a redesign cheaper, and continuous design cheaper still, by orders of magnitude; the question is the one continuous delivery asks: accept the bugs and the rework, or reduce them. Small batches are what keeps the risk low ([[philosophy/batch-size-economics]], [[philosophy/change-in-place]]), and too much specification loses the flow. Agents shorten the mean time to recovery; the floor is further down.

The problem shows only with the accumulation of features and insight, and it has gone unnoticed mostly in organisations large and inefficient enough to tolerate waste: in lean terms, muda nobody sees. There, code is rewritten rather than redesigned. Code is meant to be redesigned often, not to live long; thrown away whole and remade from zero, it sediments no learning, neither in the head nor in the code.

## Agents accelerate the right path

None of this is new to agentic development. Agents have eased the pain, which makes it less noticeable, and they accelerate the right path faster than the wrong one, for two reasons. A good design prevents waste in context, so an agent works better on it ([[philosophy/context-economics]]). And the fundamentals of flow have not changed, batch size economics and the DORA metrics: an agent's speed accelerates the flow, it is not spent shipping bigger batches ([[philosophy/batch-size-economics]], [[philosophy/agentic-extreme-programming]]). The problem with bad design was never that it is fast to build; it is the consequences. Think good architecture is expensive? Try bad architecture (Foote & Yoder).

## Related

- The model exists only as expressed, and what each expression keeps: [[philosophy/model-expressions]].
- Model tension, felt in the code before it is diagnosed: [[philosophy/model-phenomenology]].
- The language the code keeps: [[philosophy/ubiquitous-language]].
- Why the spectator builds no model: [[philosophy/collaborative-production]].
- Thinking with the code by moving through it: [[philosophy/embodied-navigation]].
- The consistency boundary: [[philosophy/aggregates]].
- Small batches, and the change made where it stands: [[philosophy/batch-size-economics]], [[philosophy/change-in-place]].
- Waste in context, and the practices that hold each other up: [[philosophy/context-economics]], [[philosophy/agentic-extreme-programming]].
