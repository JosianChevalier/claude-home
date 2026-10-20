```
   ·                                                       ✦    ·
   ████    ███   █   █  █  █████       ████    ███   █   █  ███   ████
   █   █  █   █  ██  █  █    █         █   █  █   █  ██  █   █   █
   █   █  █   █  █ █ █       █         ████   █████  █ █ █   █   █
   █   █  █   █  █  ██       █         █      █   █  █  ██   █   █
   ████    ███   █   █       █         █      █   █  █   █  ███   ████

                        in large, friendly letters
```

Far out in the uncharted backwaters of the unfashionable end of software engineering lies a small unregarded repository.

It contains a philosophy. This has made a lot of people very confused and been widely regarded as a bad move.

Should you wish to understand it anyway, it comes with a Guide: an agent that has read all of it so that you don't have to.

From a terminal, with Claude Code:

```sh
claude --agent philosophy-guide
```

From a session already open, Claude Code or opencode:

```
/philosophy-guide
```

## What this is

My personal harness: everything my coding agents load before they touch anything, and the reasoning behind it.

It is opinionated, on purpose: theory-informed practice. It is also alive: this is where my ideas land while they are still forming, so it keeps moving.

It is public because parts of it travel. A rule, a skill, an idea may serve you as it stands: take what helps.

## Structure

```
.
├── CLAUDE.md     ─┐
├── AGENTS.md      │
├── rules/         │   a normal agent harness, each piece in its usual place
├── skills/        │
├── agents/        │
├── commands/     ─┘
├── philosophy/        never loaded: the rationale behind everything above
└── widgets/           not harness: what I look at while using Claude Code (status line, quota chip)
```

Clone it as `~/.claude` for Claude Code, or as `~/.config/opencode` to make it your opencode configuration.

`settings.template.json` is a starting point for your own `settings.json`. Anything named `*.work.md` is work in progress.

## Philosophy

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

Read it like a book where you are the hero. Page one is [harness](philosophy/harness.md). Then choose a path. Each carries one question into every file it visits, forks where another file answers it better, and says what you hold at the end.

### The human

*What does this do for my cognition, and why does it make my work with agents effective?*

1. [collaborative-production](philosophy/collaborative-production.md): a model of the work is built only by taking part, so the agent belongs inside the loop as driver.
2. [transmission-belt](philosophy/transmission-belt.md): remove the medium's load, transmit the domain's, protect the germane; friction coming back is where understanding grows.
3. [model-phenomenology](philosophy/model-phenomenology.md): what I hold and the agent cannot, a type with a horizon; why the human stays central.
4. [conversation-as-interface](philosophy/conversation-as-interface.md): the chat is my only medium, and I still go down to the files.
5. [embodied-navigation](philosophy/embodied-navigation.md): thinking runs on spatial machinery; moving through code is how I think with it.
6. [mechanical-refactoring](philosophy/mechanical-refactoring.md): moves cost no understanding, so understanding is spent only on the model.
7. [batch-slicing](philosophy/batch-slicing.md): the step is the human's unit of thought; intent, not route.
8. [compounding-decisions](philosophy/compounding-decisions.md): decisions chain and weaken; the human is put on the ones that matter.
9. [metis-kairos](philosophy/metis-kairos.md): what no level can absorb reaches me, and that arrival is the moment to improve.

Forks: after 4, [zoom-levels](philosophy/zoom-levels.md), attention as the mirror of context economics; after 8, [model-tiers](philosophy/model-tiers.md), cognitive energy is sparser than tokens.

Held at the end: I stay central because I hold what the agent cannot; the harness transmits the friction, and that is where I learn; every practice is sized to my attention.

### The context

*What does this do for the agent's context, and how does the harness's structure follow from it?*

1. [context-economics](philosophy/context-economics.md): context is scarce and degrades; all harness structure derives from this.
2. [harness-elements](philosophy/harness-elements.md): choosing an element is a loading decision first.
3. [compounding-decisions](philosophy/compounding-decisions.md): a full context is not only costly, it is weaker.
4. [context-splitting](philosophy/context-splitting.md): two axes, the sub-agent as the unit of both.
5. [parse-dont-validate](philosophy/parse-dont-validate.md): the spatial cut made inside the code; a signature is a call site's whole context.
6. [session-state-in-documents](philosophy/session-state-in-documents.md): the conversation is process memory; the work file holds the state, the repo what graduated.
7. [attractors](philosophy/attractors.md): what a file does to a fresh context; it pulls, negation included.
8. [collaborative-production](philosophy/collaborative-production.md): posture is upstream of context; the human in the loop is the shortest chain.
9. [agentic-trunk-based-development](philosophy/agentic-trunk-based-development.md): between agents, the diff and never the conversation.
10. [agentic-extreme-programming](philosophy/agentic-extreme-programming.md): a lean context keeps the top model affordable, which keeps the context lean.

Forks: at 2, [three-layer-harness](philosophy/three-layer-harness.md) then [harness-shape](philosophy/harness-shape.md), loading policy by lifecycle; at 7, [level-design](philosophy/level-design.md), a file is a landscape, or [mechanical-refactoring](philosophy/mechanical-refactoring.md), code is context.

Held at the end: context is scarce and degrades, so the harness is shaped by what loads and when; the work is cut in space and time, and a file, never the conversation, crosses between contexts; the whole moves together.

### The practices

*Which practice is this, what did it do for a team, what does it become applied to both sides?*

1. [agentic-extreme-programming](philosophy/agentic-extreme-programming.md): practices are complements; tokens, context, cognitive load, feedback move together.
2. [batch-size-economics](philosophy/batch-size-economics.md): holding cost includes cognitive load; transaction cost falls to near zero, so the optimum falls to a floor.
3. [atomic-commit](philosophy/atomic-commit.md): the floor; validation, not generation, is the price.
4. [mechanical-refactoring](philosophy/mechanical-refactoring.md): the epistemic action moves to the agent; a cleaning pass is context hygiene.
5. [trunk-based-development](philosophy/trunk-based-development.md): commit = integrate = publish, the human-team form in full.
6. [agentic-trunk-based-development](philosophy/agentic-trunk-based-development.md): the same bound, a worktree as a committer; the purest before/after.
7. [collaborative-production](philosophy/collaborative-production.md): mob programming and strong-style driving; the agent is the driver.
8. [context-splitting](philosophy/context-splitting.md): Beck's two hats and map-reduce applied to the context.
9. [kairos-gates](philosophy/kairos-gates.md): a practice enters the loop as a step at its moment.
10. [harness-direction](philosophy/harness-direction.md): a practice's path from steered in session to script.

Forks: at 4, [make-the-change-easy](philosophy/make-the-change-easy.md) then [change-in-place](philosophy/change-in-place.md); at 8, [parse-dont-validate](philosophy/parse-dont-validate.md) then [always-valid-domain](philosophy/always-valid-domain.md) and [aggregates](philosophy/aggregates.md), the DDD entry.

Held at the end: each known practice keeps its bound and changes its holder; the agent takes the mechanical part, the human keeps the decision that changes the concept; a practice enters as a gate and travels down to a script.

### The whole

*How do the human, the context and the loop hold together as one system?*

1. [collaborative-production](philosophy/collaborative-production.md): the loop is the boundary of one extended mind.
2. [model-phenomenology](philosophy/model-phenomenology.md): the engineer holds the type, the code the concept, the agent neither; no part stands in for another.
3. [transmission-belt](philosophy/transmission-belt.md): one rule, remove the medium's load and transmit the domain's; friction-feel is carried by no single part.
4. [abstraction-ladder](philosophy/abstraction-ladder.md): one shape; every ladder in the corpus is a sighting.
5. [context-economics](philosophy/context-economics.md): one economy on two sides, tokens for the harness, cognitive load for the human.
6. [agentic-extreme-programming](philosophy/agentic-extreme-programming.md): a coherent set asks for no trade-off; feeling pulled between two sides is the test the set is not coherent.
7. [compounding-decisions](philosophy/compounding-decisions.md): waste, what an element costs when it works, and reliability, the chance it does what was meant, are tied.
8. [parse-dont-validate](philosophy/parse-dont-validate.md): one practice, three faces in the code itself: less to read, nothing to hold, no decision to take.
9. [embedded-reflexive](philosophy/embedded-reflexive.md): a breakdown climbs until the philosophy rewrites the engineer's own perception.

Forks: at 5, [zoom-levels](philosophy/zoom-levels.md); at 8, [mechanical-refactoring](philosophy/mechanical-refactoring.md) or [agentic-trunk-based-development](philosophy/agentic-trunk-based-development.md).

Held at the end: one extended mind, type in the engineer, concept in the code, transmission in the agent; one rule and one shape run across all; the system learns as one.

Crossroads: collaborative-production is on all four paths, agentic-extreme-programming and compounding-decisions on three. Meeting one again, you stand where another path passes; change path if its question is now yours.

## Ideas

- **Context is the scarce resource.** Every token loaded is budget spent and precision lost. All the structure follows from that: what loads always, what loads on trigger, what never loads.

- **Three layers.** Know-how codifies what worked. Doctrine is the boundary the agent improvises within when the know-how runs out. Philosophy is where the harness is heading, and stays out of the context.

- **A rule or a skill has one shape.** A doctrine, a know-how, then a pointer to its rationale in `philosophy/`. The reasons stay out of the file that loads.

- **Attractors.** What is in context pulls what comes next, and the sharpest pull per token is a precise term. A rule names the theory instead of explaining it.

- **Transmission belt.** The agent removes the load of the medium and transmits the load of the domain, friction included. I choose the concept; it handles the code.

- **The conversation is the interface.** I steer from the conversation alone, so every message is written for a reader with nothing else open.

- **State lives in documents.** A session can die at any moment. The state of a work lives in a work file, and the file dies with the work.

- **Subtraction.** The pull is to add and to keep. What is done is deleted; history is git's job.
