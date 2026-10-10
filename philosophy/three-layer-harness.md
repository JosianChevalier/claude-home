---
tags: [harness-design, kaizen]
---

# Rationale: The Three-Layer Harness

| Layer | Answers | Lives in | Loaded | Questioned |
|---|---|---|---|---|
| **1. Know-how** | what works in the usual case | the body of rules and skills, after the doctrine | execution | during execution |
| **2. Doctrine** | what must always be true: the intent | `## Doctrine` in rules and skills; `CLAUDE.md` | execution | at kaizen only |
| **3. Philosophy** | why: the philosophy of software development and of working with agents | `philosophy/` | harness improvement | at kaizen, by reasons and falsification |

Doctrine is fixed during execution, and it is the test for leaving the know-how: the agent departs from a step because the doctrine still holds. Lakatos's research programmes have the same structure: a hard core never targeted from inside, and a protective belt that absorbs the anomalies.

## Why the layers: inertia

The layers have different lifecycles, and that is why they stay apart: design rationale in the Rittel/Kunz (IBIS) lineage, the insight behind ADRs, a decision and its argumentation have different readers and different lifecycles. The lifecycle difference is inertia.

- **Layer 1, know-how: low inertia.** It moves fast. Each session that goes wrong feeds it; each model change reshapes it. This is the Cynefin complex domain, near the edge of chaos: act, watch the agent, adjust, again. It is the least portable layer, coupled to the project and the team. Its role is to absorb variation where it happens: in Cynefin, complexity is absorbed at the closest place to where it arises.
- **Layer 2, doctrine: coupled to layer 1.** The two have similar inertia. The doctrine is updated when a failure goes beyond what the know-how could absorb, and that happens: a bump taken in layer 1 can reorient the steering quite easily. It covers all cases where the know-how covers the usual four in five, so it changes less often, and a change to it is a behavior adjustment, not a fine-tune.
- **Layer 3, philosophy: a different lifecycle altogether.** It changes less often because we do not change where we want to go every time. Updating it updates our understanding of the activity itself: Boyd's orient, destroying a world and building another. Our own mental models change, not only the agent's instructions. It also has uses beyond the harness: a reflection base, notes, material to produce content from.

Change runs in two directions. Upward, as feedback: the know-how absorbs the variation; whatever survives the absorption is what reaches the philosophy. Downward, as consequence: a change in a layer trickles down into every layer below it.

The layers are one rung-set of the abstraction ladder ([[philosophy/abstraction-ladder]]), with pace layering (Brand) as the foundation: fast layers propose, slow layers dispose; the slow constrain the fast, the fast keep the slow alive; change shears between layers. Our own metaphor for the three: the know-how is the shock absorber, the doctrine the steering, the philosophy the navigation. A bump never changes the destination; a new destination changes the steering and what the suspension meets.

## Related

- How a rule or skill is shaped from layers 1 and 2: [[philosophy/harness-shape]].
- How feedback moves between the layers: [[philosophy/kaizen]].
- The shape the layers share with the process tree and the belt: [[philosophy/abstraction-ladder]].
- What each harness element is for: [[philosophy/harness-elements]].
