---
tags: [refactoring, atomic-commit, verification]
---

# Rationale: Mechanical Refactoring

Why refactoring is a chain of moves known safe *before* they are applied, and why rewriting is not refactoring.

## Safe a priori, not because tests pass

An atomic refactoring move — rename, extract a function, inline a variable, move a side-effect-free line, make a value immutable where nothing mutates it, delete dead code — is **semantics-preserving by construction**. The move is valid whatever the code means, the way substituting equals for equals is valid whatever the expression denotes (Leibniz's law: replacing a term by an equal term does not change the truth of the statement). Tests confirm the move; they are not what makes it safe. The safety was known before the diff existed.

This is the property that makes chaining possible. A chain of moves each proven safe is proven safe as a whole — proof composes. A single large step must be re-proven from scratch, and the only available proof is *understanding the code*, which is exactly what the large step was supposed to spare us.

## The diff is its own proof

A mechanical move can be validated at a glance: the reviewer checks the *shape* of the diff (this is a rename; every occurrence changed; nothing else moved), not the meaning of the code. Validation cost is constant regardless of what the code does. A rewrite has the opposite property: the reviewer must reconstruct the old behavior, reconstruct the new one, and compare — validation cost proportional to the code's complexity, and error-prone in proportion.

If a diff cannot be validated by glancing at it, it is not a refactoring move. Either split it into moves that can, or admit it is a behavior change and treat it as one (@rationale/workflow-rhythm.md).

## Refactor before understanding

Because moves are safe without understanding, refactoring is how we *acquire* understanding, not what we do after acquiring it. Faced with opaque code: rename what is legible, extract what repeats, inline what obscures, and the structure surfaces on its own. Understanding is the output of the chain, not its precondition.

The reverse order — read until you understand, then rewrite cleanly — carries the risk in the wrong place. Understanding is the fallible step; a rewrite founded on a partial understanding silently drops the cases the reader missed. Moves drop nothing because they never depended on the reader's model.

## Rewriting is the anti-move

The tempting moment is mid-chain: "I see what this does now, let me just write it properly." Do not. The clarity was produced by the chain; a rewrite discards the proof the chain accumulated and replaces it with a bet on the reader's model. Keep chaining: the clean version is reachable by moves, and arriving by moves means arriving proven.

## Consequences

- One move, one commit — the commit is the proof unit (@rationale/small-batches.md).
- Never replace a body; reshape it progressively until the target shape is reached.
- A move that "needs" a behavior tweak to compile is two commits: the move, then the tweak — or a smaller move.
- Reviewers check diff shape, not code meaning. If meaning is needed, the diff is too big.
