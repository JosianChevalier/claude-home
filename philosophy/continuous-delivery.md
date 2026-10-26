---
tags: [continuous-delivery, small-batches]
---

# Continuous delivery

**Thesis.** The trunk is always releasable (Farley & Humble): every commit can go to production, whether or not it does, and is written as if it deploys the instant it lands. Releasability is not a judgment call; the pipeline defines it.

Every commit is a release candidate: it *can* go to production, whether or not it actually does. Releasability is defined mechanically by the deployment pipeline (build, tests, checks): a commit that passes the pipeline is deployable by definition, one that doesn't never lands on trunk.

This is the invariant behind continuous *deployment* (where every commit additionally *does* deploy): deployment automates the last step, but delivery is the discipline that makes the step safe. Operationally, treat *can* as *will*: write every commit as if it deploys the instant it lands. A broken commit is a broken production, discovered later.

Releasability is a property of the commit, not its location: a branch's commits obey the same discipline as trunk's ([[philosophy/trunk-based-development]]). It is small batches applied to integration: a commit that cannot ship is inventory, its risk coupled to whatever ships next ([[philosophy/batch-size-economics]]).

## The invariant: always working, zero regression

Releasability is the pipeline's word for a stronger norm: at every intermediate step, every commit, every plan stage, the app **works**, causes **zero regression**, and does not deviate from observed production behavior. Not "will work once the next stage lands"; works *now*. This is the conserved quantity of the whole workflow: batch slicing cuts the steps ([[philosophy/batch-slicing]]), change in place keeps each one live ([[philosophy/change-in-place]]), all in service of never leaving the trunk in a state worse than the one before.

A step may add nothing visible (dark code, reshaping), but it may never subtract: no broken flow, no degraded behavior, no "temporary" deviation from the norm. Deviations don't stay temporary; they ship.

## The live path

Releasable does not mean feature-complete. The unit of safety is the **live path**: code reachable from a production entry point (endpoint, scheduler, listener). Code reachable from nowhere cannot break anything: it is dark, deployed but dormant. A stub is fine while dark; code that throws on a live path never ships.

Dark is not idle: driving from the domain, its first consumer is the engineer, and each exposure after that is chosen for the feedback it gives ([[philosophy/domain-first-implementation]]). The thin commit that wires a dark batch to its consumer is the keystone ([[philosophy/change-in-place]]).

Exposure is broader than wiring an endpoint. A **published contract**, API documentation, a frontend contract, naming presented as public, is a promise others build against; publishing it makes the behavior "live" in the social sense even if no code path exists. Vaporware is the contract-level equivalent of a throw on a live path: consumers hit behavior that isn't there. So contracts obey the same keystone order: behavior effective, then verified, then advertised. The one legitimate inversion is deliberate contract-first design, where the contract explicitly carries no implementation claim.

## Related

- Branch commits under the same discipline: [[philosophy/trunk-based-development]].
- Why every commit, not just the last: [[philosophy/batch-size-economics]].
- The keystone as the exception to live at every move: [[philosophy/change-in-place]].
- Exposure chosen for feedback: [[philosophy/domain-first-implementation]].
- Deployed and activated as two loops: [[philosophy/feedback-loops]].
