---
tags: [session-design, workflow, sub-agents, context-economics, cynefin, variety-absorption]
---

# Rationale: Session Design

Process is a containment tree. Each node has an orchestrator, and the kind of unit is the degree to which that orchestrator's decisions are codified: who holds the steering at the node.

| Unit | Who decides at the node | Cynefin | Contains |
|---|---|---|---|
| **Session** | a human, in or on the loop | complex | dispatches, workflows |
| **Dispatch** | an agent, ad hoc, from inside a session | liminal: constrained enough to run as ordered, escalation as the escape hatch | workflows, leaves |
| **Workflow** | an orchestrator, human or agent, following a codified plan | ordered | workflows, leaves |
| **Leaf**: script or sub-agent | nobody: a step with no orchestration of its own | ordered | nothing |

The Cynefin column names the domain the orchestrator works in, not where variety arrives: complexity arrives at the leaf and is decided on at the session.

These are process units of the sociotechnical system, engineer plus harness. They are not harness elements: an agent, a sub-agent, an orchestrator, script or agent, is what materializes one of them ([[philosophy/harness-elements]]). The same materialization serves two units, and the way it is called tells them apart: a sub-agent is a dispatch when a session calls it live, a leaf when a workflow calls it headless.

"Workflow" is used in the sense of Anthropic's split: LLMs and tools orchestrated through predefined code paths, as opposed to agents that direct their own process. The dispatch is that agent side, bounded to one delegated task.

**Variety is absorbed at the lowest node that can take it.** The process tree is one sighting of the abstraction ladder; read it first ([[philosophy/abstraction-ladder]]). What is specific here is the chain: a leaf escalates to its workflow, a workflow to the dispatch or session that called it, a dispatch to the human, and what reaches the human is the kairos ([[philosophy/metis-kairos]]). The process tree and the three layers ([[philosophy/three-layer-harness]]) are two rung-sets of the same ladder. Where the boundary between human and codified sits is not fixed: it sits at the cost limit ([[philosophy/context-splitting]], where to stop), and moving it down is the harness's direction ([[philosophy/harness-direction]]).

**The dispatch is the probe.** It fits no reusable workflow, or runs where none exists yet. A dispatch that recurs is a workflow waiting to be codified; the meta-learning it brings back is the signal.

**A session is where a human is required.** The heuristic for telling a session from the other units is the doctrine of [[philosophy/collaborative-production]]: agents act, humans decide.

Handovers are the communication layer between sessions ([[philosophy/conversation-continuity]]).

A session is anchored in a working document, and conversation, document, repo are three stores ordered by inertia ([[philosophy/session-state-in-documents]]).
