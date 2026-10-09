# Model tiers

**Doctrine.** Default to the most intelligent model. Step down a tier only when the task carries no decision.

- **Top** (Opus class): anything with a decision, a concept, knowledge or design in it. Choosing what to build, judging, reviewing, conversing, reading documents for insight rather than facts.
- **Middle** (Sonnet class): execution without real decisions. The architecture and the spec are given; the model fits code to them. Automatic sub-agents that follow a workflow.
- **Small** (Haiku class): the extremely trivial. Commit messages. Mechanical sub-agents deployed in workflows to surface a piece of information.

**Why.** A tier below its task fails silently: the output looks like work done, and nothing says the decision was taken at the wrong level. A wrong decision executed cleanly costs more than the tokens saved.

Defaulting to intelligence is affordable for one reason: context economics. A short window on a top model costs less than a bloated one on a middle model, and decides better. The two doctrines hold each other up.

**When it fails.** When context is not economical. Long sessions, everything loaded, big windows: the top tier becomes unaffordable, cost wins the argument, and the default drifts down where it hurts most, on the decisions. People who default to cost are usually paying for context they did not need.

Names rotate; reason in tiers. Current names: Anthropic Opus / Sonnet / Haiku; OpenCode Sol / Terra / Luna.
