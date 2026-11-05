---
tags: [craft, clean-code, types, invariants, domain-modeling, tactical-ddd]
---

# Typestate

**Thesis.** The lifecycle state lives in the type (Strom & Yemini): an operation exists only on the states where it is legal, so an illegal transition is a compile error.

This is φalways-valid-domain applied to transitions: value objects make invalid values unrepresentable, typestate makes invalid transitions unrepresentable.

- `cancel()` is not guarded on `Shipped`; it is absent. Consumers ask for the one state they handle, `ship(order: Paid)`, and the checks downstream go.
- Immutability is load-bearing (φimmutability): a transition returns a fresh value of the next type. Mutating in place lets the runtime state drift from the static type. Using the returned value stands in for affine types.
- Each transition appends its domain event: state is derived, changes are facts.
- In TypeScript, an explicit literal discriminant lets classes narrow.

## Related

- The property this enforces for transitions: φalways-valid-domain.
- Why a transition returns a new value: φimmutability.
