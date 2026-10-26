---
tags: [ddd, feedback-loops, hexagonal-architecture]
---

# Domain-first implementation

**Thesis.** Driving from the domain, the engineer is the domain's first consumer; every exposure after that is chosen for the feedback it gives, and dependency inversion is what makes the exposure a choice.

Driving from the domain (DDD), the first feedback an engineer gets is the domain expressed: whether the model holds with conceptual integrity or shows tensions ([[philosophy/model-phenomenology]]). The domain's first consumer is the engineer, at once. Its tests, written as the domain asks for them (TDD, Cooper's reading: at the use-case boundary), bring the fake driven adapters with them: domain and fakes grow entangled.

From there each step exposes the domain to the next consumer that can answer a question, and no further:

1. **Domain and fakes.** Consumer: the engineer. Answers whether the model holds.
2. **Dark path.** An undocumented endpoint, a path open to chosen users. Consumer: us, chosen users. Answers whether it runs where it lives.
3. **End-user consumable**, when useful: a front for stakeholders, an API for another team to test their flow, a CLI. Consumer: stakeholders, another team. Answers whether the behavior is right.
4. **The rest plugged.** Consumer: everyone.

A whole project can run as a CLI with no database until its algorithms are validated. Hexagonal architecture, dependency inversion, is what makes each exposure a choice: the domain does not know which adapter drives it. The outer loops, from deployment to the domain: [[philosophy/feedback-loops]].

Releasability, the live path and the keystone: [[philosophy/continuous-delivery]].
