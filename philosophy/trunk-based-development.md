---
tags: [trunk-based-development, continuous-integration, git, concurrency]
---

# Trunk-based development

**Thesis.** Trunk-based development is continuous integration, not a way of doing it; and continuous integration is trunk-based development.

## Commit on main

Trunk-based development, in the modern sense, is committing on main directly. Continuous integration is to integrate continuously, and continuously is more often than you think (Mike Roberts). A sync, rebase then fast-forward, takes seconds to minutes; a small team integrates tens to hundreds of times a day.

Unintegrated work lives one commit. Under that bound three verbs collapse into one:

```
commit  =  integrate  =  publish
```

There is no "committed but not yet shared" state. Everything the practice promises — no merge ever, conflicts a few lines wide, trunk always current — follows from the bound, and from nothing else. Holding the bound takes atomic commits, and the skill of splitting a change into them (φatomic-commit).

## Branches are the exception

"Short-lived branches" does not mean branch first and merge soon. It means: no branch, and when one is inevitable it lives hours at most. Ship/show/ask gives one of the few acceptable cases: isolate the part that must be asked, and only that part, onto a branch; the rest ships on trunk. The branch's commits obey the same discipline as trunk's (φcontinuous-delivery).

## Coordination is optimistic locking

Several actors committing to one trunk coordinate the way optimistic locking does:

| Optimistic locking | Trunk |
|---|---|
| shared record | trunk |
| transaction | the delta, its base commit as expected version |
| version check | the rebase |
| commit | the fast-forward |
| check fails | a rebase conflict: retry on the new base |

The one-commit bound makes optimistic locking's premise true by construction: the window for two deltas to overlap is seconds wide, and when the check fails the retry is a few lines, paid by the one who conflicted. Nobody else waits, nobody agrees on anything beforehand. Collaboration costs almost no communication bandwidth because it fails fast instead of synchronizing.

Partitioning the work up front is the pessimistic scheme: the cost of synchronization paid on every unit of work, against a conflict that mostly would not have happened.

## The overlap signal

Optimistic locking handles **ephemeral** overlap: two deltas touching the same place once, retried and gone.

Overlap that **persists** across commits is a different fact. Two actors are working on the same thing. A retry does not fix that and a lock would only hide it. It is the signal to synchronize: talk, pair, or redraw who holds what. The conflict rate alone is not the signal; the same spatial overlap returning commit after commit is.

## Related

- What makes a commit atomic, and the splitting skill: φatomic-commit.
- The same practice for agents sharing one repository: φagentic-trunk-based-development.
- Every commit releasable: φcontinuous-delivery.
- Batch size as the dominant variable, the atomic commit as its floor: φbatch-size-economics.
