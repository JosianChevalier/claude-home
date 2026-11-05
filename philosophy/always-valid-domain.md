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

By structure is φparse-dont-validate applied to the domain: the model is parsed into, once, and the invalid state has no representation. By code is the operations refusing: a `require` in a method, a guard in a transition. Both keep the property; only the first keeps the proof.

Structure first, because the proof is what the rest of the code reads. A property held by code is a property to be aware of at every call site; a property held by structure is in the shape. Code is the floor, for what the grammar cannot state.

## Symptoms

Each is a parse missing, and names the type that is missing. If a structure can represent a state, code will produce it.

- **A nullable beside a status.** `shippedAt` null unless shipped, with a check that the two agree. One type per state: `Placed`, `Shipped(shippedAt)`.
- **Flags.** `pending`, `solved`, `closed` as three booleans: eight combinations, three valid. A sum type.
- **Parallel collections.** Products and quantities aligned by index. One line type.
- **Unpacking.** A value object opened to pass its primitive to a collaborator. The collaborator's signature is wrong; it predates the type.
- **A setter.** Any state reachable from outside. Transitions are methods returning the next state's type; what is not a method is not a transition.

## By structure, two techniques

- Invalid transitions unrepresentable: φtypestate.
- Invalid values unrepresentable where the language is structural: φnominal-value-objects.

## Related

- The pattern this is the domain instance of: φparse-dont-validate.
- The boundary the invariants derive, and saving whole: φaggregates.
- A grammar that cannot state the invariant: φmodel-expressions.
- Transitions as types: φtypestate.
- Values that cannot be confused: φnominal-value-objects.
