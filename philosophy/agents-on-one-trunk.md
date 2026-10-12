---
tags: [trunk-based-development, agents, worktrees, concurrency]
---

# Agents on one trunk

## One thing, three storages

A branch, a clone, a worktree are the same object: a **delta from trunk, with a lifetime**. They differ in where the delta is stored — a ref, another directory, another machine — and in nothing that matters. What a delta does to a team is decided by how long it lives, not by where it sits.

A developer's local clone is a branch: the unpushed commits are the delta, `pull --rebase` rebases it on trunk, `push` fast-forwards trunk to it. Nobody calls it branching, and it is.

## A worktree is a trunk-based committer

Trunk-based development is commit on trunk: the lifetime of a delta is one commit, and that bound is the only thing that ever defined a trunk-based committer ([[philosophy/trunk-based-development]]). A worktree that rebases on trunk and fast-forwards it at each commit meets the bound. It **is** a trunk-based committer — not similar, identical.

One worktree per agent is a convenience of the filesystem: separate working directories, one object store, one trunk.

## No orchestration between agents

Several agents can therefore work on the same local repository with nothing coordinating them: each commits, fast-forwards trunk, rebases on it, at every commit. Coordination is optimistic locking, as it is for humans on a trunk: no synchronization beforehand, a conflict caught at the next rebase and retried on the new base.

An orchestrator partitioning the work up front is the pessimistic scheme. For agents it costs more than for humans: a decision at every dispatch, a chain of its own ([[philosophy/compounding-decisions]]), to avoid conflicts that mostly would not have happened.

## The trunk is the communication channel

Each rebase is an agent reading what the others did since its last commit, in the form that costs least: the diff, never their conversations ([[philosophy/context-economics]]). Nothing of another agent's context enters this one; only the artifact does, and only the part that changed.

A rebase conflict is not a decision the agent takes alone. It is a check between steps ([[philosophy/compounding-decisions]]): self-correcting like a failing test, caught before it compounds.

## What stays above the agents

The granularity is the same as for humans: atomic commits, seconds apart ([[philosophy/atomic-commit]]). An agent is not at that granularity by nature; it gets there with the splitting skill, which the harness must carry.

And the overlap signal is read above the agents, not by them: the same spatial overlap returning commit after commit means two actors hold the same thing, and it is time to synchronize — redraw who holds what, or merge the two into one. Agents or humans, the signal reads the same.

## Related

- The practice and why it coordinates without synchronizing: [[philosophy/trunk-based-development]].
- The conflict as a check between steps; the orchestrator as a decision chain: [[philosophy/compounding-decisions]].
- Why the diff, not the conversation: [[philosophy/context-economics]].
- The granularity, and the skill it rests on: [[philosophy/atomic-commit]].
