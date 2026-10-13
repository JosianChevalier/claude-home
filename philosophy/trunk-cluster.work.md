---
ongoing_work_file: "Iterate the trunk cluster to landed: trunk-based-development, atomic-commit, agentic-trunk-based-development, then mechanical-refactoring and make-the-change-easy. Empty when each has a thesis, a shape pass, a mapping row in sync-repo.work.md, and this file is deleted."
rank: 1
---

# Trunk cluster

Five philosophy files and one study on one idea: code integrated on trunk at the smallest granularity there is, the atomic commit, by humans and agents alike. Three drafted 2026-10-12 (commit 2f31178), two to write. Review in conversation, one issue per turn; the file is written and committed right after each decision, one commit per decision (MO in `sync-repo.work.md`).

## Steps

- [ ] For every practice in the cluster: when agentic, analyse what changes. Standing, per file.
- [ ] Review the three drafts, in reading order.
  - [x] `trunk-based-development`: substance done 2026-10-13 (commits d6e58e3..aa4b34f).
  - [x] `agentic-trunk-based-development`: substance done 2026-10-13; renamed from `agents-on-one-trunk`, tag `agentic-extreme-programming`.
  - [ ] `atomic-commit`. **← current.** Techne gathered 2026-10-13 from the old skills (atomic-commit, atomic-refactoring, refactoring-moves, TDD, tester, green-implementor, refactorer, committer). Issue 1 in "Why the unit matters", near decided: Reading goes (argues from history), Revert becomes bounded loss (the smaller the step, the less redone after a failure), Proof and Integration stay. Issue 2: "One" gets its two tests. Issue 3: the manual/agentic shift.
- [ ] Thesis line per file, after the sections stand. Short: the file is not compressed into it.
- [ ] Write `mechanical-refactoring` (backlog: `old-claude/rationale/mechanical-refactoring.md`, tags `refactoring, atomic-commit, verification`), right after `atomic-commit` so its Proof bullet points at a file that exists. Source: the old rationale plus the post below. Center, new against the old file: a refactor preserves the model, a redesign changes it; a redesign may preserve behavior but knowing it takes understanding, so it is not mechanical. One line: the moves presuppose the design discipline (side-effect-free bodies, immutability) and produce it; a coherent body of practices, synergized. One line on agentic: validate by shape, spend no cognition on meaning.
- [ ] Write `make-the-change-easy`: alternate model-preserving refactors and model-changing redesigns, features slipped in between; make the change easy, make the easy change, pushed to the extreme. Source: the post below, fourth paragraph. No old counterpart known; check `old-claude/` first.
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
- **"One" has two tests, both held.** A single concern a reader names in a line; and no equivocation when collapsed: the reviewer validates the collapsed diff at once, by shape for a move, by the tests for a behavior. If lines must first be attributed to concerns, it is two commits. Addition plus its polish collapses; feature plus nearby cleanup does not; a rename across 12 files is one.
- **Tests on one unit of behavior group** because they require one atomic functional change. The hardcoded intermediates of GREEN are spent, not information.
- **"Whole" is continuous delivery's claim**, pointed at: production and its tests in the same commit, trunk releasable after it. Not re-argued in `atomic-commit`.
- **History is spent.** Intention lives in the present code and repository; a commit is validated, then forgotten. Fire and forget; a cluttered history costs nothing. Arguments from history (reading, bisect) go. What survives of revert: the smaller the step, the less is redone after a failure.
- **Manual and agentic differ on where the price is.** By hand, the atomic commit is a unit for the brain and a forcing function to move on: write a line, change it five times, what matters is the small safe steps. Agentic, generation is cheap and the price shifts to validating: the commit is the unit of validation. The thesis candidate, the largest change that still validates as one, is the agentic reading.

## Open

- Hazard for the `continuous-delivery` migration: its old line "the branch shrinks to a conflict-avoidance queue and can shrink further to nothing" is softer than "branches are the exception"; align it then.
- Where the git mechanics live (trunk may not be a checked-out working tree; fast-forward refused otherwise): a rule, not philosophy. Successor of `old-claude/rules/branch-hygiene.md`, phase 3.3.
- `atomic-commit` cites "tested" as half of whole. Third reading from the examples: "tested" means two things, confirmation for a move (safe before the diff existed), proof for a behavior (the failing test first). The file may say "production and its tests together" and leave the gate to the skill.
- `workflow-rhythm`, pointed at by the old rule and the moves skill, is not under `old-claude/rationale`. Where it lives, or gone.

## Source: post on mechanical refactoring (Josian, 2026-10-13)

Reading refactored code is cognitively taxing, as we need to understand it to ensure it behaves the same. But that's not inevitable, it can be done mechanically even without tests.

Every refactor, no matter how large, can be decomposed into tiny moves that cost no understanding at all. Extracting a method, renaming, reordering side-effect-free code, turning an imperative loop into a map/filter. Each move could be applied or verified by a tool, and we can ensure that it is safe a priori, without even understanding the code. It can be validated by its shape alone. The safety is in the process itself.

This holds because refactor and redesign are two different things. A refactor doesn't change the underlying model, so tests and observable behavior are preserved. A redesign affects the model and can break the tests. Behavior may still be preserved, but knowing it takes understanding the old and the new, so it cannot always be mechanical.

The trick is to decompose the work into larger steps of model-preserving refactors and model-changing redesigns. Make the change easy, make the easy change, alternated. You can even slip in steps adding or changing features.

This is a great approach to manage cognitive load and reduce risk when coding manually, as it decomposes the work into tiny releasable batches. With AI-assisted coding, it is even more important, as it allows us to avoid investing cognitive resources in understanding mechanical refactoring, which can just be validated mechanically, by the shape of the diff, not the meaning of the code.

Isn't it slower though? Well, slow is smooth, smooth is fast. Measured to a first draft, maybe. Measured as lead time from ideation to production, it wins.
