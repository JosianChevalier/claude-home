---
tags: [batch-size, small-batches, flow]
---

# Batch size economics

**Thesis.** Holding cost grows fast with batch size; transaction cost can fall to near zero. So the optimal batch falls to the floor, the atomic commit.

## The U-curve

Reinertsen, *The Principles of Product Development Flow*: batch size has an economic optimum. **Transaction cost** per item falls as batches grow, **holding cost** rises; the optimum is the bottom of their sum. Lower either curve and the optimum moves.

## Transaction cost

What each batch pays to ship: manual tests, manual deployment, opening and reviewing a pull request.

- TDD and an automated pipeline cut it a lot.
- Trunk-based development cuts the pull request and the wait on a teammate (φtrunk-based-development).

It has almost no lower bound.

## Holding cost

Mostly cost of delay. Then speculative work. Then risk: the cost if it realizes, times its probability. Plus the load of holding it.

None of it shows: unshipped work sits on no shelf, so it piles up unnoticed, and the case for small batches looks weaker than it is.

**Delay.** A finished piece that waits earns nothing: the missed gain. Shipped at step 2 of 6, it earns from step 2; held for the whole batch, only from step 6. The cost runs even when nothing goes wrong.

**Speculative work.** Work built on an untested assumption about the product, not over-engineered code: users want it, the design holds. If the assumption fails, everything built on it is written off; if it roughly holds, it anchors what comes after (Tversky & Kahneman), which bends to fit it instead of the reverse. Only shipping tests it, and a piece built before what consumes it waits untested: hidden inventory, which just in time (Ohno) removes. Late feedback lets the exposure pile up across the batch; fast feedback caps it at one small piece.

**Failures.** Bigger batches fail more often (Accelerate: change failure rate. Deploy frequency is the inverse of batch size, and in Accelerate's capability model continuous delivery, which means small batches by definition, drives it.) Two reasons:

- **Hard to see.** A fault hides in a large diff. A move is checked at a glance (φmechanical-refactoring).
- **Faults combine.** Most outages come from several small faults lining up, not from one. n changes make n(n−1)/2 pairs that can interact, so risk grows faster than size. A small batch exposes each change alone. Wiring a configuration value that used to be null takes two commits: pass it and validate it, then use it. A wrong value shows before anything depends on it.

**Collision.** Two people on the same thing without knowing it: integration hazards, waste. Handled optimistically on trunk (φtrunk-based-development, optimistic locking).

**Cognitive load.** A batch soon exceeds working memory, then the load grows with the interactions between its changes. A small batch is fire and forget: review a tiny bit, ship it, clear it from your head.

## The reflex

The usual reflex attacks holding cost: synchronize ahead so that nobody works on the same thing.

- It is the pessimistic scheme: synchronization paid on every unit of work (φtrunk-based-development).
- It stops small cleanups along the way, since they may touch someone else's work. "Open another pull request for it" does not hold: a pull request is a transaction cost, so nobody opens it.

Holding cost moved a little, and new costs came with it.

## The asymmetry

Transaction cost can go to near zero: TDD, continuous deployment, trunk. Holding cost cannot. The optimum follows transaction cost down until it hits the floor: the smallest change that still works, the atomic commit (φatomic-commit). An optimum on a floor is not a dosage: the knob is at 10 (φagentic-extreme-programming).

## Related

- The floor: φatomic-commit.
- Collision, handled optimistically: φtrunk-based-development.
- Faults seen at a glance: φmechanical-refactoring.
- Batch size applied to plans: φbatch-slicing.
