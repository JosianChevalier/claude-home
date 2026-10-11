# Application Layer in Hexagonal Architecture

> This bounded context uses an application layer to separate pure domain logic from side effects.

## What It Is

Sits between domain and adapters, orchestrating side effects while keeping the domain pure (Functional Core / Imperative Shell pattern).

## What It Is NOT

- **Not presentation** — no REST controllers, message listeners, CLI handlers (those are driving adapters)
- **Not business logic** — that belongs in the domain model

## What It Contains

- Repository interactions (loading/saving via driven ports)
- Transactions
- Event propagation and external calls
- Use case orchestration

## Rules

1. **Domain stays pure**: no direct SPI interaction from domain objects
2. **No business logic**: computations and rules belong in the domain
3. **Entry point for driving adapters**: left ports defined here, not on domain directly
4. **Thin orchestration**: coordinate, don't accumulate implicit business rules
