---
tags: [harness-design, vocabulary]
---

# Harness elements

**Thesis.** A harness is a few kinds of element, each with one job: what it holds, when it loads, and the test that tells it is in the right place. Every element but the philosophy file points to its rationale, usually a philosophy file. Choosing one is a loading decision first (φcontext-economics), a reliability decision second (φcompounding-decisions).

## The elements

| Element | Holds | Loaded | Test |
|---|---|---|---|
| **Rule** | a short instruction that is always on | every session, or whenever its scope matches | it can be applied with no further context |
| **Skill** | reusable, composable knowledge | at runtime, when the task calls for it | several agents or tasks could use it |
| **Session agent** | a posture (verbosity, style), or an interlocutor for one task | for the whole session, human in the loop | it serves whatever the human brings; no goal of its own |
| **Sub-agent** | an intention: a task to handle, or a probe; generic at genesis, specialized around the product over time | for one dispatch, called live from a session, fresh context | intention in the definition, knowledge in composed skills |
| **Headless agent** | a goal, and the knowledge to reach it: a non-deterministic brick in a workflow, nothing more | for one workflow step, node or leaf, called by a script, human on the loop at most | a standardized answer the script can act on |
| **Philosophy file** | theory: why the prescriptions hold | only when the work is on the harness itself: improving it, reviewing an artifact | written in the field's own terms (φfield-terms) |
| **Script, hook, tool** | a guarantee | when called, outside the model | the same result every time |

One definition can serve as sub-agent, then headless: the call tells them apart, and the move from the first to the second is the agent's path (φharness-direction).

These elements are not the process units (φprocess-units): an element materializes a unit.

```
 element                   materializes                                        cynefin
 session agent             works in the session, where the human is            complex
 sub-agent, called live    a dispatch: the probe                               liminal
 skill + orchestrator      a workflow; orchestrator: an agent, then a script   ordered
 headless agent, script    a leaf                                              ordered
```

Orchestrator is a role, held by an agent or a script. An agent moving down this list is the harness's direction: its intention hardens into a goal (φharness-direction).

## Deterministic what can and should be

Prose asks; code guarantees. An instruction the agent "must always" follow, on something a script could check or do, is a decision left to a model that will eventually get it wrong. *Can* is not enough: a step that needs judgment stays with the agent. *Should* is the test: is a guarantee needed here, and does the step run often enough to pay for one. A guarantee is the commodity end of a step's path (φharness-direction).

## Usual misplacements

- **A rule that needs explaining.** Always-on text is paid for in every session. If applying it takes context, it is a skill.
- **An agent that carries a procedure.** The steps belong in a skill, where another agent can reuse them and where they load only when needed. The agent keeps the posture and the goal.
- **A sub-agent that counts on a skill it never receives.** A fresh context holds only what the definition declares. The knowledge is in composed skills, declared, or loading the skill is its first step.
- **A skill nobody triggers.** The description is matched against what the session contains. It states when to use the skill, in the words the user will actually say (φattractors).
- **Prose where a guarantee is needed.** See above.

## Related

- The process units the elements materialize: φprocess-units.
- The path an agent travels, from posture to headless: φharness-direction.
- The layers each element is written in: φthree-layer-harness.
