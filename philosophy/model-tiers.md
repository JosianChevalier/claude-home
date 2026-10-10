---
tags: [harness-design, model-tiers, context-economics]
---

# Model tiers

**Doctrine.** Default to the most intelligent model.

A tier is set by two variables:

- how much decision the task carries
- what its failure costs

Only the harness lowers them, by recomposing the work ([[philosophy/harness-direction]]). A lower tier is earned that way, never chosen as a saving.

## The tiers

- **Top** (Opus class): anything with a decision, a concept, knowledge or design in it. Choosing what to build, judging, reviewing, conversing, reading documents for insight rather than facts.
- **Middle** (Sonnet class): execution without real decisions. The architecture and the spec are given; the model fits code to them. Automatic sub-agents that follow a workflow.
- **Small** (Haiku class): the extremely trivial. Commit messages. Mechanical sub-agents deployed in workflows to surface a piece of information.

## Why

Cognitive energy is sparser than tokens.

A tier below its task fails silently: the output looks like work done, and nothing says the decision was taken at the wrong level. Someone pays for that in attention, and attention is the scarce resource.

Anything user-facing is Top, with no step down. The session agent is the one node that never moves down the process tree; any stupidity from the model there is absorbed by the user.

## Why it stays affordable

Context economics ([[philosophy/context-economics]]). A lean window keeps the top tier cheap enough to remain the default even when a session runs long.

The alternative costs more on both sides:

- errors mean rework and extra tokens
- struggle means context bloat

The two doctrines hold each other up. Harnesses not conceived for context economy cannot afford this, and their default drifts down where it hurts most, on the decisions.

## How a tier moves

One loop, four stages. Tier in brackets.

```
1  session agent [Top]
   reads code, picks a change, applies it, commits, decides when to stop

2  orchestrator [Top: must not drift]
   │ loop
   ├─▶ refactorer [Top: decides the change] ─▶ one tiny change | NOTHING_TO_REFACTOR
   ├─▶ committer  [Small: mechanical, bad commit is cheap, hook is the net]
   └─  stop?  ◀── judgment, each turn

3  script
   │ while true
   ├─▶ claude -p refactorer [Top]
   ├─  sentinel → break
   └─▶ claude -p committer [Small]

4  script
   │ while true
   ├─▶ claude -p refactorer [Middle: refined prompt]
   ├─  sentinel → break
   └─▶ claude -p committer [Small]
   └─▶ last pass [Top]: anything missed, anything wrong? ─▶ loop again | done
```

1→2 splits by nature: each node gets the tier its decision content asks for.
2→3 removes a node that carried no decision once drift was ruled out.
3→4 steps the same node down: its failure is now cheap because a Top pass catches it.

## Related

- The process that recomposes the work: [[philosophy/harness-direction]].
- Why the top tier stays affordable: [[philosophy/context-economics]].
