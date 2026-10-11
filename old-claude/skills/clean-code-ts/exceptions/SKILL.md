---
name: clean-code-ts:exceptions
description: Use when handling failures in TypeScript — choosing between tagged union returns, Result railway, local try-catch, and throw.
---

# Error Handling Ladder

Failure handling is a design decision, not a reflex. Pick the lowest rung that fits. Aligned with @rules/exception-strategy.md: **if the caller must react, make failure visible in the type system; if not, let it propagate.**

## 1. Tagged Union Return — outcomes the caller decides on

When failure is a *domain outcome* the caller inspects and acts upon, return it as data.

```ts
export type ProcessOrderOutput =
  | { result: 'SUCCESS'; events: ProcessingEvents }
  | { result: 'FAILURE'; events: ProcessingEvents; cause: string };

export type InvalidPrice =
  | { type: 'EMPTY_ORDER'; cause: string }
  | { type: 'INVALID_PRICE'; cause: string }
  | { type: 'UNKNOWN_PRODUCT_TYPE'; cause: string };
```

Match exhaustively on the discriminant; `assertNever` makes new cases fail to compile:

```ts
switch (error.type) {
  case 'EMPTY_ORDER': return ...;
  case 'INVALID_PRICE': return ...;
  case 'UNKNOWN_PRODUCT_TYPE': return ...;
  default: return assertNever(error);
}

function assertNever(value: never): never {
  throw new Error(`Unreachable: ${JSON.stringify(value)}`);
}
```

## 2. Railway (`Result`) — recoverable failures in a flow

When a multi-step transformation can fail midway and later steps must be skipped, compose with `Result.map`/`flatMap` — the first failure short-circuits, and the error type is part of the signature.

```ts
fullPrice(): TotalPriceResult {
  return Result.success(this.orderLines)
    .flatMap(validateNonEmpty)
    .map(mapArray(addVat))
    .flatMap(Result.combine)
    .flatMap(ensureHigherThan(this.deliveryFees))
    .valueOrError();
}
```

Use it when it's cheaper than try-catch at every step — almost always true once the flow has more than two failure points.

## 3. Local try-catch — recovery is local and imperative

When the recovery logic lives right next to the risky call and the surrounding code is already imperative, a local try-catch is simpler than threading a `Result` through.

```ts
function parseCachedRates(raw: string): TaxRates {
  try {
    return taxRates(JSON.parse(raw));
  } catch {
    return DEFAULT_TAX_RATES;   // recovery is one line, right here
  }
}
```

Do **not** let a try-catch interrupt a functional pipeline with imperative logic — that's rung 2's job.

## 4. Throw — unrecoverable

Bugs, broken invariants, unreachable states: throw and let it propagate to the boundary (the left adapter translates to HTTP 500, NACK, etc.). The domain never catches these.

```ts
class BatteryLevel {
  constructor(readonly value: number) {
    if (value < 0 || value > 100) throw new Error(`Battery level must be 0-100, got ${value}`);
  }
}
```

## Checklist

1. Caller decides on the outcome? → tagged union return
2. Multi-step flow with recoverable failure? → `Result` railway
3. One-line local recovery amid imperative code? → local try-catch
4. No recovery possible? → throw; never catch it in the domain

Rationale: @rationale/error-ladder.md
