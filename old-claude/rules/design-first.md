# Design First

## Ideal Before Existing

When implementing new code that integrates with existing code:

1. **Design the ideal API** — what you *want* to write, unconstrained by what exists
2. **Find misalignment** — compare the ideal with reality
3. **Align reality** — refactor existing code to match the ideal (separate commit)
4. **Implement** — now the feature fits naturally

Never close the gap by degrading new code to match a flawed existing API.
The existing code is under our control — change it.

## When the Model Is In Play

Ideal-API design that touches domain state starts from the aggregate: dispatch **aggregate-identification** before shaping the API — the boundary shapes the ideal, not the existing persistence.

## Cascading Misalignment

If aligning the existing API causes misalignment in *other* places (callers break,
types don't fit, tests need reworking across boundaries), **stop and report to the user**.
This is a signal of **model tension** — the domain model may need a broader redesign
that shouldn't be decided unilaterally.

## Smell: Moving Code Around a Flawed Data Structure

If a data structure forces awkward access patterns (index-based correlation, parallel lists, defensive null checks), **the structure is the problem**. Moving the awkward code to a different class doesn't fix anything — redesign the structure.

**The test:** does the refactored code still make assumptions about alignment, ordering, or completeness that aren't enforced by the type? If yes, the data structure needs to change.

## Smell: Adapting New Code to a Flawed API

If your new code unwraps types, adds conversions, or uses workarounds to
satisfy an existing collaborator, **stop**. The collaborator's API is the problem,
not your new code. Fix the API first (or ask the user if unsure).

Rationale: @rationale/model-expressions.md, @rationale/aggregates.md
