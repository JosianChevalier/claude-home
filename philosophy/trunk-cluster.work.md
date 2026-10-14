---
ongoing_work_file: "Iterate the trunk cluster to landed: trunk-based-development, atomic-commit, agentic-trunk-based-development, then mechanical-refactoring, make-the-change-easy and agentic-extreme-programming. Empty when each has a thesis, a shape pass, a mapping row in sync-repo.work.md, and this file is deleted."
rank: 1
---

# Trunk cluster

Six philosophy files and one study on one idea: code integrated on trunk at the smallest granularity there is, the atomic commit, by humans and agents alike. Review in conversation, one issue per turn; the file is written and committed right after each decision, one commit per decision (MO in `sync-repo.work.md`).

## Steps

- [ ] `batch-size-economics` landed 2026-10-14 (Reinertsen's U-curve, transaction vs inventory cost in software), to review. `small-batches` stays separate (batch size applied to plans) and points at it at its migration. Open: whether `agentic-extreme-programming`, "The optimum is tiny", links it.
- [ ] Shape pass per file, second commit (`rules/writing.md`). In `atomic-commit`, the heading "Same file is not same change" no longer names what its section holds (atomic and meaningful).
- [ ] Rows in `sync-repo.work.md`, Mapping old → new, for the four files that have none: `trunk-based-development`, `atomic-commit`, `agentic-trunk-based-development`, `agentic-extreme-programming`. Note `continuous-delivery` and `small-batches` are pointed at from the backlog.
- [ ] Delete this file.

## Open

- The Reinertsen study now feeds `agentic-extreme-programming`, section "The optimum is tiny": its own file, or folded there.

- Hazard for the `continuous-delivery` migration: its old line "the branch shrinks to a conflict-avoidance queue and can shrink further to nothing" is softer than "branches are the exception"; align it then.
- Where the git mechanics live (trunk may not be a checked-out working tree; fast-forward refused otherwise): a rule, not philosophy. Successor of `old-claude/rules/branch-hygiene.md`, phase 3.3.

## Source: post on mechanical refactoring (Josian, 2026-10-13)

Reading refactored code is cognitively taxing, as we need to understand it to ensure it behaves the same. But that's not inevitable, it can be done mechanically even without tests.

Every refactor, no matter how large, can be decomposed into tiny moves that cost no understanding at all. Extracting a method, renaming, reordering side-effect-free code, turning an imperative loop into a map/filter. Each move could be applied or verified by a tool, and we can ensure that it is safe a priori, without even understanding the code. It can be validated by its shape alone. The safety is in the process itself.

This holds because refactor and redesign are two different things. A refactor doesn't change the underlying model, so tests and observable behavior are preserved. A redesign affects the model and can break the tests. Behavior may still be preserved, but knowing it takes understanding the old and the new, so it cannot always be mechanical.

The trick is to decompose the work into larger steps of model-preserving refactors and model-changing redesigns. Make the change easy, make the easy change, alternated. You can even slip in steps adding or changing features.

This is a great approach to manage cognitive load and reduce risk when coding manually, as it decomposes the work into tiny releasable batches. With AI-assisted coding, it is even more important, as it allows us to avoid investing cognitive resources in understanding mechanical refactoring, which can just be validated mechanically, by the shape of the diff, not the meaning of the code.

Isn't it slower though? Well, slow is smooth, smooth is fast. Measured to a first draft, maybe. Measured as lead time from ideation to production, it wins.
