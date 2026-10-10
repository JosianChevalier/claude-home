---
tags: [session-design, workflow, sub-agents, context-economics, cynefin]
---

# Rationale: Session Design

Process is a containment tree. Each node has an orchestrator, and the kind of unit is the degree to which that orchestrator's decisions are codified: who holds the steering at the node.

| Unit | Who decides at the node | Cynefin | Contains |
|---|---|---|---|
| **Session** | a human, in or on the loop | complex | dispatches, workflows |
| **Dispatch** | an agent, ad hoc, from inside a session | the edge: complex run as complicated | workflows, leaves |
| **Workflow** | an orchestrator, human or agent, following a codified plan | complicated | workflows, leaves |
| **Leaf**: script or sub-agent | nobody: a step with no orchestration of its own | clear, or complicated absorbed inside the leaf | nothing |

These are process units of the sociotechnical system, engineer plus harness. They are not harness elements: an agent, a sub-agent, an orchestrator, script or agent, is what materializes one of them ([[philosophy/harness-elements]]). The same materialization serves two units, and the way it is called tells them apart: a sub-agent is a dispatch when a session calls it live, a leaf when a workflow calls it headless.

"Workflow" is used in the sense of Anthropic's split: LLMs and tools orchestrated through predefined code paths, as opposed to agents that direct their own process. The dispatch is that agent side, bounded to one delegated task.

**Variation is absorbed at the lowest node that can take it**, and escalates one level up when it exceeds that node's codification: a leaf to its workflow, a workflow to the dispatch or session that called it, a dispatch to the human. The process tree and the three layers ([[philosophy/three-layer-harness]]) have the same shape, the abstraction ladder ([[philosophy/abstraction-ladder]]): Cynefin's "absorb complexity closest to where it arises", applied to time instead of knowledge. What reaches the human is the kairos ([[philosophy/metis-kairos]]). Where the boundary between human and codified sits is not fixed; moving it down is the harness's direction ([[philosophy/harness-direction]]).

**The dispatch is the probe.** It fits no reusable workflow, or runs where none exists yet. A dispatch that recurs is a workflow waiting to be codified; the meta-learning it brings back is the signal.

**A session is where a human is required.** The heuristic for telling a session from the other units is the doctrine of [[philosophy/collaborative-production]]: agents act, humans decide.

Handovers are the communication layer between sessions ([[philosophy/conversation-continuity]]).

## The session is anchored in a working document

By default a conversation is trashable: what exists only in it is state already decided to be lost ([[philosophy/session-state-in-documents]]). So, unless explicitly not required, a session gets anchored in a working document: an existing study or plan, or something else, committed or not, or in `/tmp`, depending on the nature of the work and above all on its longevity. Some sessions do not need one: a conversation that drifts a bit. When it drifts too much, it is worth asking whether to anchor it. Conversation, working document, repo is the ladder again, ordered by longevity: what survives the conversation reaches the document, what survives the document is committed ([[philosophy/abstraction-ladder]]).
