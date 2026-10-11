---
tags: [harness-design, kaizen, cynefin]
---

# Harness Direction

**Thesis.** The harness is one way of making Cynefin's move from complex to complicated: the Wardley drift from genesis to commodity, applied to every piece of the complex that can be mechanized, one filter at a time.

In Cynefin a situation moves from complex to complicated when constraints make its patterns repeatable. Each step down adds a filter, not a wall: it absorbs the noise of that rung and passes the signal up ([[philosophy/abstraction-ladder]]). The complexity underneath is untouched.

The move happens in the liminal zone, and it can slip back. Watching for the moment a filter stops working, and dropping back into complexity when it does, is the constant adjustment of kaizen ([[philosophy/kaizen]]). A filter misses some signal; the engineer gets it back by going down ([[philosophy/conversation-as-interface]]).

Two engines move the boundary: better models, which are given to us, and the harness's own systematic exploration, which is ours. The second encodes metis, the practical sense of sessions, into techne: constraints the harness can run.

Between people that encoding fails (Scott). Here it holds because the harness is a tool, not a guidebook sent to others: the one encoding sees the encoding fail, in the next session, and what resists encoding escalates.

## The process

Start with tiny bricks: the agent micromanaged in session, one small thing at a time. Kaizen ([[philosophy/kaizen]]) makes a brick reliable. A reliable brick is composable, and a composable brick moves down one rung of the process tree ([[philosophy/session-design]], [[philosophy/abstraction-ladder]]), toward the leaf: what was steered by the human in session becomes a dispatch; a dispatch that recurs becomes a workflow; a workflow that no longer needs judgment becomes a leaf. Mechanization is the end of the path: scripts and headless agents.

Reliability makes the step down possible; reuse makes it worth taking. The path is Wardley's evolution axis: a brick starts at genesis, steered in session, and each rung down is a step of its commodification. Each rung trades judgment for a handover and a coordination step, and only a brick that runs often pays that back. So the head of the distribution, the low-level workflows run many times a day, commodifies first; the fat tail of one-off work stays at genesis ([[philosophy/context-splitting]], where to stop).

Each step down is a change of absorber, not of the variety. The work is as variable as before; the node now absorbs what used to escalate to the human.

## Agents on this path

An agent begins as a posture, or as an intention. The intention hardens into a definitive goal; the skills it composes codify, the communication between agents included: fixed roles, sentinel answers, one change per call. The drift ends when calling the agent as a sub-agent becomes calling it headless, as a step in a workflow.

A refactoring loop shows one step of the path. Before, the session agent runs the loop itself: it dispatches a refactorer, commits between cycles, decides when to stop from the refactorer's reports, and never edits code. The refactorer makes one tiny change per invocation, never commits, and answers a sentinel when the code is clean. Pre-commit hooks are the safety net. Every piece is shaped for determinism; only the loop itself runs on judgment. After, the loop is a script, a deterministic while loop that dispatches the same sub-agents headless (pattern: `scripts-own-state`, the script holds the loop and the state, the agent holds the judgment of one change):

```
before: loop run by the session agent         after: script, run by nobody
                                              
  dispatch refactorer ─▶ one tiny change        while true:
       report | sentinel                          claude -p refactorer
  dispatch committer  ─▶ commit                   [ sentinel ] && break
  decide when to stop  ◀─ judgment, each turn     git commit    # hook = safety net
                                                done
```

## Related

- The layers and their inertia: [[philosophy/three-layer-harness]].
- The units of process: [[philosophy/session-design]].
- The ladder the brick descends: [[philosophy/abstraction-ladder]].
- What each harness element is for: [[philosophy/harness-elements]].
- What a brick lower on the path can be run by: [[philosophy/model-tiers]].
