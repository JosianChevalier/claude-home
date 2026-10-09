---
tags: [harness-design, context-economics, cohesion, sub-agents]
---

# Rationale: Context Economics

Context is the scarce resource. Every token loaded is budget spent and precision lost. Degradation is gradual, with a soft limit that depends on the model class:

| Model class | Soft limit |
|---|---|
| Sonnet / terra | 50k tokens |
| Opus / sol | 80k tokens |
| Fable / astra | 100k tokens |

About 20k past the soft limit, output is considered really unreliable. All harness structure derives from this constraint.

The same economy on the human side, the user's cognitive load, is another subject: [[philosophy/zoom-levels]].

## Additivity bias

Under pressure, the cheap local move is to *add*: a new file, a new rule, a new caveat. Each addition costs forever (loaded in every relevant session), compounds (more files → more contradictions → more meta-rules to arbitrate), and is never garbage-collected on its own. Hence **rework > adding**: the default fix is editing or deleting existing material; creating something new requires demonstrating no existing home fits.

## One canonical home per fact

Every piece of knowledge has exactly one home; anything else may only point to it, never copy it (Pierrain: "pointers, not copies"). Duplicates diverge inevitably, and reconciling diverging sources costs more than the copy ever saved. This is why the harness has no memory files, why completed plan stages collapse to pointers at commits, and why philosophy files reference each other instead of restating.

## Cohesion

One concept per rule file, cohesive files. The payoff is at harness-improvement time: a fix should require reading and editing exactly one file. Monoliths force loading everything to change anything — the exact failure the architecture exists to prevent.

## Two axes

A context is spent along two axes.

- **Spatial: the blast radius.** The size of the input and output one context works with. Signals: a full codebase, a wide search, a whole PDF or a long document read in one go, a large generated output.
- **Temporal: the run.** Two things grow with it. Different types of operation require different skills (the two hats of TDD), so a context that changes hats carries the harness of each one (rules, skills, agent prompt). And each successive operation takes context in turn, through the tokens of running it. Signals: reading, planning and acting in the same context; a long-lived process; a session that carries many steps before anyone looks.

The two multiply. A large input read by a context that then plans and acts on it pays for the input at every later step.

## Cutting, and why a cut enables the next

**Spatial cut.** Modularise, and think map-reduce (Dean & Ghemawat): an orchestrator hands each slice to a sub-agent, each returns only its conclusion, the orchestrator reduces. The slices' tokens die with the sub-agents.

**Temporal cut.** Two hats (Beck), one at a time. One hat per context: each step runs in its own sub-agent, loaded with that step's harness only, and hands over through a file ([[philosophy/session-state-in-documents]]).

The two are not alternatives tried in sequence. A cut on one axis can open the way for a cut on the other. It is like the puzzle games where you have to turn the puzzle around to find the next piece to move, or a meshwork where you have to undo along one dimension before you can attack the other.

- *A scientific paper as a PDF.* An agent cannot easily split it by meaning, so the spatial cut is hard. Cut in time first: (1) convert to markdown, (2) read and process. Between the two there is now room for a step that cuts the text section by section. **The temporal cut enabled the spatial one.** Sections, once they exist, can be scheduled: read every chapter in parallel, summarise, then compare the summaries with the paper's own conclusion. **The spatial cut enabled new temporal ones.**
- *A feature changed across a codebase.* Too much for one context. Cut in space first: change module by module, keeping backward compatibility. That allows an order: start in the core domain, validate there, then propagate to the adapters and the consuming bounded contexts. **The spatial cut enabled the temporal one.**

So when one axis resists, the question is not "how do I cut harder here" but "which cut on the other axis would free this one".

**Escalation.** When orchestration itself becomes too complex for an agent to hold, the intermediate steps move to code: a script that calls agents headless and owns the control flow. It is deterministic where an orchestrating agent decides ([[philosophy/compounding-decisions]]).

**Where to stop.** Two limits.

- *Indivisibility.* If you cannot split, change axis and state what you see on that one. If you still cannot, you have probably reached the bottom.
- *Cost.* Each cut costs a handover and a coordination step. Stop where the context stays workable and the next cut would not pay for itself.

Pushing the cuts all the way to the bottom is the spirit of XP, but we do not do it in every harness.

## Loading policy

Loading is a policy, not a taxonomy: personal and frontmatter-less project rules are the only always-on cost; scoped rules inject deterministically when a touched file matches their `globs:`; skills load on invocation; philosophy loads only during harness work. Each mechanism exists to keep something *out* of some window. What each element is for: [[philosophy/harness-elements]].

## Rule → context (the AOP decision)

Scoped loading inverted from context-pulls-rules (per-subdomain AGENTS.md with refs) to rule-declares-context (`globs:` frontmatter, injected by the `opencode-rules` plugin). This is aspect-oriented programming's model — rules as aspects, globs as pointcuts — chosen for **determinism** (plugin hooks, not LLM judgment; survives compaction) and **free sharing** (one file, N globs). The accepted cost is AOP's classic one, **obliviousness**: a folder no longer self-describes its governing rules. Mitigation: the plugin's TUI sidebar shows which rules are active. If the plugin breaks or opencode ships native nested-AGENTS.md discovery, revisit this decision — the prior prose-wiring design is in git history.

## Sub-agents

Sub-agents are context firewalls: delegate exploratory or high-volume work so its tokens die with the sub-agent, returning only conclusions.

They are the unit of both cuts. On the spatial axis, one sub-agent per slice of the input. On the temporal axis, one sub-agent per workflow step, composed with only that step's skills and context (TDD → test-writer, green implementor, refactorer). Skills are composable because this composition is deterministic — the agent definition declares what loads.
