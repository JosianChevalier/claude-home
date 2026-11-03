---
tags: [ddd, conceptual-integrity, sociotechnical, variety-absorption, probe-sense-respond]
---

# Compensations in software

**Thesis.** An organisation that builds software grows its compensation system (φsystems-of-compensations) around a model it did not split: the design tension is worked around by process, the process has side effects, and the organisation anchors both.

```
concerns added          premature split
without splitting       of the organisation
      │                        │
      ▼                        ▼
intrinsic coupling ──▶ extrinsic coupling
      │                        │
      └──▶ fragility ──▶ rigidity ──▶ Big Ball of Mud
                                        │
            ┌───────────────────────────┘
            ▼
   process compensations ──▶ unexpected side effects ──▶ more process
            │                                                   │
            └──────── fragmentation of the organisation ◀───────┘
```

## The loop

Two entrances. Concerns added to one model without splitting it, DRY and refactoring doing the adding: the model serves heterogeneous responsibilities and loses conceptual integrity, the spork (φmodel-phenomenology). A premature split of services or teams: coupled systems collaborating on one responsibility become fragments of one model spread across all of them. Both degrade through constraint relaxation, logic leaks and synchronised evolutions into fragility, then rigidity, change avoided because risky, then the Big Ball of Mud (Foote & Yoder).

The mud is worked around rather than resolved: added testers and environments, dependencies managed instead of fixed, synchronised releases compensated with feature flags, review processes in place of trunk-based development. Each is process on a design problem; each has side effects that call for more process, and the loop fragments the organisation again.

## Mechanisms here

- **Conway's law** is the anchoring: the organisation canalises the design tension into teams, roles and contracts, and the structure then holds the workflow as such.
- **Variety climbs.** What the model could not absorb is absorbed by process, then by roles, then by frameworks: the abstraction ladder read upward (φabstraction-ladder), each rung dearer per unit of variety. The cost is not the climb, it is the dissipation: the stack is sand (φsystems-of-compensations).

## One approach

Model tension is the sense of a probe-sense-respond stance (φmodel-phenomenology): felt before diagnosed, a signal read as a symptom, never as the cause. Not acting on it lets it crystallise: the tension becomes sediment (Husserl, φsystems-of-compensations), an unknown known the organisation builds on without seeing; and the loop distributes the cause across business, architecture, process and organisation, so the signal is what is tracked, not the origin. Build a body of evidence of misalignments; respond by splitting the model (φmodel-expressions) while the layers are few. Where the layers are recoverable by systematic perturbation, the Mikado method; where they interact and only show dynamically, safe-to-fail probes.

## Related

- The law this instantiates: φsystems-of-compensations.
- Model tension, the spork: φmodel-phenomenology.
- The ladder variety climbs: φabstraction-ladder.
- The design watched in the code at every change: φcontinuous-design.
