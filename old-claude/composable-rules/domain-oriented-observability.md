# Domain Oriented Observability

Domain logic declares instrumentation SPIs (observation points). Infrastructure implements them with concrete logging/metrics.

Based on [Domain-Oriented Observability](https://martinfowler.com/articles/domain-oriented-observability.html).

## Pattern

1. Domain defines an `*Instrumentation` SPI with methods named after **domain events** (e.g. `discountApplied()`, `deviceBecameUnreachable()`)
2. Infrastructure provides concrete implementations (logging, metrics, Datadog, etc.) — domain doesn't know or care which

## Rules

- Domain MUST NOT depend on observability frameworks
- Instrumentation methods describe **domain events**, not technical operations (no `logError()`, `incrementCounter()`)
