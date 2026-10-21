---
tags: [change-in-place, refactoring, small-batches, continuous-delivery]
---

# Change in place

**Thesis.** An existing path is changed where it stands, live at every step. Building the new shape beside it and plugging it in at the end is the big batch, however small its commits.

## The bias

Asked to change a working path, an agent rewrites: a new module beside the old one, plugged in at the end. Each commit looks small and green. None of them is live: the old path still serves production, and nothing tests the new one until the switch. The steps are small on paper; the batch is the whole rewrite, and all its risk lands at the switch ([[philosophy/batch-size-economics]]).

Small steps and atomic commits are worth something only if each one runs in production. Built beside, none does.

## In place

The code never leaves production: it changes shape under it, one move at a time, each live the moment it lands. A move is the lowest possible safe change: usually an atomic commit, like a mechanical refactoring ([[philosophy/mechanical-refactoring]]), but not always.

```
beside:    old ───────────────────────── switch   ← all the risk lands here
           new ── step ── step ── step ──┘
in place:  old ── step ── step ── step ── new     each step live
```

It is how making the change easy walks the path ([[philosophy/make-the-change-easy]]).

## The exception: a move slightly higher

Normally the chain advances one atomic move at a time, each activated in production as it lands. Sometimes a change can only be validated whole: an activation waiting on stakeholders, or parts that only work swapped together. Then the move sits slightly higher: its commits are deployed dark and activated together by a keystone, through an alternative flow such as expand/contract, an adapter or a flag. The two feedback loops are the ones of [[philosophy/feedback-loops]], activation in production and deployed in production.

What sits behind the keystone is a batch, so the swap goes at the lowest safe level, around the smallest piece that can only be validated whole.

- **Look lower first.** Before settling on a swap point, look for an approach that moves it lower.
- **It is lower than it looks.** The lowest point is hard to see and hard to design for.

## Related

- Why the batch must stay small: [[philosophy/batch-size-economics]].
- The moves: [[philosophy/mechanical-refactoring]].
- The rhythm it serves: [[philosophy/make-the-change-easy]].
- How work is cut: [[philosophy/batch-slicing]].
- The floor: [[philosophy/atomic-commit]].
