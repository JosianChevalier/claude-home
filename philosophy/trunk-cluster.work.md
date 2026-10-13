---
ongoing_work_file: "Iterate the trunk cluster to landed: trunk-based-development, atomic-commit, agentic-trunk-based-development, then mechanical-refactoring, make-the-change-easy and agentic-extreme-programming. Empty when each has a thesis, a shape pass, a mapping row in sync-repo.work.md, and this file is deleted."
rank: 1
---

# Trunk cluster

Six philosophy files and one study on one idea: code integrated on trunk at the smallest granularity there is, the atomic commit, by humans and agents alike. Review in conversation, one issue per turn; the file is written and committed right after each decision, one commit per decision (MO in `sync-repo.work.md`).

## Steps

- [ ] For every practice in the cluster: when agentic, analyse what changes. Standing, per file.
- [ ] Review the three drafts, in reading order.
  - [x] `trunk-based-development`: substance done 2026-10-13 (commits d6e58e3..aa4b34f).
  - [x] `agentic-trunk-based-development`: substance done 2026-10-13; renamed from `agents-on-one-trunk`, tag `agentic-extreme-programming`.
  - [x] `atomic-commit`: substance done 2026-10-13; glanceable added as the test for a move. Shape pass: the heading "Same file is not same change" no longer names what the section holds (atomic and meaningful).
- [ ] Thesis line per file, after the sections stand: `**Thesis.** …` under the title, grepable. Short: the file is not compressed into it. Three left: `trunk-based-development`, `atomic-commit`, `agentic-trunk-based-development`.
- [ ] `agentic-extreme-programming`: first draft written 2026-10-13, thesis in. **← current.** Left: review in conversation, section by section; sections 1 and 2 of 4 done, at section 3 ("Crossing the valley"): "valley" stays against the sense it has in `attractors`, Wright and Kauffman being the attractor; open, a second attractor from evolution for this section, candidates on the table (epistasis, shifting balance, local optimum, no foresight, Gavetti & Levinthal). The five bullets of its "Agentic" section are one-line readings of the files they point to, not checked against them.
- [ ] `make-the-change-easy`: the existing file, renamed from `workflow-rhythm` 2026-10-14, thesis in. Left: check it against the post below, fourth paragraph (refactors and redesigns alternated, features slipped in between).
- [ ] Study: Reinertsen's optimal batch size. The U-curve: transaction cost per batch falls as batches grow, holding (inventory) cost rises; the optimum is the bottom. The cluster's attractors are Reinertsen's, more than XP's: atomic commit is where the curve bottoms once transaction cost is near zero (the commit, the pipeline, the rebase all cheap). Where it lands: `small-batches` at its migration, or its own file. Decide after the review. Holding cost is named there only: `agentic-extreme-programming` dropped it 2026-10-14, the batch-economics file carries it.
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
- **Atomic and meaningful.** Atomic: an operation that cannot be split without breaking trunk (a rename across 12 files is one). Meaningful: the next step does not override it. A step overridden right after folds into the step that overrides it, until the fold stands: addition and polish, green and its refactor, tests on one unit of behavior. A fix and a rename do not fold. What stands is validated at once, by shape for a move, by the tests for a behavior.
- **"Whole" is continuous delivery's claim**, pointed at: production and its tests in the same commit, trunk releasable after it. Not re-argued in `atomic-commit`.
- **History is spent.** Intention lives in the present code and repository; a commit is validated, then forgotten. Fire and forget; a cluttered history costs nothing. Arguments from history (reading, bisect) go. What survives of revert: the smaller the step, the less is redone after a failure.
- **Manual and agentic differ on where the price is.** By hand, the atomic commit is a unit for the brain and a forcing function to move on: write a line, change it five times, what matters is the small safe steps. Agentic, generation is cheap and the price shifts to validating: the commit is the unit of validation. The thesis candidate, the largest change that still validates as one, is the agentic reading.
- **Mechanical refactoring's thesis:** refactoring costs no understanding; understanding is spent on the model, and only there. Stated as a line under the title; the boundary (redesign) comes later, as the limit of the claim. Settled 2026-10-13.
- **Acting to understand is the human epistemic action** (Kirsh & Maglio), pre-agentic first and foremost. Agentic, it moves to the agent: the human says "clean up in place" and reasons over the cleaned shape. Settled 2026-10-13.
- **Where the moves hold: referential transparency, Leibniz as its name.** Functional-style code holds it everywhere, no check. Side effects make code opaque and a move acquires preconditions (Opdyke): local ones (rename, extract, inline) hold anywhere, global ones (reorder, loop to map) hold on side-effect-free code after a check whose reach grows with coupling. One paragraph, not a taxonomy. Settled 2026-10-13.
- **Glanceable diff.** A diff whose validity is seen, not read: the test for a move, in both `mechanical-refactoring` (defined, section "The diff is its own proof") and `atomic-commit` (atomic for the trunk, glanceable for the reviewer; the agentic unit of validation is the largest change still glanceable). Property of the diff as presented, not of its size. Settled 2026-10-13.
- **Agentic, a cleaning pass always pays.** The code is context: cleaned, it realigns the semantic valleys for the agents that follow. Its own step, a temporal cut: clean, then change. Settled 2026-10-13.
- **`agentic-extreme-programming` is the frame of the cluster**, not a file on functional style: a coherent set of practices asks for no trade-off. The design discipline the moves presuppose is one instance in it. Settled 2026-10-13.
- **The agentic practices are not XP's set unchanged**: they have been rethought for agentic programming. The thesis of `agentic-extreme-programming` stays the frame and says agentic in passing; the file has no second point. Settled 2026-10-14.
- **The optimum is a floor, not a trade-off.** The knob is pushed to 10: the optimum is the smallest possible change that still works. What is left to decide is not between practices (nothing to choose, nothing to adjust so one does not go too far): it is how far to go into them, how much is invested against how much comes back. Settled 2026-10-14.

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
