---
tags: [probe-sense-respond, planning, collaboration]
---

# Rationale: Prototypes Are Probes

Prototypes operationalize probe–sense–respond (@rationale/planning-is-everything.md): when trade-offs resist discussion, code is the cheapest honest evidence. A prototype is built to answer a question, never to become the answer's implementation.

## The loop

Probe–sense–respond maps onto three activities and three artifact lifecycles:

```text
prototype (probe)   → code as evidence, deleted after
study     (sense)   → durable understanding, docs/studies/
plan      (respond) → accepted decisions and stages, docs/plans/
```

The prototype never survives. What survives is what the study compressed (mechanism, ordering constraints, surprises) and what the plan accepted (decisions, stages). Deletion is the guard against the main failure mode: prototype semantics silently hardening into product/API commitments before behavior, ordering, and tests are validated. A plan downstream of a prototype must therefore separate: observations from the prototype, decisions accepted, semantics still under review, implementation stages — public/API exposure only after the behavior is effective.

## Scale-free

Like the workflow rhythm (@rationale/workflow-rhythm.md), the argument mentions no size, so it is fractal:

- Before a plan: a design direction is probed (prototype → study → plan).
- During planning: each alternative that surfaces is probed instead of argued.
- During implementation: a doubt is probed before being coded for real.

Comparison is cheap; opinion is expensive. Whenever discussion stalls on "which would be better", a probe answers with evidence for less than the debate costs.

## In the loop, not beside it

Per @rationale/collaborative-production.md, the prototype is part of the thinking loop — the conversation is the learning, working code a side effect (Brandolini). Probing produces evidence the user senses *with*, not deliverables the user reviews. Two consequences:

- While the user is sense-making on a prototype (flow, scaffolding, with/without shape, decision drivers), inspect — do not edit. Edits shift the evidence under the study.
- When the user offers a sharper abstraction of the mechanism, adopt it (@rationale/attractors.md) — conceptual compression is the probe's actual yield.
