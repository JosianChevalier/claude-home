---
tags: [change-in-place, refactoring, small-batches, continuous-delivery]
---

# Change in place

**Thesis.** An existing path is changed where it stands, live at every step. Building the new shape beside it and plugging it in at the end is the big batch, however small its commits.

## The bias

Asked to change a working path, an agent rewrites: a new module beside the old one, plugged in at the end. Each commit looks small and green. None of them is live: the old path still serves production, and nothing tests the new one until the switch. The steps are small on paper; the batch is the whole rewrite, and all its risk lands at the switch ([[philosophy/batch-size-economics]]).

Small steps and atomic commits are worth something only if each one runs in production. Built beside, none does.

## In place

The path goes from old shape to new by a chain of moves, each live the moment it lands ([[philosophy/mechanical-refactoring]]). The code never leaves production; it changes shape under it.

```
beside:    old ───────────────────────── switch   ← all the risk lands here
           new ── step ── step ── step ──┘
in place:  old ── step ── step ── step ── new     each step live
```

It is how making the change easy walks the path ([[philosophy/make-the-change-easy]]).

## The exception, at the smallest atom

Sometimes one step cannot be made in place without regression: the new behavior needs another shape at a boundary the callers depend on. Then, and only then, an alternative flow: expand/contract, an adapter, a branch behind a flag.

- **The smallest atom.** It covers the one piece that cannot change in place, not the function around it.
- **Adopted in the same step.** Once parity is proven, it goes live in the step that brings it. It never waits dark for a later switch. Behind a flag is not dark: reachable and exercised, only invisible.

## When steps cannot be validated in place

Some changes can only be validated whole: an activation waiting on stakeholders, or parts that only work swapped together. They are built dark and swapped by a keystone at the lowest safe level, around the smallest piece that can only be validated whole. What sits behind it is a batch.

- **Look lower first.** Before settling on a swap point, look for an approach that moves it lower.
- **It is lower than it looks.** The lowest point is hard to see and hard to design for.

## Related

- Why the batch must stay small: [[philosophy/batch-size-economics]].
- The moves: [[philosophy/mechanical-refactoring]].
- The rhythm it serves: [[philosophy/make-the-change-easy]].
- How work is cut: [[philosophy/batch-slicing]].
- The floor: [[philosophy/atomic-commit]].
