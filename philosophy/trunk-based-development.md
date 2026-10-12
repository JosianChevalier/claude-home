---
tags: [trunk-based-development, continuous-integration, git, concurrency]
---

# Trunk-based development

## One thing, three storages

A branch, a clone, a worktree are the same object: a **delta from trunk, with a lifetime**. They differ in where the delta is stored — a ref, another directory, another machine — and in nothing that matters. What a delta does to a team is decided by how long it lives, not by where it sits.

A developer's local clone is a branch: the unpushed commits are the delta, `pull --rebase` rebases it on trunk, `push` fast-forwards trunk to it. Nobody calls it branching, and it is.

## Commit on trunk

Trunk-based development, as read here, is the spirit of the practice and not its tolerances: **commit on trunk**. Continuous integration at the smallest granularity that exists, the atomic commit ([[philosophy/atomic-commit]]). One rename, committed. One extracted function, committed. One moved variable, committed. Seconds apart, a few lines each.

The bound on the lifetime of the delta is therefore one commit, and under that bound three verbs collapse into one:

```
commit  =  integrate  =  publish
```

There is no "committed but not yet shared" state. Work is private until the commit and public at the commit. Everything the practice promises — no merge ever, conflicts a few lines wide, trunk always current — follows from the bound, and from nothing else.

## Coordination is optimistic locking

Several actors committing to one trunk coordinate the way optimistic locking does:

| Optimistic locking | Trunk |
|---|---|
| shared record | trunk |
| transaction | the delta, its base commit as expected version |
| version check | the rebase |
| commit | the fast-forward |
| check fails | a rebase conflict: retry on the new base |

The premise of optimistic locking is that conflicts are rare compared to the cost of synchronizing. The one-commit bound makes the premise true by construction: the window for two deltas to overlap is seconds wide, and when the check fails the retry is a few lines, paid by the one who conflicted. Nobody else waits, nobody agrees on anything beforehand. Collaboration costs almost no communication bandwidth because it fails fast instead of synchronizing.

The pessimistic alternative — partition the work up front, each actor owning a region — pays the cost of synchronization on every unit of work to avoid a conflict that mostly would not have happened.

## The granularity is a skill

Seconds between commits is not a pace held by discipline; it is what a well-split change produces. Teams that did not integrate at this granularity were not slow at committing. They could not see the small steps inside the large one.

The practice therefore rests on a splitting skill, which this file depends on and does not own: what makes a commit atomic, and how a change decomposes into atomic commits ([[philosophy/atomic-commit]]).

## The overlap signal

Optimistic locking handles **ephemeral** overlap: two deltas touching the same place once, retried and gone.

Overlap that **persists** across commits is a different fact. Two actors are working on the same thing. A retry does not fix that and a lock would only hide it. It is the signal to synchronize: talk, pair, or redraw who holds what. The conflict rate alone is not the signal; the same spatial overlap returning commit after commit is.

## Related

- Every commit releasable; the branch shrinking to a conflict-avoidance queue, then to nothing: [[philosophy/continuous-delivery]].
- Batch size as the dominant variable, the atomic commit as its floor: [[philosophy/small-batches]].
- What makes a commit atomic, and the splitting skill: [[philosophy/atomic-commit]].
- The same practice applied to agents sharing one repository: [[philosophy/agents-on-one-trunk]].
