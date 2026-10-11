---
tags: [harness-design, kaizen, cynefin]
---

# Rationale: Harness Direction

The harness evolves from complex toward complicated, by design. In Cynefin a situation moves from complex to complicated when constraints make its patterns repeatable. The move is proven by iteration in the liminal zone between the two, and it is rechecked, because it can slip back. Two engines move the boundary: better models, which are given to us, and the harness's own systematic exploration, which is ours. The second encodes metis, the practical sense of sessions, into techne: constraints the harness can run. Between people that encoding fails (Scott); here it holds because the one encoding sees the encoding fail, in the next session, and what resists encoding escalates.

## The process

Start with tiny bricks: the agent micromanaged in session, one small thing at a time. Kaizen ([[philosophy/kaizen]]) makes a brick reliable. A reliable brick is composable, and a composable brick moves down one rung of the process tree ([[philosophy/session-design]], [[philosophy/abstraction-ladder]]), toward the leaf: what was steered by the human in session becomes a dispatch; a dispatch that recurs becomes a workflow; a workflow that no longer needs judgment becomes a leaf. Mechanization is the end of the path: scripts and headless agents.

Reliability makes the step down possible; reuse makes it worth taking. The path is Wardley's evolution axis: a brick starts at genesis, steered in session, and each rung down is a step of its commodification. Each rung trades judgment for a handover and a coordination step, and only a brick that runs often pays that back. So the low-level, heavily reused workflows commodify first, and one-off work stays at genesis ([[philosophy/context-splitting]], where to stop).

Each step down is a change of absorber, not of domain. The work is as variable as before; the node now absorbs the variation that used to escalate to the human.

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
