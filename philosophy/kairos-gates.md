---
tags: [collaboration, harness-design, workflow, domain-modeling]
---

# Kairos gates

**Thesis.** Where kairos recurs, build a step so the moment is seized by design, not by luck.

The core of the agentic loop is how the work that must be done gets done. The kairos that matters most arrives inside it, through the belt, and is seized by metis or missed ([[philosophy/metis-kairos]]). The loop is a built process, codified in sessions and workflows, so steps can be added on top of it. A gate is such a step: the practice or the model is reflected on before the belt moves again.

```
request ──▶ plan ──▶ change ──▶ change ──▶ ship ──▶ end of session
   │                    │                    │            │
 gate                 gate                 gate         gate
 rival reading        model tensions       security     kaizen
```

## What a gate injects, by example

- **A reminder.** Kaizen as a step at the end of a session, not an intention ([[philosophy/kaizen]]).
- **A chore.** The checks the work would skip: updating documentation, running the audit.
- **Expertise.** A practice, at the moment it applies. Below.

## Expertise

A practice enters the team's loop as a step, at the moment it applies. Examples, not a list:

- after each domain-model change, an agent carrying DDD inspects the model for tensions and raises an alert
- before a change ships, a security review
- before a feature is planned, a product challenge, or a grill of the plan
- before the work starts, the metrics it will move and the hypothesis it tests, written down

Any practice fits the pattern: name its moment, build the step. This is how a new practice or a new habit takes hold: not taught once, met every time its moment comes. The same step shows when the question exceeds what the loop can answer, and expertise must be escalated.

### Where it is legitimate

The agent holds sedimented culture, not a situated type ([[philosophy/model-phenomenology]]). That familiarity is illegitimate as adjudication and legitimate as *supply*. Gopnik's finding on ambiguous figures: reversal is impossible until someone hands you the alternative representation; informed versus uninformed is the variable, not intelligence. A gate that asks whether an Order in this codebase is also a revenue event elsewhere is the library making a flip available. The resolution is the engineer's.

### The first gate

The request itself. Calibration, the first response before anything is built, is where a rival reading of what was asked goes on the table: the cheapest moment for a flip, since nothing has been predicated yet. The first-turn stop in the planning and study skills is this gate, named.

## Gates and transparency

Kairos is seized two ways:

- through a gate, for the known unknowns: the moment is known to recur, so a step is built at its place
- through transparency, for the unknown unknowns: the belt shows the work and the engineer catches, by metis, the moment nobody planned for ([[philosophy/transmission-belt]])

Neither replaces the other.

## Related

- Kairos seized unplanned, through the belt: [[philosophy/metis-kairos]].
- The base layer a gate sits on: [[philosophy/transmission-belt]].
- The reminder gate: [[philosophy/kaizen]].
- Why the agent supplies and never adjudicates: [[philosophy/model-phenomenology]].
