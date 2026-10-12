---
ongoing_work_file: "Iterate the trunk cluster to landed: trunk-based-development, atomic-commit, agentic-trunk-based-development, then mechanical-refactoring and make-the-change-easy. Empty when each has a thesis, a shape pass, a mapping row in sync-repo.work.md, and this file is deleted."
rank: 2
---

# Trunk cluster

Five philosophy files and one study on one idea: code integrated on trunk at the smallest granularity there is, the atomic commit, by humans and agents alike. Three drafted 2026-10-12 (commit 2f31178), two to write. Review in conversation, one issue per turn; the file is written and committed right after each decision, one commit per decision (MO in `sync-repo.work.md`).

## Steps

- [ ] Review the three drafts, in reading order.
  - [x] `trunk-based-development`: substance done 2026-10-13 (commits d6e58e3..aa4b34f).
  - [x] `agentic-trunk-based-development`: substance done 2026-10-13; renamed from `agents-on-one-trunk`, tag `agentic-extreme-programming`.
  - [ ] `atomic-commit`. **← current.** Fresh session. First issue proposed, not decided: in "Why the unit matters", cut the Revert and Reading bullets (in the weights), keep Proof and Integration (the cluster's claims). Second reading: keep all four for the skill's sake. Then the "tested" question below.
- [ ] Thesis line per file, after the sections stand. Short: the file is not compressed into it.
- [ ] Write `mechanical-refactoring` (backlog: `old-claude/rationale/mechanical-refactoring.md`, tags `refactoring, atomic-commit, verification`): the mechanical split of a refactoring into moves safe by construction.
- [ ] Write `make-the-change-easy`: make the change easy, then make the easy change, pushed to the extreme. No old counterpart known; check `old-claude/` first.
- [ ] Study: Reinertsen's optimal batch size. The U-curve: transaction cost per batch falls as batches grow, holding (inventory) cost rises; the optimum is the bottom. The cluster's attractors are Reinertsen's, more than XP's: atomic commit is where the curve bottoms once transaction cost is near zero (the commit, the pipeline, the rebase all cheap). Where it lands: `small-batches` at its migration, or its own file. Decide after the review.
- [ ] Shape pass per file, second commit (`rules/writing.md`).
- [ ] Rows in `sync-repo.work.md`, Mapping old → new. Note `continuous-delivery` and `small-batches` are pointed at from the backlog.
- [ ] Delete this file.

## Decided

- **TBD is commit on main directly.** Seconds to minutes to sync, tens to hundreds of integrations a day for a small team. The canon's "under a day" is not what the file holds.
- **Branches are the exception.** "Short-lived" means when inevitable, hours at most; not branch-first. Ship/show/ask: isolate what must be asked onto the branch, the rest ships on trunk.
- **Three files, not four.** Optimistic locking and the overlap signal are human TBD: they stay in `trunk-based-development`. Branch = clone = worktree (the storages) is the agentic step: it opens `agentic-trunk-based-development`. No separate synchronization file.
- **What we optimize for is communication bandwidth and the cost of synchronization**; those phrases stay. Definitions the weights carry go.
- **Locking fits agents better than humans**: often different sessions, cheaper retry, shorter window. In the agentic file.
- **Branch, clone, worktree are one object**, a delta from trunk with a lifetime. Only the lifetime matters.
- **Coordination is optimistic locking.** Rebase is the version check, fast-forward the commit, conflict a retry on the new base. No synchronization beforehand, almost no communication bandwidth, fail fast.
- **Partition is not the default and not cancelled.** Ephemeral overlap is retried. Overlap that persists across commits means two actors hold the same thing: time to synchronize (talk, pair, redraw). Humans and agents alike.
- **The granularity rests on a splitting skill**, not on committing pace. Teams failed there. The skill is carried by `atomic-commit`, `mechanical-refactoring`, `make-the-change-easy`.
- **A worktree under the bound is a trunk-based committer**, identical not similar. Several agents on one repo need no orchestrator; the trunk is their channel, the diff not the conversations.
- **A rebase conflict is a check between steps** (`compounding-decisions`), not a decision taken alone.
- **The overlap signal is read above the agents**: redrawing who holds what is the navigator's decision, not a retry. Settled 2026-10-13.

## Open

- Hazard for the `continuous-delivery` migration: its old line "the branch shrinks to a conflict-avoidance queue and can shrink further to nothing" is softer than "branches are the exception"; align it then.
- Where the git mechanics live (trunk may not be a checked-out working tree; fast-forward refused otherwise): a rule, not philosophy. Successor of `old-claude/rules/branch-hygiene.md`, phase 3.3.
- `atomic-commit` cites "tested" as half of whole; whether that is the skill's test or the file's claim.
