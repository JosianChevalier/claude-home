---
tags: [continuous-delivery, small-batches]
---

# Rationale: Continuous Delivery

Governing frame: Farley & Humble's *Continuous Delivery* — the trunk is **always releasable**. Every commit is a release candidate: it *can* go to production, whether or not it actually does. Releasability is not a judgment call; it is defined mechanically by the deployment pipeline (build, tests, checks) — a commit that passes the pipeline is deployable by definition, one that doesn't never lands on trunk.

This is the invariant behind continuous *deployment* (where every commit additionally *does* deploy): deployment automates the last step, but delivery is the discipline that makes the step safe. Operationally, treat *can* as *will*: write every commit as if it deploys the instant it lands. A broken commit is a broken production, discovered later.

Releasability is a property of the **commit, not its location**. A branch commit obeys the exact same discipline as a trunk commit — a branch is only a short queue of release candidates awaiting fast-forward, never a hygiene exemption. "It's just a branch, I'll clean up before merging" recreates the big batch: it defers integration risk to the merge and makes the merge a laundering step. When every branch commit is independently releasable, branches carry no risk trunk doesn't — which is precisely what makes trunk-based development possible: the branch shrinks to a conflict-avoidance queue and can shrink further to nothing. Branch discipline *is* the demonstration that TBD is safe.

## The invariant: always working, zero regression

Releasability is the pipeline's word for a stronger norm: at every intermediate step — every commit, every plan stage — the app **works**, causes **zero regression**, and does not deviate from observed production behavior. Not "will work once the next stage lands"; works *now*. This is the conserved quantity of the whole workflow: small batches shrink the steps, the keystone orders them, safe-rollout guards the live ones — all in service of never leaving the trunk in a state worse than the one before.

A step may add nothing visible (dark code, reshaping), but it may never subtract: no broken flow, no degraded behavior, no "temporary" deviation from the norm. Deviations don't stay temporary — they ship.

## Working ≠ exposed

Releasable does not mean feature-complete. The unit of safety is the **live path**: code reachable from a production entry point (endpoint, scheduler, listener). Code that is not reachable cannot break anything — it is dark, deployed but dormant.

This yields the build order for new behavior: **domain first, expose last**.

1. Build the domain model, services, adapters — fully tested, entirely unreachable. Every commit releasable because nothing triggers the new code.
2. The final commit wires the entry point — the **keystone** (Fowler's *Keystone Interface*): a small, trivial commit that turns dark code live.

Exposure is broader than wiring an endpoint. A **published contract** — API documentation, a frontend contract, naming presented as public — is a promise others build against; publishing it makes the behavior "live" in the social sense even if no code path exists. Vaporware is the contract-level equivalent of a throw on a live path: consumers hit behavior that isn't there. So contracts obey the same keystone order — behavior effective, then verified, then advertised. The one legitimate inversion is deliberate contract-first design, where the contract explicitly carries no implementation claim.

The keystone inverts where risk sits. All the hard work ships early, in small safe commits; the risky moment — going live — is reduced to the thinnest possible change, easy to review and to revert.

## Dark is operationally free, not economically free

Dark code cannot break production. It is still design-in-process inventory ([[philosophy/batch-size-economics]]): unvalidated, depreciating, and paying its integration risk in one lump at the keystone. The keystone order is therefore for **new** behavior with no existing live path, and even there the dark phase is kept as short as the thinnest keystone allows.

Modifying an *existing* live path is a different regime. The code is already exposed, so the change is done **in place** — a chain of mechanical, behavior-preserving moves on the live path, each live as it lands ([[philosophy/change-in-place]], @rationale/mechanical-refactoring.md). Alternative flows (no-op adapters, safe defaults, flags, expand-contract — the safe-rollout strategies) cover only the smallest atom that cannot be transformed in place, and that atom is adopted in the same stage. Building a dark replacement of a live workflow and switching at the end is not the keystone pattern: it is the big batch, with the switch as its big-bang integration.

Same invariant, two regimes: new behavior goes dark-then-keystone, existing behavior is transformed in place.

## Why every commit, not just the last

Releasability per commit is small batches applied to integration ([[philosophy/batch-size-economics]]). A commit that cannot ship is design-in-process inventory: it blocks trunk, defers feedback, and couples its risk to whatever ships next. Keeping each commit releasable keeps batch size at its floor — each one an independently revertible bet, integration risk paid continuously in cents instead of at release time in full.

## Consequences

- Never ship code that throws on a live path — no `UnsupportedOperationException`, no `TODO` that blows up at runtime. Stubs are fine only while dark.
- Branch commits get no exemption: same tests, same releasability, same keystone order as trunk. No "fix before merge" commits.
- Producers before consumers; remove old code only after new code is proven.
- Ordering is part of design: a plan whose intermediate states are unreleasable is sliced wrong.
- Plans end with the keystone: exposure and contract documentation are late stages, after behavior is effective and verified; legacy removal comes last, after the new path is proven.
- Replacing existing live behavior is refactoring, not a keystone: change in place, alternative flows at the smallest atom only, adopted in the same stage.
- Nothing is built before its consumer: a stage introduces only what is on the live path by the end of that stage or the next.
