---
tags: [craft, clean-code, types, invariants, domain-modeling, tactical-ddd]
---

# Nominal value objects

**Thesis.** A nominal type makes the wrong value hard to pass: arguments can't be swapped, and a representation can't be mistaken for another.

`transfer(from: AccountId, to: AccountId, amount: Money)` can't take its arguments in the wrong order. Nobody has to wonder whether an amount is in cents or in euros. That is the **Money** pattern (Fowler), with all that comes with it.

In a structurally typed language nominal types are manufactured: a class for a value with behaviour, a brand and a factory for an id.

## Related

- The property this enforces for values: φalways-valid-domain.
