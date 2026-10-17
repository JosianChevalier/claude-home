---
tags: [ddd, domain-modeling, invariants, tactical-ddd, types]
---

# Always-valid domain model

**Thesis.** The domain model holds its invariants at every moment domain code can see it. Enforced by structure first, the invalid state unrepresentable; by code at minimum, the operations refusing it.

## The property and its observer

The observer is any code in the domain that holds the model. Its invariants hold after each operation, in memory, before any save. Only the inside of one operation is unobserved.

Nothing outside the model enforces anything: not a validator called before use, not the database, not the adapter. A model valid only after someone validated it is not always valid; it is valid at the places someone remembered.

## Two ways to enforce

| | By structure | By code |
|---|---|---|
| Check runs | once, at construction | at every operation |
| Proof lives in | the type | nowhere; re-established each time |
| Caller must | nothing | trust, or re-check |

By structure is [[philosophy/parse-dont-validate]] applied to the domain: the model is parsed into, once, and the invalid state has no representation. By code is the operations refusing: a `require` in a method, a guard in a transition. Both keep the property; only the first keeps the proof.

Structure first, because the proof is what the rest of the code reads. A property held by code is a property to be aware of at every call site; a property held by structure is in the shape. Code is the floor, for what the grammar cannot state.

## Symptoms

Each is a parse missing, and names the type that is missing. If a structure can represent a state, code will produce it.

- **A nullable beside a status.** `shippedAt` null unless shipped, with a check that the two agree. One type per state: `Placed`, `Shipped(shippedAt)`.
- **Flags.** `pending`, `solved`, `closed` as three booleans: eight combinations, three valid. A sum type.
- **Parallel collections.** Products and quantities aligned by index. One line type.
- **Unpacking.** A value object opened to pass its primitive to a collaborator. The collaborator's signature is wrong; it predates the type.
- **A setter.** Any state reachable from outside. Transitions are methods returning the next state's type; what is not a method is not a transition.

## Transitions as types

Typestate (Strom & Yemini): the lifecycle state in the type, so an operation exists only on the states where it is legal. `cancel()` is not guarded on `Shipped`; it is absent, and the illegal transition is a compile error. Consumers demand the only state they can handle, `ship(order: Paid)`, and the defensive checks downstream go.

Immutability is load-bearing. A transition returns a fresh value of the next type; mutating in place would let the runtime state diverge from the static type, and the type would lie.

## Nominal where the language is structural

In a structurally typed language every `string` is every other `string`, so an `OrderId` passed where a `SiteId` is expected is invisible to the checker: primitive obsession has no symptom. Nominal-ness is manufactured: a class for a value with behaviour, a brand and a factory for an id. The contract is what matters, construction through one door and the plain primitive rejected; the mechanism is each project's.

## Related

- The pattern this is the domain instance of: [[philosophy/parse-dont-validate]].
- The boundary the invariants derive, and saving whole: [[philosophy/aggregates]].
- A grammar that cannot state the invariant: [[philosophy/model-expressions]].
