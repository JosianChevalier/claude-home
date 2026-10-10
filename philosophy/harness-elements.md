---
tags: [harness-design, vocabulary]
---

# Rationale: Harness Elements

What each element of a harness is for.

## The elements

| Element | Holds | Loaded | Test |
|---|---|---|---|
| **Rule** | a short instruction that is always on | every session, or whenever its scope matches | it can be applied with no further context |
| **Skill** | reusable, composable knowledge | at runtime, when the task calls for it | several agents or tasks could use it |
| **Session agent** | a posture, sometimes oriented toward an activity | for the whole session, human in the loop | it serves whatever the human brings; no goal of its own |
| **Headless agent** | an intention on its way to a goal, and the knowledge to reach it | for one workflow step, called by a script, human on the loop at most | a clear objective, standardized to be integrated in a script orchestration, composable |
| **Sub-agent** | an intention on its way to a goal, and the knowledge to reach it | for one delegated task, called live from a session, fresh context | goal in the definition, knowledge in composed skills |
| **Philosophy file** | theory: why the prescriptions hold | only when the work is on the harness itself: improving it, reviewing an artifact | written in the field's own terms ([[philosophy/attractors]]) |
| **Script, hook, tool** | a guarantee | when called, outside the model | the same result every time |

Headless agent and sub-agent intersect: one agent definition serves both, and the call tells them apart. The headless agent is designed for process first; a human is not forbidden, but sits on the loop, not in it. The session agent is the one with the human in the loop.

These elements are not the process units ([[philosophy/session-design]]). A session is no element: it is where the human is, and the session agent works in it. A sub-agent materializes a dispatch, the probe. A headless agent or a script materializes a leaf. A workflow is a skill run by an orchestrator until it becomes a script. Orchestrator is a role, held by an agent or a script. The intention hardens into a goal as the agent moves down this path ([[philosophy/harness-direction]]).

Each choice is first a loading decision ([[philosophy/context-economics]]) and second a reliability decision ([[philosophy/compounding-decisions]]).

## Deterministic what can and should be

Prose asks; code guarantees. An instruction the agent "must always" follow, on something a script could check or do, is a decision left to a model that will eventually get it wrong. *Can* is not enough: a step that needs judgment stays with the agent. *Should* is the test: is a guarantee needed here.

## Usual misplacements

- **A rule that needs explaining.** Always-on text is paid for in every session. If applying it takes context, it is a skill.
- **An agent that carries a procedure.** The steps belong in a skill, where another agent can reuse them and where they load only when needed. The agent keeps the posture and the goal.
- **A sub-agent that counts on a skill it never receives.** A fresh context holds only what the definition declares. The knowledge is in composed skills, declared, or loading the skill is its first step.
- **A skill nobody triggers.** The description is matched against what the session contains. It states when to use the skill, in the words the user will actually say ([[philosophy/attractors]]).
- **Prose where a guarantee is needed.** See above.

## Related

- The process units the elements materialize: [[philosophy/session-design]].
- The path an agent travels, from posture to headless: [[philosophy/harness-direction]].
- The layers each element is written in: [[philosophy/three-layer-harness]].
