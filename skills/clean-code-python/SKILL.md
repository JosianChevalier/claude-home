---
name: clean-code-python
description: Writing or reviewing Python code. Clean code: functional flows, idiomatic implementation, behaviour packaged with its data, states as types.
---

# Clean code (Python)

## Doctrine

- Three tactical moves, in this order: the flow is designed functionally, implemented in idiomatic Python, packaged in objects.
- Functional core, imperative shell (Bernhardt): decisions are referentially transparent functions over immutable values; effects sit at the edge, in the function that orchestrates.
- Command-query separation (Meyer): a function returns a value or changes the world, never both.
- SLAP, always: one level of abstraction per function (Composed Method, Beck). The tool is extracting a function, never naming a variable.
- Intention-revealing interfaces (Evans): a reader digs into a function to see how, never to understand what.
- Stepdown rule: each layer reads as a coherent English sentence, like well-written prose (Booch).
- Pythonic: the comprehension and the generator carry the flow, the data model's protocols carry the syntax. A fluent chain exists where a domain object offers one, never rebuilt from `map`, `filter` and `lambda`.
- Tell, don't ask: behaviour lives on the object that owns the data; a collection with domain meaning is a class.
- Illegal states are unrepresentable: a state is a type, a transition returns the next state's type. The type checker, strict, is the compiler.
- Everything is immutable: a change returns a new instance.
- Object Calisthenics, loosely.

## Know-how

### Design: the functional flow

- A use case reads fetch, decide, apply: queries first, one pure decision, commands last. The decision takes values and returns values, testable without a double.
- A query is pure and returns; a command returns `None` and is named by its effect. A function that mutates its argument and returns it is split.
- Time, randomness and configuration enter as arguments, read once at the edge.
- Read aloud: "filter, sum, for" is implementation, "remove inactive, sum totals" is intent.
- A comment separating sections, or an "and" in the description, names the functions to extract. Bodies of one to five lines.
- Early return over nesting.

```python
# before
def process(customer_id: CustomerId) -> None:
    # Fetch current state
    orders = order_repository.find_pending(customer_id)
    payments = payment_repository.find_by_customer(customer_id)

    # Detect failed payments
    failed_payments = []
    for payment in payments:
        if payment.is_declined:
            failed_payments.append(FailedPayment.declined(payment))

    # Reconcile
    for order in orders:
        if any(failed.matches(order) for failed in failed_payments):
            order_repository.save(order.cancel())


# after
def process(customer_id: CustomerId) -> None:
    pending_orders = fetch_pending_orders(customer_id)
    failed_payments = fetch_failed_payments(customer_id)

    cancellations = reconcile(pending_orders, failed_payments)

    save_all(cancellations)
```

### Implement: idiomatic Python

- A comprehension holds one concept per clause: a named predicate, a named transform. Logic in a clause becomes a function; a second `for` or a second `if` becomes a second step, named.

```python
def missing_timestamps(expected: Timestamps, covered: frozenset[Instant], unit: Unit) -> tuple[Missing, ...]:
    return tuple(as_missing(timestamp, unit) for timestamp in expected if timestamp not in covered)
```

- A generator expression feeds a reducer directly, `sum`, `any`, `all`, `max`, `min`; no intermediate list, no accumulator loop.
- A `for` statement is for commands: its body is one call with an effect.
- A domain type joins the language through the data model: `__iter__`, `__len__`, `__contains__`, `__add__`, `__lt__`, so `timestamp in coverage`, `sum(prices, Euros.zero())`, `sorted(deadlines)` read as the domain. `@property` for a derived value, `@classmethod` for a named constructor, `Euros.of("12.50")`.
- `enumerate`, `zip`, `itertools.pairwise`, `itertools.batched`, unpacking: never an index.
- Partial application hides the syntax: a function returning a function, or `functools.partial`, gives a `key=` or a callback its domain name. A bare delegation, `key=attrgetter("due_date")`, stays inline.
- `match` destructures a union or a shape; `if` decides a boolean.
- A resource acquired and released is a context manager.
- Names: intent, in the domain's language; no abbreviation: `quantity`, `repository`. Arguments past the second are keyword-only.

### Package: behaviour with its data

- A value is a `@dataclass(frozen=True, slots=True)`; its collections are `tuple` and `frozenset`; a change goes through a method returning a new instance, `dataclasses.replace` inside it.
- A collection with domain meaning is a class wrapping a tuple, iterable, its queries returning its own type: the chain reads as the domain.

```python
@dataclass(frozen=True, slots=True)
class Orders:
    _orders: tuple[Order, ...]

    def __iter__(self) -> Iterator[Order]:
        return iter(self._orders)

    def pending(self) -> "Orders":
        return Orders(tuple(order for order in self if order.is_pending))

    def total(self) -> Euros:
        return sum((order.total for order in self), Euros.zero())


orders.pending().total()
```

- A function using the object's state or part of its public API is a method; a pure helper is a module-level function below the class, underscore-prefixed, the module being the privacy boundary.
- A service is a closure: context captured once, one behaviour returned. Several closures over the same context, calling each other or evolving together, are a class, the repository shape being the archetype. Never a module of unrelated functions, never a class of static methods.
- A dependency is a `Protocol`, declared by the consumer, in the consumer's words.
- A state is a frozen dataclass in a union. The transition a state lacks does not type-check; a consumer demands the one state it handles; a `match` over the union is exhaustive, closed by `assert_never`.

```python
@dataclass(frozen=True, slots=True)
class OrderReady:
    lines: OrderLines

    def cancel(self, at: Instant) -> "OrderCancelled":
        return OrderCancelled(self.lines, cancelled_at=at)

    def expedite(self, at: Instant) -> "OrderExpedited":
        return OrderExpedited(self.lines, expedited_at=at)


@dataclass(frozen=True, slots=True)
class OrderExpedited:
    lines: OrderLines
    expedited_at: Instant
    # no cancel(): an expedited order cannot be cancelled, the type checker says so


type Order = OrderReady | OrderExpedited | OrderCancelled


def process_order(order: OrderReady) -> ProcessOrderOutput: ...
```

- A value object is its own type, never a bare primitive: a frozen dataclass when it has behaviour (`Euros.add`), a `NewType` when it is id-like. It is always valid: the constructor or the named constructor parses, nothing downstream re-checks.
- Absence is modelled, `Price | None`, handled once by an early return or a `match`; never a sentinel value, never a required field filtered upstream.
- Errors: a union of outcome types for outcomes the caller decides on, matched exhaustively; a local `try`/`except` for local recovery, on the narrowest exception; `raise` for the unrecoverable. A project that already has a `Result` type uses it for recoverable flows.

Rationale: φservices-closures-first, φtypestate, φimmutability, φnominal-value-objects, φerror-ladder, φubiquitous-language
