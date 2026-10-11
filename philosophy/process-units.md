---
tags: [session-design, workflow, sub-agents, context-economics, cynefin, variety-absorption]
---

# The process units

**Thesis.** Process is a containment tree. Each node has an orchestrator, and the kind of unit is the degree to which that orchestrator's decisions are codified: who holds the steering at the node.

| Unit | Who decides at the node | Cynefin | Contains |
|---|---|---|---|
| **Session** | a human, in or on the loop | complex | dispatches, workflows |
| **Dispatch** | an agent, ad hoc, from inside a session | liminal: constrained enough to run as ordered, escalation as the escape hatch | workflows, leaves |
| **Workflow** | an orchestrator, human or agent, following a codified plan | ordered | workflows, leaves |
| **Leaf** | nobody: a step with no orchestration of its own | ordered | nothing |

The Cynefin column names the domain the orchestrator works in, not where variety arrives: variety arrives at the leaf and is decided on at the session.

These are process units of the sociotechnical system, engineer plus harness. They are not harness elements: an agent, a sub-agent, an orchestrator, script or agent, is what materializes one of them ([[philosophy/harness-elements]]). The same materialization serves two units, and the way it is called tells them apart: a sub-agent is a dispatch when a session calls it live, a leaf when a workflow calls it headless.

"Workflow" is used in the sense of Anthropic's split: LLMs and tools orchestrated through predefined code paths, as opposed to agents that direct their own process. The dispatch is that agent side, bounded to one delegated task.

## The chain up

**Variety is absorbed at the lowest node that can take it.** The process tree is one sighting of the abstraction ladder; read it first ([[philosophy/abstraction-ladder]]). What is specific here is the chain:

```
  session     the human; what arrives uncaught is the engineer's Observe
    ▲
  dispatch
    ▲
  workflow
    ▲
  leaf        where variety arrives first
```

A leaf escalates to its workflow, a workflow to the dispatch or session that called it, a dispatch to the human, where what arrives is the engineer's Observe ([[philosophy/metis-kairos]]). The process tree and the three layers ([[philosophy/three-layer-harness]]) are two ladders, two instances of abstraction layering.

Where the boundary between human and codified sits is not fixed: it sits at the cost limit ([[philosophy/context-splitting]], Where to stop), and moving it down is the harness's direction ([[philosophy/harness-direction]]).

## The two ends

**The dispatch is the probe.** It fits no reusable workflow, or runs where none exists yet. A dispatch that recurs is custom-built drifting to commodity: a workflow waiting to be codified; what it brings back about its own running is the signal to codify.

**A session is where a human is required.** The heuristic for telling a session from the other units is the doctrine of [[philosophy/collaborative-production]]: agents act, humans decide.

## Related

- The pattern this is a sighting of: [[philosophy/abstraction-ladder]].
- What materializes a unit: [[philosophy/harness-elements]].
- The communication layer between sessions: [[philosophy/conversation-continuity]].
- Where a session's state lives, three stores ordered by inertia: [[philosophy/session-state-in-documents]].
