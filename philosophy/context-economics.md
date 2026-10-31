---
tags: [harness-design, context-economics, cohesion, sub-agents]
---

# Context economics

**Thesis.** Context is the scarce resource. Every token loaded is budget spent and precision lost. All harness structure derives from this constraint.

Degradation is gradual, with a soft limit that depends on the model class:

| Model class | Soft limit |
|---|---|
| Sonnet / terra | 50k tokens |
| Opus / sol | 80k tokens |
| Fable / astra | 100k tokens |

About 20k past the soft limit, output is considered really unreliable.

The same economy on the human side, the user's cognitive load, is another subject: φzoom-levels.

## Techniques

Each one exists to keep something *out* of some window. Three attack the size of the harness, one what loads from it, two what one context holds.

### Fewer things exist

**Rework over adding.** Under pressure, the cheap local move is to *add*: a new file, a new rule, a new caveat. Each addition costs forever (loaded in every relevant session), compounds (more files → more contradictions → more meta-rules to arbitrate), and is never garbage-collected on its own. Hence **rework > adding**: the default fix is editing or deleting existing material; creating something new requires demonstrating no existing home fits.

**One canonical home per fact.** Every piece of knowledge has exactly one home; anything else may only point to it, never copy it (Pierrain: "pointers, not copies"). Duplicates diverge inevitably, and reconciling diverging sources costs more than the copy ever saved. This is why the harness has no memory files, why completed plan stages collapse to pointers at commits, and why philosophy files reference each other instead of restating.

**Cohesion.** One concept per rule file, cohesive files. The payoff is at harness-improvement time: a fix should require reading and editing exactly one file. Monoliths force loading everything to change anything, the exact failure the architecture exists to prevent.

### Fewer of them load

**Loading policy.** Loading is a policy, not a taxonomy: personal and unscoped project rules are the only always-on cost; scoped rules inject when a touched file matches their path pattern; skills load on invocation; philosophy loads only during harness work. What each element is for: φharness-elements.

### What loads is divided across contexts

**Sub-agents.** Sub-agents are context firewalls: delegate exploratory or high-volume work so its tokens die with the sub-agent, returning only conclusions. This is near-decomposability (Simon): each node absorbs its own variety, and the orchestrator faces only what leaks out (φabstraction-ladder).

**Context splitting.** When one context is too much, it is cut along two axes, space and time, and a cut on one axis opens the way on the other: φcontext-splitting.

## Related

- The same economy on the human side: φzoom-levels.
- How a context is cut: φcontext-splitting.
- What each harness element loads: φharness-elements.
