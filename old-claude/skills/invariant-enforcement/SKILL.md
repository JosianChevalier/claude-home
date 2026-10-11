---
name: invariant-enforcement
description: Use when enforcing an invariant on a known aggregate — type structure vs save ordering vs transaction, unit of work, constraint. NOT for finding the boundary (aggregate-identification).
---

# Invariant Enforcement

Enforce each safety property at the highest rung its media allow. Never descend without naming the grammar that blocks the rung above — an unnamed descent is compensation, not design.

## The ladder

1. **Structure** — the invalid state is unrepresentable (always-valid-domain); the aggregate root is the sole handle to interior state.
2. **Ordered saved steps** — only where the grammar cannot state the property (e.g. cross-row cardinality in SQL: the rule is cross-row, CHECK is row-local). Every intermediate saved state stays valid to observers.
3. **Shared unit of work** — last resort: no intermediate state observable at all.

## Exit criteria

Every safety property names its rung; every rung-2 or rung-3 choice names the blocking grammar.

Rationale: @rationale/aggregates.md
