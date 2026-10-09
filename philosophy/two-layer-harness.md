---
tags: [harness-design, kaizen]
---

# Rationale: The Two-Layer Harness

## The layers

- **Layer 1 — prescriptive**: rules, skills, AGENTS.md. Terse, decision-only, always cheap to load. Business as usual runs on this layer exclusively.
- **Layer 2 — rationale** (`rationale/`): larger documents explaining *why and how* the prescriptions came to be. Loaded only when improving the harness.

This is design rationale in the Rittel/Kunz (IBIS) lineage — the same insight behind ADRs: a decision and its argumentation have different lifecycles and different readers. Executing a decision needs only the decision; *changing* it requires the argumentation, or you re-litigate solved problems and silently break the reasoning that made the rule coherent.

## The contract

1. Layer-1 files may end with `Rationale: @rationale/<concept>.md`. These refs are never loaded greedily; the harness-improvement skill loads them at its step 1.
2. The `harness-improvement` skill MUST load the rationale behind any rule or skill it touches before diagnosing.
3. **Drift guard**: if a proposed fix contradicts its rationale, either the fix is wrong or the rationale is outdated — one of the two must change, explicitly. This clause is the only mechanism keeping layer 2 honest; never bypass it.

## Why kaizen is user-invoked

Feedback is noted in-flow but processed on explicit invocation ("kaizen"): agent-side triggers for "session end" are undecidable, and mid-session processing interrupts work and pollutes task context with harness context. The transcript itself carries the notes across compaction.
