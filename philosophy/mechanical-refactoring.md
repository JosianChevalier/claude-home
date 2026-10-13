---
tags: [refactoring, atomic-commit, verification]
---

# Mechanical refactoring

## Safe before the diff exists

Any refactor, however large, decomposes into moves that are safe a priori. Use them to change the shape of the code without risking errors.

A refactoring move, rename, extract a function, inline a variable, move a side-effect-free line, make immutable what nothing mutates, delete dead code, is **semantics-preserving by construction**. It is valid whatever the code means, wherever the code is **referentially transparent**: equals substitute for equals, whatever they denote (Leibniz). Side effects make the code opaque, and the substitution stops holding: the limit of Leibniz's law, and the line between the two tiers below. A tool could apply it or verify it. Tests confirm the move; they are not what makes it safe. The safety was known before the diff existed, and it lives in the process, not in the reader.

This is what makes chaining possible. A chain of moves each safe is safe as a whole: proof composes. A single large step must be proven from scratch, and the only proof available is understanding the code, which is exactly what the small step was meant to spare.

## Safe a priori, applicable after a check

A move carries preconditions (Opdyke): once they hold, behavior is preserved. The safety is a priori; the applicability is checked.

- **Tier 1, local preconditions:** rename, extract, inline, unpack (surface what sat at a lower level). Safe anywhere, spaghetti included.
- **Tier 2, global preconditions:** reorder, loop to map. Safe only on side-effect-free code.

On spaghetti, tier 1 does the groundwork: it reorganizes the abstraction levels until the code is side-effect-free, and tier 2 opens. The price is the check. Confirming a tier 2 precondition means diving through the abstractions and surfacing every use of the affected functions; its reach grows with coupling.

## Validated by shape, not by meaning

A move is validated at a glance. The reviewer checks the shape of the diff: this is a rename, every occurrence changed, nothing else moved. The cost is constant, whatever the code does. A rewrite has the opposite property: reconstruct the old behavior, reconstruct the new, compare; the cost grows with the code's complexity, and the error rate with it.

If a diff needs understanding to be validated, it is not a move. Split it into moves that can be, or admit it is something else and treat it as such.

Agentic, this is where the gain is. Generation is cheap and validation is the price ([[philosophy/agentic-trunk-based-development]]); a move is validated without spending any cognition on what the code means, and the commit is its proof unit ([[philosophy/atomic-commit]]).

## Refactor preserves the model, redesign changes it

A refactor does not change the underlying model, so tests and observable behavior are preserved. A redesign changes the model, and can break the tests. Behavior may still be preserved, but knowing it takes understanding the old and the new: it cannot always be mechanical.

That is the boundary of the claim: moves cost no understanding as long as the model holds. Where the model changes, the mechanical part ends and the work is a redesign, taken in steps of its own and alternated with the refactors that prepare it ([[philosophy/make-the-change-easy]]).

## Act first, understand after

Because moves are safe without understanding, refactoring is how understanding is acquired, not what follows it. It is an **epistemic action** (Kirsh & Maglio): an action taken to make the problem easier to think about, not to move toward the goal, the way Tetris players rotate a piece on screen rather than in their heads. Faced with opaque code: rename what is legible, extract what repeats, inline what obscures, and the model surfaces. When understanding stalls, act first. The reverse order, read until it is understood then rewrite, carries the risk in the wrong place. Understanding is the fallible step; a rewrite founded on a partial understanding silently drops the cases the reader missed. Moves drop nothing, because they never depended on the reader's model.

Rewriting is the anti-move. The tempting moment is mid-chain: "I see what this does now, let me write it properly." The clarity was produced by the chain; a rewrite discards the proof the chain accumulated and replaces it with a bet on the reader's model. Keep chaining. The clean version is reachable by moves, and arriving by moves means arriving proven.

Agentic, the epistemic action mostly fades:

- **The human's part shrinks.** Dictating each move costs more than it gives. The act is one coarse instruction, clean up in place, and the human reasons over the cleaned shape.
- **A cleaning pass always pays for the agents that follow.** The code is context: tangled, it carves the wrong semantic valleys ([[philosophy/attractors]]); cleaned, it realigns them for every later step. Run it as its own step, a temporal cut ([[philosophy/context-splitting]]): clean, then change.

## Related

- One move, one commit, the commit as proof unit: [[philosophy/atomic-commit]].
- Refactor and redesign alternated: [[philosophy/make-the-change-easy]].
- Validation as the price: [[philosophy/agentic-trunk-based-development]].
