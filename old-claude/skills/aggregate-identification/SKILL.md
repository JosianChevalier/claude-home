---
name: aggregate-identification
description: Use when deciding what is saved together — aggregate, boundary, invariant, consistency, atomicity, transactional scope. NOT for code-level type design (always-valid-domain) or bounded contexts (strategic axis).
---

# Aggregate Identification

Derive the consistency boundary from invariants — never draw it first, never borrow it from tables, transactions, or UI forms.

## Steps

1. **State each property in domain vocabulary.** One sentence a domain expert would sign; no table, transaction, or framework words.
2. **Classify it.** **Safety** — must hold in every saved state ("nothing bad ever happens"). **Liveness** — must only eventually hold ("something good eventually happens").
3. **Derive the boundary.** Everything a safety property mentions is saved together: one aggregate, its root the sole handle. Liveness spans aggregates and goes eventual.

## Guards

- Demanding immediate consistency across two aggregates = boundary wrong, or liveness mistaken for safety. Re-run step 2.
- A boundary that mirrors the table layout or the transaction scope without a forcing invariant is borrowed, not derived.

## Hand-off

Each safety property then climbs the enforcement ladder: dispatch **invariant-enforcement**.

Rationale: @rationale/aggregates.md
