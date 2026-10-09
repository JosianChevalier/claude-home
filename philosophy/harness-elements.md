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
| **Agent** | a posture, a wide goal, or both | for the whole session | it says how to behave and what for, not which steps |
| **Sub-agent** | a narrow goal plus the knowledge to reach it | for one delegated task, in a fresh context | goal in the definition, knowledge in composed skills |
| **Philosophy file** | theory: why the prescriptions hold | only when the work is on the harness itself: improving it, reviewing an artifact | written in the field's own terms (@rationale/attractors.md) |
| **Script, hook, tool** | a guarantee | when called, outside the model | the same result every time |

Each choice is first a loading decision (@rationale/context-economics.md) and second a reliability decision (@rationale/compounding-decisions.md).

## Deterministic what can and should be

Prose asks; code guarantees. An instruction the agent "must always" follow, on something a script could check or do, is a decision left to a model that will eventually get it wrong. *Can* is not enough: a step that needs judgment stays with the agent. *Should* is the test: is a guarantee needed here.

## Usual misplacements

- **A rule that needs explaining.** Always-on text is paid for in every session. If applying it takes context, it is a skill.
- **An agent that carries a procedure.** The steps belong in a skill, where another agent can reuse them and where they load only when needed. The agent keeps the posture and the goal.
- **A sub-agent that counts on a skill it never receives.** In Claude Code a sub-agent declares its skills. In OpenCode skills are not loaded by default: without the `opencode-preload` plugin, the knowledge is inlined in the sub-agent's prompt, or loading the skill is its first step.
- **A skill nobody triggers.** The description is matched against what the session contains. It states when to use the skill, in the words the user will actually say (@rationale/attractors.md).
- **Prose where a guarantee is needed.** See above.
