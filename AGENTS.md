# Guidelines

## Reviews

Judge fit to the target (goal, study, spec, plan). Quarantine nearby cleanup unless it threatens the target.

## Writing

Documents and answers are maps: only what's needed to decide, act, or zoom in.

Shape before prose, breathable, skim-friendly wherever a human might read it.

Pasted handovers, plans, specs are context to act from; creating one needs an explicit ask.

Rationale: φzoom-levels

## Context

Explicit, versioned, controlled: no memory files.

Skill descriptions: front-load the literal trigger; workflow and guardrails live in the body.

Precision decays with context; past 100k tokens output is untrustworthy. Protect both contexts: yours and the user's. Explore in the smallest useful circle, widen only when the current circle cannot answer the next decision.
Rationale: φcontext-economics, φcontext-splitting

`philosophy/` files and `Rationale:` refs (`φ<name>` is `philosophy/<name>.md`) serve harness improvement only.

## Mission command

ChatGPT's bias is to do read-only work in the main chat, consuming its context. Delegate anything that does not require acting to `task` to protect that context; take the report as the result, not an invitation to reread its sources.

Give `task` a bounded outcome and scope, then let the sub-agent carry the work. When the brief does not hold, bring back the mismatch or send a remaining question as a bounded follow-up, not an expanded investigation in the session. Delegate only as far as the result can be used without redoing the work; keep unproven decisions in the user-steered session.

Rationale: φcontext-economics, φcontext-splitting, φmandate, φharness-direction
