---
tags: [harness-design, kaizen, variety-absorption]
---

# The three-layer harness

**Thesis.** Know-how, doctrine, philosophy. The know-how codifies what worked, the head of a Pareto distribution; the doctrine is the boundary the agent improvises within, and it holds in the fat tail; the philosophy is where we want to go, on a lifecycle of its own. A bump never changes the destination.

| Layer | Answers | Lives in | Loaded | Questioned |
|---|---|---|---|---|
| **3. Philosophy** | why: the philosophy of software development and of working with agents | `philosophy/` | harness improvement | at kaizen, by reasons and falsification |
| **2. Doctrine** | what must always be true: the intent | `## Doctrine` in rules and skills; `CLAUDE.md` | execution | at kaizen only |
| **1. Know-how** | what worked: the head of the distribution | the body of rules and skills, after the doctrine | execution | during execution |

The three are one rung-set of the abstraction ladder; read it first ([[philosophy/abstraction-ladder]]). What follows is what is specific to these rungs.

Doctrine is fixed during execution, and it is the test for leaving the know-how: the agent departs from a step because the doctrine still holds. Snowden says the same of rules: they do not create order, they codify what worked, and what worked is Pareto-distributed: a head of usual cases, a fat tail of exceptions where one improvises within principles. Lakatos's research programmes have the same structure: a hard core never targeted from inside, and a protective belt that absorbs the anomalies.

```
 philosophy    navigation    where we want to go
     │  ▲
     │  │  consequence down, feedback up
     ▼  │
 doctrine      steering      what must stay true
     │  ▲
     ▼  │
 know-how      suspension    where the bumps arrive
```

## Why the layers

Two seams. Between the philosophy and the two below, inertia: the lifecycles differ. Between the doctrine and the know-how, commodification: the head of the distribution codified out of the rule that holds in the tail too. Design rationale in the Rittel/Kunz (IBIS) lineage, the insight behind ADRs: a decision and its argumentation have different readers and different lifecycles. The lifecycle difference is inertia ([[philosophy/change-inertia]]).

**Layer 1, know-how: low inertia.** It moves fast: each session that goes wrong feeds it, each model change reshapes it. Tuning it is Cynefin's complex domain: probe, sense, respond; act, watch the agent, adjust, again.

It is the least portable layer, coupled to the project and the team. Its role is the bottom rung's: absorb variation where it happens.

**Layer 2, doctrine: the know-how's lifecycle, a wider coverage.** The know-how is the head of the distribution, commodified into steps; the doctrine is the blanket rule that holds in the fat tail, where the steps stop applying. It is updated when a failure goes beyond what the know-how could absorb, and that happens.

It changes less often because it covers more, and a change to it is a behavior adjustment, not a fine-tune. Within a session it does not move at all: questioned at kaizen, never during execution.

**Layer 3, philosophy: a different lifecycle altogether.** It changes less often because we do not change where we want to go every time. Updating it updates our understanding of the activity itself: Boyd's orient, destroying a world and building another. Our own mental models change, not only the agent's instructions.

It also has uses beyond the harness: a reflection base, notes, material to produce content from.

## Two directions

Upward, as feedback: the know-how absorbs the variation; whatever survives the absorption is what reaches the philosophy. Downward, as consequence: a change in a layer trickles down into every layer below it. Pace layering (Brand) holds here as on every rung of the ladder.

Our own metaphor for the three: the know-how is the shock absorber, the doctrine the steering, the philosophy the navigation. A bump never changes the destination; a new destination changes the steering and what the suspension meets.

## Related

- How a rule or skill is shaped from layers 1 and 2: [[philosophy/harness-shape]].
- How feedback moves between the layers: [[philosophy/kaizen]].
- The shape the layers share with the process tree and the belt: [[philosophy/abstraction-ladder]].
- What each harness element is for: [[philosophy/harness-elements]].
