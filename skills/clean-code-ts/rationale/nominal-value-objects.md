---
tags: [typescript, type-safety, domain-modeling, always-valid-domain]
---

# Rationale: Nominal Types for Value Objects

TypeScript is **structurally** typed: two types are interchangeable whenever their shapes match, so every `string` is every other `string`. Domain languages are **nominal**: an `OrderId` is not a `CustomerId` even when both are strings underneath. Primitive obsession is therefore *invisible* to the structural checker — nominal-ness has to be manufactured deliberately. (Java people get this for free from nominal typing; that's why the Java skill never needed the section.)

Two levels of investment, priced by behavior:

- **Rich behavior** (arithmetic, comparison, formatting) → class wrapper. The class is nominal by construction *and* gives the operations a home (`Euros.add/times/deduct`) — same move as first-class collections.
- **Id-like primitives** → branded type + factory. All they need is identity; a brand is the minimal purchase.

## Why the skill stays silent on the branding mechanism

Branding mechanisms (compile-time-only cast, runtime symbol tagging, wrapper objects…) trade off differently on runtime cost, serialization transparency, equality semantics, and lint conventions — and each project weighs those differently. A skill that prescribes one mechanism exports one project's trade-off to every project. The invariant worth prescribing is the **contract**, not the mechanism: construction goes through a factory, and a plain primitive is rejected by the checker wherever the branded type is demanded. Follow the project's existing branding utility.
