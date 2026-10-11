---
tags: [harness-design, context-economics, sub-agents, workflow]
---

# Context splitting

**Thesis.** A context is spent along two axes, space and time. When one axis resists, the question is not "how do I cut harder here" but "which cut on the other axis would free this one".

## Two axes

- **Spatial: the blast radius.** The size of the input and output one context works with. Signals: a full codebase, a wide search, a whole PDF or a long document read in one go, a large generated output.
- **Temporal: the run.** Two things grow with it. Different types of operation require different skills (the two hats of TDD), so a context that changes hats carries the harness of each one (rules, skills, agent prompt). And each successive operation takes context in turn, through the tokens of running it. Signals: reading, planning and acting in the same context; a long-lived process; a session that carries many steps before anyone looks.

The two multiply. A large input read by a context that then plans and acts on it pays for the input at every later step.

## The two cuts

**Spatial cut.** Modularise, and think map-reduce (Dean & Ghemawat): an orchestrator hands each slice to a sub-agent, each returns only its conclusion, the orchestrator reduces. The slices' tokens die with the sub-agents.

**Temporal cut.** Two hats (Beck), one at a time. One hat per context: each step runs in its own sub-agent, loaded with that step's harness only, and hands over through a file ([[philosophy/session-state-in-documents]]).

Sub-agents are the unit of both cuts. On the spatial axis, one sub-agent per slice of the input. On the temporal axis, one sub-agent per workflow step, composed with only that step's skills and context (TDD → test-writer, green implementor, refactorer). Skills are composable because this composition is deterministic: the agent definition declares what loads.

## A cut enables the next

The two are not alternatives tried in sequence. A cut on one axis can open the way for a cut on the other. It is like the puzzle games where you have to turn the puzzle around to find the next piece to move, or a meshwork where you have to undo along one dimension before you can attack the other.

```
 too big ──▶ cut in time ──▶ room appears ──▶ cut in space ──▶ new cuts in time
   PDF        convert, read   sections exist    one per chapter   summarise, compare
```

- *A scientific paper as a PDF.* An agent cannot easily split it by meaning, so the spatial cut is hard. Cut in time first: (1) convert to markdown, (2) read and process. Between the two there is now room for a step that cuts the text section by section. **The temporal cut enabled the spatial one.** Sections, once they exist, can be scheduled: read every chapter in parallel, summarise, then compare the summaries with the paper's own conclusion. **The spatial cut enabled new temporal ones.**
- *A feature changed across a codebase.* Too much for one context. Cut in space first: change module by module, keeping backward compatibility. That allows an order: start in the core domain, validate there, then propagate to the adapters and the consuming bounded contexts. **The spatial cut enabled the temporal one.**

## Where to stop

Two limits, of different kinds.

- *Indivisibility.* A limit of the material: no seam left. If you cannot split, change axis and state what you see on that one. If you still cannot, you have probably reached the bottom. Nothing moves this limit.
- *Cost.* A limit of the economics: a seam exists but cutting it does not pay. Each cut costs a handover and a coordination step; stop where the gain no longer justifies the overhead. Everything moves this limit: reuse, a cheaper handover, a deterministic net in place of a review step, a larger window.

The gap between the two is the evolution axis (Wardley). A low-level workflow that runs often is a candidate for commoditisation, and there the cuts go all the way down: one move per context, a deterministic net checking each step, the orchestrator reading reports and never code. That is agentic extreme programming; a one-off workflow does not earn it.

| Stage | Cuts | Stops at | Control flow |
|---|---|---|---|
| Genesis | few, one context | cost | human in the loop |
| Custom-built | some, where cheap | cost | orchestrating agent |
| Commodity | all the way down | indivisibility | script |

**Escalation.** The commodity end. When orchestration itself becomes too complex for an agent to hold, the intermediate steps move to code: a script that calls agents headless and owns the control flow. It is deterministic where an orchestrating agent decides ([[philosophy/compounding-decisions]]).

## Related

- Why context is scarce: [[philosophy/context-economics]].
- The handover file between temporal steps: [[philosophy/session-state-in-documents]].
- One hat per context, as session design: [[philosophy/session-design]].
