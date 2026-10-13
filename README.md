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
claude --agent theory-guide
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

## Ideas

- **Context is the scarce resource.** Every token loaded is budget spent and precision lost. All the structure follows from that: what loads always, what loads on trigger, what never loads.

- **Three layers.** Know-how codifies what worked. Doctrine is the boundary the agent improvises within when the know-how runs out. Philosophy is where the harness is heading, and stays out of the context.

- **A rule or a skill has one shape.** A doctrine, a know-how, then a pointer to its rationale in `philosophy/`. The reasons stay out of the file that loads.

- **Attractors.** What is in context pulls what comes next, and the sharpest pull per token is a precise term. A rule names the theory instead of explaining it.

- **Transmission belt.** The agent removes the load of the medium and transmits the load of the domain, friction included. I choose the concept; it handles the code.

- **The conversation is the interface.** I steer from the conversation alone, so every message is written for a reader with nothing else open.

- **State lives in documents.** A session can die at any moment. The state of a work lives in a work file, and the file dies with the work.

- **Subtraction.** The pull is to add and to keep. What is done is deleted; history is git's job.
