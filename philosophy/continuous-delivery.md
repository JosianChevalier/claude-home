---
tags: [continuous-delivery, small-batches]
---

# Continuous delivery

**Thesis.** Every commit, on trunk or a branch, at every stage of a plan, is deliverable: it works now, zero regression. Continuous delivery (Humble & Farley), the live path as its unit of safety.

Continuous delivery as Humble & Farley wrote it (the 2010 book, Accelerate's measures with Forsgren): releasability is a property of the commit, proven by the deployment pipeline. Continuous deployment only automates the last step; the discipline is the same, so *can* is read as *will*: a commit is written as if it deploys the instant it lands.

A branch's commits obey the same discipline as trunk's ([[philosophy/trunk-based-development]]). Releasability is small batches applied to integration: a commit that cannot ship is inventory, its risk coupled to whatever ships next ([[philosophy/batch-size-economics]]).

## The invariant: always working, zero regression

Works now: not "will work once the next stage lands". Zero regression: no deviation from observed production behavior. This is the conserved quantity of the whole workflow: batch slicing cuts the steps ([[philosophy/batch-slicing]]), change in place keeps each one live ([[philosophy/change-in-place]]), all in service of never leaving a commit in a state worse than the one before.

A step may add nothing visible (dark code, reshaping), but it may never subtract: no broken flow, no degraded behavior, no "temporary" deviation from the norm. Deviations don't stay temporary; they ship.

## The live path

Releasable does not mean feature-complete. The unit of safety is the **live path**: code reachable from a production entry point (endpoint, scheduler, listener). Code reachable from nowhere cannot break anything: it is dark, deployed but dormant. A stub is fine while dark; code that throws on a live path never ships.

Dark is not idle: driving from the domain, its first consumer is the engineer, and each exposure after that is chosen for the feedback it gives ([[philosophy/domain-first-implementation]]). The thin commit that wires a dark batch to its consumer is the keystone ([[philosophy/change-in-place]]).

Exposure is broader than wiring an endpoint. A **published interface** (Fowler), API documentation, a frontend contract, naming presented as public, is live in the social sense even if no code path exists. Vaporware is the interface-level equivalent of a throw on a live path: consumers hit behavior that isn't there. So a published interface obeys the same keystone order: behavior effective, then verified, then advertised. The one legitimate inversion is deliberate contract-first design, where the contract explicitly carries no implementation claim.

## Related

- Branch commits under the same discipline: [[philosophy/trunk-based-development]].
- Why every commit, not just the last: [[philosophy/batch-size-economics]].
- The keystone as the exception to live at every move: [[philosophy/change-in-place]].
- Exposure chosen for feedback: [[philosophy/domain-first-implementation]].
- Deployed and activated as two loops: [[philosophy/feedback-loops]].
