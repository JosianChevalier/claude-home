---
tags: [batch-size, small-batches, flow]
---

# Batch size economics

**Thesis.** Inventory cost grows fast with batch size; transaction cost can fall to near zero. So the optimal batch falls to the floor, the atomic commit.

## The U-curve

Reinertsen, *The Principles of Product Development Flow*: batch size has an economic optimum. **Transaction cost** per item falls as batches grow, **holding cost** (inventory) rises; the optimum is the bottom of their sum. Lower either curve and the optimum moves.

## Transaction cost

What each batch pays to ship: manual tests, manual deployment, opening and reviewing a pull request.

- TDD and an automated pipeline cut it a lot.
- Trunk-based development cuts the pull request and its review ([[philosophy/trunk-based-development]]).

It has almost no lower bound.

## Inventory cost is risk

Mostly risk: the cost if it realizes, times its probability. Two kinds.

**Failures.** Bigger batches fail more often (Accelerate: change failure rate). Two reasons:

- **Hard to see.** A fault hides in a large diff. A move is checked at a glance ([[philosophy/mechanical-refactoring]]).
- **Faults combine.** Most outages come from several small faults lining up, not from one. n changes make n(n−1)/2 pairs that can interact, so risk grows faster than size. A small batch validates each fault alone: pass the configuration that was null, show it in a log, then use it.

**Collision.** Two people on the same thing without knowing it: integration hazards, waste. Handled optimistically on trunk ([[philosophy/trunk-based-development]], optimistic locking).

## The reflex

The usual reflex attacks inventory cost: synchronize ahead so that nobody works on the same thing.

- It adds a synchronization cost.
- It stops small cleanups along the way, since they may touch someone else's work. "Open another pull request for it" does not hold: a pull request is a transaction cost, so nobody opens it.

Inventory cost moved a little, and new costs came with it.

## The asymmetry

Transaction cost can go to near zero: atomic commits, continuous deployment. Inventory cost cannot. The optimum follows transaction cost down until it hits the floor: the smallest change that still works, the atomic commit ([[philosophy/atomic-commit]]). An optimum on a floor is not a dosage: the knob is at 10 ([[philosophy/agentic-extreme-programming]]).

## Related

- The floor: [[philosophy/atomic-commit]].
- Collision, handled optimistically: [[philosophy/trunk-based-development]].
- Faults seen at a glance: [[philosophy/mechanical-refactoring]].
- Batch size applied to plans: [[philosophy/small-batches]].
