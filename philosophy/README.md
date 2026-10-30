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

Read it like a book where you are the hero. Page one is [harness](harness.md). Then pick a walk. Each carries one question into every file it visits, forks where another file answers it better, and says what you hold at the end.

```
┌──────────────────────────────────────────┐  ┌──────────────────────────────────────────┐
│ 1  GETTING STARTED                       │  │ 2  IMPROVING A HARNESS                   │
│    "I want to get started. Where?"       │  │    "I already run agents. What do I      │
│                                          │  │     change?"                             │
│    ○─○─○─○─◉            5 stops · short  │  │    ○─○─○─○─○─○─○─◉      8 stops · steady │
│    from  the harness, shown              │  │    from  context is scarce and degrades  │
│    to    the agent inside the loop,      │  │    to    a failed run becomes a change   │
│          as driver                       │  │          at the lowest layer             │
└──────────────────────────────────────────┘  └──────────────────────────────────────────┘
┌──────────────────────────────────────────┐  ┌──────────────────────────────────────────┐
│ 3  WHAT IS DIFFERENT                     │  │ 4  THE HUMAN                             │
│    "What's different here from the       │  │    "What does this do to how I think,    │
│     usual way?"                          │  │     and what stays mine?"                │
│    ○─○─○─○─○─○─◉        7 stops · steady │  │    ○─○─○─○─○─○─○─◉      8 stops · long   │
│    from  the agent belongs in the loop   │  │    from  a model is built only by        │
│    to    the diff crosses, never the     │  │          taking part                     │
│          conversation                    │  │    to    what no level absorbs reaches   │
│                                          │  │          you                             │
└──────────────────────────────────────────┘  └──────────────────────────────────────────┘
```

## Getting started

*I want to get started. Where?*

1. [harness](harness.md): the harness serves one socio-technical system, the human at the centre; it does not control it, it shapes constraints so the whole tends toward the purpose.
2. [harness-elements](harness-elements.md): a few kinds of element, each with one job: what it holds, when it loads, the test it is in the right place.
3. [three-layer-harness](three-layer-harness.md): know-how, doctrine, philosophy; a rule or skill is a doctrine, a know-how, a pointer to its reasons.
4. [session-state-in-documents](session-state-in-documents.md): the conversation is process memory; the work file holds the state, the repo what graduated.
5. [collaborative-production](collaborative-production.md): a model of the work is built only by taking part, so the agent belongs inside the loop as driver.

Forks: at 3, [harness-shape](harness-shape.md), how a rule or skill is built from the layers; at 4, [conversation-as-interface](conversation-as-interface.md), the chat is the only medium, and you still go down to the files.

Held at the end: what the pieces are, where each thing lives, how a session runs and ends, and that you drive from inside the loop.

## Improving a harness

*I already run agents. What do I change?*

1. [context-economics](context-economics.md): context is scarce and degrades; all harness structure derives from this.
2. [harness-elements](harness-elements.md): choosing an element is a loading decision first.
3. [context-splitting](context-splitting.md): two axes, space and time, the sub-agent as the unit of both.
4. [attractors](attractors.md): what is in context pulls what comes next; the sharpest pull per token is a precise term, and a negation pulls too.
5. [session-state-in-documents](session-state-in-documents.md): the conversation is process memory; the work file holds the state, the repo what graduated.
6. [compounding-decisions](compounding-decisions.md): decisions chain and their errors multiply; how many an artifact asks is a design quantity.
7. [kaizen](kaizen.md): feedback from runs becomes changes at the lowest layer that can absorb the failure; most failures are compliance.
8. [harness-direction](harness-direction.md): a brick made reliable and reused moves down one rung, toward script and headless.

Forks: at 2, [three-layer-harness](three-layer-harness.md) then [harness-shape](harness-shape.md), the layers and how a rule or skill is built from them; at 4, [field-terms](field-terms.md), a term references a theory, a saying prescribes, or [level-design](level-design.md), a file is a landscape designed from where the reader stands; at 6, [parse-dont-validate](parse-dont-validate.md), the cut made inside the code, then [agentic-extreme-programming](agentic-extreme-programming.md), [batch-size-economics](batch-size-economics.md), [atomic-commit](atomic-commit.md), [agentic-trunk-based-development](agentic-trunk-based-development.md), the practices that keep a change small and a context lean; at 7, [metis-kairos](metis-kairos.md), what no level holds reaches the engineer, or [model-tiers](model-tiers.md), a node that reaches commodity drops a tier; at 8, [process-units](process-units.md) and [abstraction-ladder](abstraction-ladder.md), process as a containment tree, one ladder among many.

Held at the end: context is scarce and degrades, so the harness is shaped by what loads and when; the work is cut in space and time; between sub-agents a conclusion returns, never the conversation; a failed run lands at the lowest layer that absorbs it, and a brick made reliable and reused steps down toward the script.

## What is different

*What's different here from the usual way?*

1. [collaborative-production](collaborative-production.md): interactive is the default; an artifact that runs alone is chosen, its waste counted in tokens, cognitive energy and time.
2. [context-economics](context-economics.md): every token loaded is budget spent and precision lost; nothing is remembered for the agent, everything is loaded on purpose.
3. [transmission-belt](transmission-belt.md): one rule, remove the medium's load and transmit the domain's, friction included.
4. [model-phenomenology](model-phenomenology.md): the engineer holds the type, the code the concept, the agent neither, and transmits; no part stands in for another.
5. [agentic-extreme-programming](agentic-extreme-programming.md): a coherent set asks for no trade-off; feeling pulled between two sides is the test the set is not coherent.
6. [model-tiers](model-tiers.md): a lean context keeps the top model affordable, which keeps the context lean; cognitive energy is sparser than tokens.
7. [agentic-trunk-based-development](agentic-trunk-based-development.md): the same bound as for a team, a worktree as a committer; between agents, the diff and never the conversation.

Forks: at 2, [session-state-in-documents](session-state-in-documents.md), where state lives instead of a memory; at 4, [abstraction-ladder](abstraction-ladder.md), one shape, every ladder in the corpus a sighting; at 5, [compounding-decisions](compounding-decisions.md), waste and reliability tied, or [embedded-reflexive](embedded-reflexive.md), a breakdown taken as deep as it goes; at 7, [trunk-based-development](trunk-based-development.md), the human-team form in full.

Held at the end: the human stays central and the agent drives; context is the scarce thing and nothing is remembered on its behalf; one top model on a lean context; one rule and one shape run across all; the diff crosses between agents, never the conversation.

## The human

*What does this do to how I think, and what stays mine?*

1. [collaborative-production](collaborative-production.md): a model of the work is built only by taking part, so the agent belongs inside the loop as driver.
2. [model-phenomenology](model-phenomenology.md): what I hold and the agent cannot, a type with a horizon; why the human stays central.
3. [transmission-belt](transmission-belt.md): remove the medium's load, transmit the domain's, friction included; the type grows on the friction that comes back.
4. [embodied-navigation](embodied-navigation.md): thinking runs on spatial machinery; moving through code is how I think with it.
5. [conversation-as-interface](conversation-as-interface.md): the chat is my only medium, and I still go down to the files.
6. [mechanical-refactoring](mechanical-refactoring.md): moves cost no understanding, so understanding is spent only on the model.
7. [zoom-levels](zoom-levels.md): a message is a map; attention is the budget, and the map is the channel.
8. [metis-kairos](metis-kairos.md): what no level can absorb reaches me, and that arrival is the moment to improve.

Forks: at 6, [make-the-change-easy](make-the-change-easy.md) then [change-in-place](change-in-place.md), how a step is made small and kept live, or the model in code, [ubiquitous-language](ubiquitous-language.md), [model-expressions](model-expressions.md), [always-valid-domain](always-valid-domain.md), [aggregates](aggregates.md), [continuous-design](continuous-design.md), [domain-first-implementation](domain-first-implementation.md); at 7, [batch-slicing](batch-slicing.md), everything is a hypothesis, then [feedback-loops](feedback-loops.md), [planning-is-everything](planning-is-everything.md), [prototypes-are-probes](prototypes-are-probes.md), [continuous-delivery](continuous-delivery.md), the loops a hypothesis is tested in; at 8, [embedded-reflexive](embedded-reflexive.md), the reflexive work is mine, as deep as the breakdown goes.

Held at the end: I stay central because I hold what the agent cannot; the harness transmits the friction, and that is where I learn; every practice is sized to my attention, and the moment that reaches me is where the harness improves.

Crossroads: collaborative-production is on all four walks, context-economics, session-state-in-documents, model-phenomenology, transmission-belt and harness-elements on two. Meeting one again, you stand where another walk passes; change walk if its question is now yours.
