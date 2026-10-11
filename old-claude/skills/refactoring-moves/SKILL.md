---
name: refactoring-moves
description: Catalog of atomic refactoring moves. Loaded by the refactorer agent to know what "one tiny change" means.
---

# Refactoring Moves

A move is safe **before** you apply it — it preserves behavior by construction, whatever the code means. That is why you may refactor code you do not yet understand, and why a reviewer validates a move by glancing at the diff's shape, never by reading the code's meaning. If the diff needs understanding to validate, it is not a move.

A single atomic step is ONE of:

- Rename a variable, method, or class
- Extract a method
- Inline a method
- Inline a variable
- Move a side-effect-free line
- Make a value immutable where nothing mutates it
- Move a method to another class
- Move similar files to another package (batch into one commit)
- Introduce a parameter object
- Replace a conditional with polymorphism (one branch)
- Extract an interface
- Change a method signature
- Delete dead code

**If you're doing two of these at once, you're doing too much.**

## Red Flags — STOP

- "I'll commit after these three renames" → **No. One rename, one commit.**
- "This rename requires updating 12 files" → **That's fine — it's still one atomic rename.**
- "I need to move 5 similar files to a new package" → **That's fine — it's one move operation. Batch similar file moves into a single commit.**
- "I need to extract and rename in one step" → **Extract first, commit. Rename second, commit.**
- "The tests won't pass until I do both changes" → **Find a smaller step where they do.**
- "I need to replace this method body with new logic" → **No. Reshape it progressively: extract one helper, adjust the structure, simplify — one step at a time.**
- "I understand it now, let me rewrite it cleanly" → **No. The clarity came from the chain; a rewrite throws away the proof. Keep chaining moves until the clean shape is reached.**
- "I need to understand this before I can refactor it" → **Backwards. Rename, extract, inline — understanding is what the moves produce.**
- "This is too slow" → **Slow is smooth, smooth is fast. Batching causes bugs.**

## Lambdas and Method References

**Extract methods** to hide implementation details behind a readable name. Reference them with `this::method`.

```java
// GOOD — hides conversion details behind a name
.map(this::toRoomConsumptions)

private RoomConsumptions toRoomConsumptions(Entry<RoomId, Map<Instant, Double>> entry) {
    // conversion logic here
}
```

**Use partial application** when a pipeline step needs an extra parameter.

```java
// GOOD — captures siteHeatingConsumption into the pipeline
.map(distributeUsing(siteHeatingConsumption))

private Function<Weights, Distributed> distributeUsing(WattHour consumption) {
    return weights -> distribute.distribute(weights, consumption);
}
```

**Don't nest both.** If a method already exists for partial application, don't extract the inner lambda into yet another `Function<>`-returning method.

```java
// BAD — partial application wrapping another Function-returning method
private Function<Weights, Distributed> distributeUsing(WattHour consumption) {
    return applyDistribute(consumption);
}
private static Function<Weights, Distributed> applyDistribute(WattHour c) {
    return weights -> distribute.distribute(weights, c);
}
```

## Anti-Patterns

| Temptation | Why it's wrong |
|---|---|
| Big-bang refactor | Impossible to revert partially |
| Rewrite instead of reshape | Discards the proof; safety now depends on your understanding |
| "Refactoring" that changes behavior | That's a feature, not a refactor |
| Skipping commit because "it's trivial" | Trivial changes still break things |
| Combining move + rename | Two moves = two commits |
| Moving unrelated files together | Group only similar files sharing the same move |
| Using `--no-verify` | You just lost your safety net |

Rationale: @rationale/mechanical-refactoring.md, @rationale/change-in-place.md, @rationale/workflow-rhythm.md
