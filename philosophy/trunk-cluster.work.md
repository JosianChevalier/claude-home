---
ongoing_work_file: "Iterate the trunk cluster to landed: trunk-based-development, atomic-commit, agents-on-one-trunk, then mechanical-refactoring and make-the-change-easy. Empty when each has a thesis, a shape pass, a mapping row in sync-repo.work.md, and this file is deleted."
rank: 2
---

# Trunk cluster

Five philosophy files and one study on one idea: code integrated on trunk at the smallest granularity there is, the atomic commit, by humans and agents alike. Three drafted 2026-10-12 (commit 2f31178), two to write. Review in conversation, one issue per turn, file written after the decision (MO in `sync-repo.work.md`).

## Steps

- [ ] Review the three drafts, in reading order. **← current**
  - [ ] `trunk-based-development`: the concept. Read first.
  - [ ] `atomic-commit`: the granularity, and the splitting skill.
  - [ ] `agents-on-one-trunk`: the consequence for worktrees and agents.
- [ ] Thesis line per file, after the sections stand. Short: the file is not compressed into it.
- [ ] Write `mechanical-refactoring` (backlog: `old-claude/rationale/mechanical-refactoring.md`, tags `refactoring, atomic-commit, verification`): the mechanical split of a refactoring into moves safe by construction.
- [ ] Write `make-the-change-easy`: make the change easy, then make the easy change, pushed to the extreme. No old counterpart known; check `old-claude/` first.
- [ ] Study: Reinertsen's optimal batch size. The U-curve: transaction cost per batch falls as batches grow, holding (inventory) cost rises; the optimum is the bottom. The cluster's attractors are Reinertsen's, more than XP's: atomic commit is where the curve bottoms once transaction cost is near zero (the commit, the pipeline, the rebase all cheap). Where it lands: `small-batches` at its migration, or its own file. Decide after the review.
- [ ] Shape pass per file, second commit (`rules/writing.md`).
- [ ] Rows in `sync-repo.work.md`, Mapping old → new. Note `continuous-delivery` and `small-batches` are pointed at from the backlog.
- [ ] Delete this file.

## Decided

- **TBD is read as its spirit, not its tolerances: commit on trunk.** Continuous integration at the atomic commit. Seconds apart, a few lines: one rename, one extracted function, one moved variable. The canon's "under a day" is not what the file holds.
- **Branch, clone, worktree are one object**, a delta from trunk with a lifetime. Only the lifetime matters.
- **Coordination is optimistic locking.** Rebase is the version check, fast-forward the commit, conflict a retry on the new base. No synchronization beforehand, almost no communication bandwidth, fail fast.
- **Partition is not the default and not cancelled.** Ephemeral overlap is retried. Overlap that persists across commits means two actors hold the same thing: time to synchronize (talk, pair, redraw). Humans and agents alike.
- **The granularity rests on a splitting skill**, not on committing pace. Teams failed there. The skill is carried by `atomic-commit`, `mechanical-refactoring`, `make-the-change-easy`.
- **A worktree under the bound is a trunk-based committer**, identical not similar. Several agents on one repo need no orchestrator; the trunk is their channel, the diff not the conversations.
- **A rebase conflict is a check between steps** (`compounding-decisions`), not a decision taken alone.

## Open

- Name `agents-on-one-trunk`: coined, to confirm.
- Sentence in `agents-on-one-trunk`: "the overlap signal is read above the agents, not by them". An agent conflicting twice on the same lines could read it itself; placed above because synchronizing is the navigator's decision.
- Where the git mechanics live (trunk may not be a checked-out working tree; fast-forward refused otherwise): a rule, not philosophy. Successor of `old-claude/rules/branch-hygiene.md`, phase 3.3.
- `atomic-commit` cites "tested" as half of whole; whether that is the skill's test or the file's claim.
