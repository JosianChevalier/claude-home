---
tags: [harness-design, reliability, determinism]
---

# Rationale: Compounding Decisions

Every decision an agent takes has a small chance of going wrong, and the chances multiply.

## The arithmetic

Reliability engineering calls it a **series system**: a chain that works only if every link works, so its reliability is the product of the links'. With `n` decisions each right with probability `p`, the run is right with probability `p^n`.

| Decisions | at 99% each | at 95% each |
|---|---|---|
| 10 | 90% | 60% |
| 50 | 61% | 8% |
| 100 | 37% | under 1% |

A model that is right 99 times out of 100 is impressive on one decision and unreliable over a long run. The number of decisions an artifact asks of the agent is therefore a design quantity, like the size of its context.

## What counts as a decision

Any place where the agent must choose and the artifact does not settle it: which file, which order, which format, whether a condition is met, when to stop. Vague wording manufactures decisions ("clean up as needed"). So does a long autonomous run, and so does an orchestrating agent, which decides at every dispatch.

## Reliability and waste

A harness element has two measures. **Waste** is what it costs when it works: tokens, the person's cognitive energy, time (@rationale/collaborative-production.md). **Reliability** is the chance that it does what was meant. They are not independent.

- **Context ties them.** An overloaded context costs tokens and loses precision in the same move (@rationale/context-economics.md). So `p` is not a constant: it falls as the context grows, and a long run is a long chain made of weaker links.
- **Failure is waste.** A wrong run is paid for twice in tokens and time. It also costs cognitive energy: someone has to find which decision failed, in an output they did not watch being made.
- **Posture feeds both.** A person kept out of the loop means a longer run and more chained decisions (@rationale/collaborative-production.md).

This is why the same remedies usually serve both measures.

## Three ways to shorten the chain

1. **Remove the decision.** What can and should be deterministic becomes a script, a hook or a tool; what has one good answer becomes a default written in the artifact (@rationale/harness-elements.md).
2. **Check between steps.** A verified step restarts the chain: an error caught at a checkpoint does not compound into the next step. Tests, a script that validates an output, a reviewing sub-agent with fresh context.
3. **Put the human on the decisions that matter.** A decision that changes which concept the work will hold is returned to the person, who is the most reliable link for it (@rationale/collaborative-production.md). The rest stays with the agent.

## Limits

The model is a simplification. Decisions are not independent, not all errors are fatal, and some are self-correcting (a failing test). It is used to compare two designs of the same artifact, never to compute a success rate.
