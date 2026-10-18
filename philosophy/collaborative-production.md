---
tags: [collaboration, communication, cognitive-load, artifacts]
---

# Collaborative production

**Thesis.** The enacted loop stays unbroken: the conversation is the thinking in progress, the artifact crystallizes what is already understood, and the agent works inside the loop as the driver, not outside it as a producer.

**Failure mode.** Write, review, correct, review: code produced outside the loop, handed back as work never co-thought.

The engineer and the agent form one coupled system: the agent extends the engineer's intention, like a mecha-suit, rather than acting as an autonomous robot.

The mechanism behind the image: the agent is a **transmission** between the engineer's situated type and the concepts the code can hold — a belt, not a gear, because it must let load become perceptible instead of passing shock through silently ([[philosophy/model-phenomenology]], [[philosophy/transmission-belt]]). Everything below is that transmission seen from the workflow side.

```
navigator intent ──▶ driver: one move ──▶ mic back ──▶ … ──▶ artifact (checkpoint)
                        │
        does the choice change the concept the code will hold?
             yes ─▶ return it up the belt      no ─▶ infer, defer, or act
```

## The strong-style driver

In code, the image has an operational discipline behind it: **mob programming** (Zuill) with **strong-style** driving (Falco). For an idea to go from a head into the computer, it must pass through someone else's hands.

The driver is a smart input device: expert at the medium — editor, language, refactoring moves — and without authority over the concept. The navigators speak intent at the highest level of abstraction the driver can execute; the mob decides, out loud, and the driver never acts on an idea nobody said.

This is the mecha-suit split stated as a practice, and it is why the frame is chosen over rules: mob vocabulary carries the whole discipline — one step then the mic goes back, stop and talk when unsure, no arbitration between navigators — where a prohibition carries only itself.

**Autopilot** is the bounded exception: the navigators hand over a whole stage's intent, the driver runs it, and disengages at the first choice the plan does not settle. The pilots stay in their seats.

## Enactive work

Plans, studies, documents, and code emerge from interaction with the user and the system under change. The relevant point is enactive and extended: thinking happens through the act, and a notebook or an agent tightly coupled to it is part of the thinking. The boundary of the mind sits wherever that loop stays unbroken. The agent acts inside the engineer's loop, and the artifact externalizes the current shared model.

The loop has four faces, 4E cognition:

- **Enacted.** A model is built by taking part, not by watching.
- **Extended.** The agent and the notebook coupled to the act are part of the mind (Clark & Chalmers).
- **Embedded.** Thinking is situated in its terrain: the engineer still goes down to the code ([[philosophy/conversation-as-interface]]).
- **Embodied.** Thinking runs on the body's spatial machinery: the engineer moves through the code and feels where they are ([[philosophy/embodied-navigation]]).

The artifact is therefore not the primary act. The conversation is the act; the artifact crystallizes the current shared model. In belt terms: the conversation is where the belt runs, and the engineer's intention is carried, not improved — a better idea is a rival reading offered at a gate ([[philosophy/kairos-gates]]), an unchosen concept returns up the belt ([[philosophy/transmission-belt]]).

## Self-sufficient conversation

The engineer converses until the draft is ready; the artifact is opened at checkpoints, not during the exchange. So the conversation must be self-sufficient: everything needed to answer, decide, or steer — the question, the options, the relevant excerpt — is brought into chat as the work progresses.

A question whose answer requires opening the document forces a context switch and shifts extraneous load onto the engineer; "it's in the doc" is a failure of the exchange, not a shortcut. Zoom levels still apply inside chat ([[philosophy/zoom-levels]]): surface at the level of the decision, keep detail unfoldable.

## Cognitive load

Sweller's split governs the exchange. **Extraneous** load is the medium's — keyboard, format, placement, anything no concept turns on. **Intrinsic** load is the domain's — which concept the write will force into the code. The agent exists to remove the first and transmit the second intact: noise out, signal through, including the signal's friction, because that friction is where the engineer's type grows ([[philosophy/transmission-belt]]).

Two failures, one per load:

- **Interrogation**: the agent returns extraneous load up the belt — the medium turned into questions — and spends attention before it buys clarity. The belt too tight.
- **Silent choice**: the agent absorbs intrinsic load — picks among rival concepts and reports success — and the user discovers late that the direction was decided below. The belt too loose.

The test: does the choice change which concept the code will hold? Yes → intrinsic: return it. No → extraneous: infer it, defer it, or discover it by acting. Shape questions follow the same split ([[philosophy/shape-and-substance]]).

In mob terms this is what "intent at the highest abstraction the driver can execute" means: the same test keeps strong-style from sliding into interrogation.

## Chosen autonomy

**"The user decides, the agent does."** That is the doctrine. Interactive is its default form in this harness, not a dogma. An artifact that runs alone is legitimate when its author chose that.

The trouble is that autonomy is usually an accident: instructions written as "do X" produce an agent that does X and reports, and most people then complain that they have become spectators, without knowing how to make the thing interactive.

**Why the spectator pays.** Cognition is enacted (Enactive work, above): a model of the work is built by taking part in it. A person who only watches builds none: the loop is broken and the boundary of their mind has pulled back to their own head. Passivity is taxing in itself, before any review. The review that follows is then the most taxing way to catch up: the model has to be rebuilt from the output alone. This is why the person should be involved, and involved in the deciding.

**Posture is upstream.** A passive posture does not stay a posture problem. With nobody deciding along the way, the workflow runs long and the agent's decisions chain. A long run takes context at every step ([[philosophy/context-splitting]], the temporal axis); chained decisions compound their chances of error ([[philosophy/compounding-decisions]]). Both add to the waste the posture already caused.

**The measure is waste**, in three currencies: tokens, the person's cognitive energy, and time. Interaction that asks about things no decision turns on wastes all three (interrogation, above).

So does the opposite, and it is the worst case: **an autonomous run that ends in a large output to review**. The person was absent while the decisions were taken, then pays for all of them at once, with no way to tell the sound ones from the others, and the run is redone if one early decision was wrong ([[philosophy/compounding-decisions]]). Autonomy with a small, checkable output has none of these costs.

Waste is not the only measure: an artifact can be cheap and wrong. Reliability, and how the two feed each other: [[philosophy/compounding-decisions]].

## Making an artifact interactive

What works, in the order it is usually needed:

- **End the turn after one move.** One decision-sized step, then the mic goes back. An unconditional stop holds; "ask if unsure" does not.
- **Frame a session, not a deliverable.** "We are planning this together" keeps the conversation as the task. "Write the plan" makes the file the task, and the file wins against any instruction to stop and ask.
- **Ask only what changes the outcome.** The test of the cognitive-load section, given to the artifact as an instruction.
- **Name the mode.** Step by step with the person, a checkpoint at each stage, or alone with a small checkable output. An artifact that says which one it is can be held to it.
- **Give autopilot a word.** An explicit word hands over a whole stage; without it the agent stays in conversation. Autopilot disengages at the first choice the plan does not settle.
- **Open with a quick guide.** The first message states the mode, the trigger words, and that nothing changes unless asked. The person knows from the start how to steer.

## Related

- The mechanism this workflow is seen from: [[philosophy/transmission-belt]].
- What the belt transmits between: [[philosophy/model-phenomenology]].
- Where a better idea goes: [[philosophy/kairos-gates]].
- Surfacing at the level of the decision: [[philosophy/zoom-levels]].
- Why a long run costs, in context and in error: [[philosophy/context-splitting]], [[philosophy/compounding-decisions]].
- Shape questions under the same test: [[philosophy/shape-and-substance]].
- The embodied face of the loop: [[philosophy/embodied-navigation]].
- The embedded face, and the reflexive mode that designs its conditions: [[philosophy/embedded-reflexive]].
