# Philosophy

You may never run an agent and still share the concern this repository starts from: attention is the scarce thing, and most tooling spends it. The philosophy is that concern worked out, and it reads by hand. Nothing in it needs an agent to open.

What the harness serves is one socio-technical system: the human at the centre, augmented by agents. Three properties of it are designed, and never apart: the human's cognition, the agent's context, and the loop between them.

```
                 THE SOCIO-TECHNICAL SYSTEM, taken whole
                 the human at the centre, augmented by agents
   ══════════════════════════════════════════════════════════════════════
   three lenses, present in every file, never a bin:
     H  what it does for the human's cognition
     C  what it does for the agent's context
     I  what it does to the loop between them
   ══════════════════════════════════════════════════════════════════════
   a general practice, read through the three            H          C          I
   ───────────────────────────────────────────────── ────────── ────────── ──────────
   atomic-commit     the smallest change that works   unit of     unit of    what
                                                      thought     a context  crosses
   zoom-levels       a message is a map               attention   tokens     the map
                                                      budget      (mirror)   as channel
   attractors        a term pulls what follows        a theory    a basin    a shared
                                                      named       carved     vocabulary
   three-layer-      know-how, doctrine, philosophy   what the    what       what loads
     harness                                          engineer    loads      when, for
                                                      holds                  whom
```

The three are lenses, felt in every file, never bins. A practice that existed before agents, small batches, trunk-based development, domain-driven design, is applied to both sides, and each file says what it did for a team and what it does for a context. Most of the software-development philosophy is about human cognition; that is the point. Sorting the files into three fails by design: every file is one practice, three readings, one system.

Read it like a book where you are the hero. Page one is [harness](harness.md). Then choose a path. Each carries one question into every file it visits, forks where another file answers it better, and says what you hold at the end.

## The human

*What does this do for my cognition, and why does it make my work with agents effective?*

1. [collaborative-production](collaborative-production.md): a model of the work is built only by taking part, so the agent belongs inside the loop as driver.
2. [transmission-belt](transmission-belt.md): remove the medium's load, transmit the domain's, friction included; the type grows on the friction that comes back.
3. [model-phenomenology](model-phenomenology.md): what I hold and the agent cannot, a type with a horizon; why the human stays central.
4. [conversation-as-interface](conversation-as-interface.md): the chat is my only medium, and I still go down to the files.
5. [embodied-navigation](embodied-navigation.md): thinking runs on spatial machinery; moving through code is how I think with it.
6. [mechanical-refactoring](mechanical-refactoring.md): moves cost no understanding, so understanding is spent only on the model.
7. [batch-slicing](batch-slicing.md): everything is a hypothesis; first an increment of value, then the steps that build it.
8. [compounding-decisions](compounding-decisions.md): decisions chain and their errors multiply; how many an artifact asks is a design quantity.
9. [metis-kairos](metis-kairos.md): what no level can absorb reaches me, and that arrival is the moment to improve.

Forks: after 4, [zoom-levels](zoom-levels.md), attention as the mirror of context economics; after 8, [model-tiers](model-tiers.md), cognitive energy is sparser than tokens.

Held at the end: I stay central because I hold what the agent cannot; the harness transmits the friction, and that is where I learn; every practice is sized to my attention.

## The context

*What does this do for the agent's context, and how does the harness's structure follow from it?*

1. [context-economics](context-economics.md): context is scarce and degrades; all harness structure derives from this.
2. [harness-elements](harness-elements.md): choosing an element is a loading decision first.
3. [compounding-decisions](compounding-decisions.md): the number of decisions an artifact asks is a design quantity, like the size of its context.
4. [context-splitting](context-splitting.md): two axes, the sub-agent as the unit of both.
5. [parse-dont-validate](parse-dont-validate.md): the spatial cut made inside the code; a signature is a call site's whole context.
6. [session-state-in-documents](session-state-in-documents.md): the conversation is process memory; the work file holds the state, the repo what graduated.
7. [attractors](attractors.md): what is in context pulls what comes next; the sharpest pull per token is a precise term, and a negation pulls too.
8. [collaborative-production](collaborative-production.md): interactive is the default; an artifact that runs alone is chosen, its waste counted in tokens, cognitive energy and time.
9. [agentic-trunk-based-development](agentic-trunk-based-development.md): between agents, the diff and never the conversation.
10. [agentic-extreme-programming](agentic-extreme-programming.md): a lean context keeps the top model affordable, which keeps the context lean.

Forks: at 2, [three-layer-harness](three-layer-harness.md), the layers by what each holds, then [harness-shape](harness-shape.md), how a rule or skill is built from them; at 7, [level-design](level-design.md), a file is a landscape, or [mechanical-refactoring](mechanical-refactoring.md), code is context.

Held at the end: context is scarce and degrades, so the harness is shaped by what loads and when; the work is cut in space and time; between steps a file crosses, between sub-agents a conclusion returns, never the conversation; the whole moves together.

## The practices

*Which practice is this, what did it do for a team, what does it become applied to both sides?*

1. [agentic-extreme-programming](agentic-extreme-programming.md): practices are complements; tokens, context, cognitive load, feedback move together.
2. [batch-size-economics](batch-size-economics.md): holding cost includes cognitive load; transaction cost can fall to near zero, so the optimum falls to the floor.
3. [atomic-commit](atomic-commit.md): the floor; validation, not generation, is the price.
4. [mechanical-refactoring](mechanical-refactoring.md): the epistemic action moves to the agent; a cleaning pass is context hygiene.
5. [trunk-based-development](trunk-based-development.md): commit = integrate = publish, the human-team form in full.
6. [agentic-trunk-based-development](agentic-trunk-based-development.md): the same bound, a worktree as a committer; nothing is added for agents.
7. [collaborative-production](collaborative-production.md): mob programming and strong-style driving; the agent is the driver.
8. [context-splitting](context-splitting.md): Beck's two hats and map-reduce applied to the context.
9. [kairos-gates](kairos-gates.md): a practice enters the loop as a step at its moment.
10. [harness-direction](harness-direction.md): a brick's path from steered in session to script, once reliable and reused.

Forks: at 4, [make-the-change-easy](make-the-change-easy.md) then [change-in-place](change-in-place.md); at 8, [parse-dont-validate](parse-dont-validate.md) then [always-valid-domain](always-valid-domain.md) and [aggregates](aggregates.md), the DDD entry.

Held at the end: each known practice keeps its bound and changes its holder; the agent takes the mechanical part, the human keeps the decision that changes the concept; a practice enters as a step at its moment; a brick made reliable and reused travels down to a script.

## The whole

*How do the human, the context and the loop hold together as one system?*

1. [collaborative-production](collaborative-production.md): the loop is the boundary of one extended mind.
2. [model-phenomenology](model-phenomenology.md): the engineer holds the type, the code the concept, the agent neither, and transmits; no part stands in for another.
3. [transmission-belt](transmission-belt.md): one rule, remove the medium's load and transmit the domain's; friction-feel is carried by no single part.
4. [abstraction-ladder](abstraction-ladder.md): one shape; every ladder in the corpus is a sighting.
5. [context-economics](context-economics.md): every token loaded is budget spent and precision lost; the human side of the same economy is the fork.
6. [agentic-extreme-programming](agentic-extreme-programming.md): a coherent set asks for no trade-off; feeling pulled between two sides is the test the set is not coherent.
7. [compounding-decisions](compounding-decisions.md): waste, what an element costs when it works, and reliability, the chance it does what was meant, are tied.
8. [parse-dont-validate](parse-dont-validate.md): one practice, three faces in the code itself: less to read, nothing to hold, no decision to take.
9. [embedded-reflexive](embedded-reflexive.md): embedded acts within its conditions, reflexive designs them; a breakdown is taken as deep as it goes, at the deepest into the engineer's own perception.

Forks: at 5, [zoom-levels](zoom-levels.md); at 8, [mechanical-refactoring](mechanical-refactoring.md) or [agentic-trunk-based-development](agentic-trunk-based-development.md).

Held at the end: one extended mind, type in the engineer, concept in the code, transmission in the agent; one rule and one shape run across all; the engineer does the reflexive work, as deep as the breakdown goes.

## The harness design

*How is the harness itself layered, written and improved, and where does a failed run change it?*

1. [harness-elements](harness-elements.md): a few kinds of element, each with one job: what it holds, when it loads, the test it is in the right place.
2. [process-units](process-units.md): process is a containment tree; the kind of unit at a node is how far its orchestrator's decisions are codified.
3. [abstraction-ladder](abstraction-ladder.md): the pattern itself, the process tree and the three layers two of its sightings: absorb low, pass the rest one rung up, reliable bricks move down.
4. [three-layer-harness](three-layer-harness.md): know-how, doctrine, philosophy; two seams, commodification below, lifecycle above.
5. [harness-shape](harness-shape.md): a rule or skill is a doctrine, a know-how, a pointer; the know-how covers the head, the doctrine the fat tail.
6. [attractors](attractors.md): what is in context pulls what comes next; a precise term carves the valley, a negation keeps the basin alive.
7. [field-terms](field-terms.md): a term references a theory and explains, a saying mentions a posture and prescribes; a doctrine line is looked for before it is written.
8. [level-design](level-design.md): an element is a landscape designed from where the reader stands; a section in doubt is probed on a fresh sub-agent.
9. [kaizen](kaizen.md): feedback from runs becomes changes at the lowest layer that can absorb the failure; most failures are compliance.
10. [harness-direction](harness-direction.md): a brick made reliable and reused moves down one rung, toward script and headless.

Forks: at 4, [change-inertia](change-inertia.md), cut where the inertia changes, the doctrine and the rationale pointer as the harness's seam; at 8, [embedded-reflexive](embedded-reflexive.md), the writer reflexive, the reader embedded; at 9, [metis-kairos](metis-kairos.md), what no level holds reaches the engineer; at 10, [model-tiers](model-tiers.md), a node that reaches commodity drops a tier.

Held at the end: the harness is a few elements, the agents among them materializing units of one process tree; process and knowledge are both ladders; a rule or skill is a doctrine that holds everywhere, a know-how for the usual case and a pointer to its reasons, written as the reader's landscape; a failed run lands at the lowest layer that absorbs it, and a brick made reliable and reused steps down toward the script.

Crossroads: collaborative-production is on four of the five paths, agentic-extreme-programming and compounding-decisions on three. Meeting one again, you stand where another path passes; change path if its question is now yours.
