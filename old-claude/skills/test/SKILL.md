---
name: test
description: Use when running tests, writing new tests, or reviewing test structure and conventions.
---

# Test

## Running Tests

```bash
# Run all tests
mvn test

# Run single test class
mvn test -Dtest="CustomerOrderHistoryTest"

# Run single test method
mvn test -Dtest="CustomerOrderHistoryTest#testMethodName"

# Run nested test class
mvn test -Dtest="CustomerOrderHistoryTest$NestedClassName"
```

## Test Structure

### Class Naming

**Pattern:** `<ClassUnderTest>Test`

```kotlin
// Good
class CustomerOrderHistoryTest { }
class PaymentMonitorTest { }

// Bad
class TestCustomerOrderHistory { }
class CustomerOrderHistoryTests { }  // plural
```

### Nested Test Classes

Use **nested test classes** to organize related tests by feature or scenario.

```kotlin
class PaymentMonitorTest {

    @Nested
    inner class WhenCheckingPayments {

        @Test
        fun it_cancels_order_when_payment_is_declined() {
            val monitor = PaymentMonitor(stubRepository)
            val customerId = CustomerId("customer-1")

            val result = monitor.checkPayments(customerId)

            assertThat(result.hasCancelledOrder()).isTrue()
        }
    }

    @Nested
    inner class WhenShippingOrders {
        // More tests...
    }
}
```

### Method Naming

Use **snake_case** descriptive phrases focusing on behavior:

```kotlin
@Test
fun returns_true_when_cart_has_invalid_items() { }

@Test
fun throws_exception_when_payment_method_not_found() { }

@Test
fun ships_order_when_payment_is_confirmed() { }
```

### Test Quality

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | One thing. "and" in name? Split it. | `validates_email_and_domain_and_whitespace` |
| **Clear** | Name describes behavior | `test1` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |

## Arrange-Act-Assert (AAA) Pattern

Structure all tests with clear AAA sections, separated by empty lines.

One empty line when sections are small:

```kotlin
@Test
fun it_offers_free_shipping_when_total_above_threshold() {
    val threshold = 30.0
    val policy = ShippingPolicy(threshold)

    val result = policy.evaluate(35.0)

    assertThat(result.isShippingFree()).isTrue()
    assertThat(result.shippingMethod()).isEqualTo(ShippingMethod.EXPRESS)
}
```

Two empty lines when sections contain internal empty lines:

```kotlin
@Test
fun it_offers_free_shipping_when_total_above_threshold() {
    val policy = aShippingPolicy()
            .withThreshold(30.0)
            .build()
    // ... more lines of shipping policy logic

    orderStore().hasExistingOrdersCount(3)
    //... other lines of order store logic


    val result = policy.evaluate(total)


    assertThat(result.isShippingFree()).isTrue()
    assertThat(result.shippingMethod()).isEqualTo(ShippingMethod.EXPRESS)
}
```

## AssertJ Assertions

Use **AssertJ** for all assertions (not JUnit assertions).

```kotlin
import org.assertj.core.api.Assertions.assertThat
import org.assertj.core.api.Assertions.assertThatThrownBy

// Good - AssertJ
assertThat(result).isNotNull()
assertThat(orders).hasSize(3)
assertThat(order.status()).isEqualTo(OrderStatus.PENDING)

// Good - exception assertions
assertThatThrownBy { service.process(null) }
    .isInstanceOf(IllegalArgumentException::class.java)
    .hasMessage("CustomerId cannot be null")

// Bad - JUnit assertions
assertEquals(3, orders.size)
assertTrue(result != null)
```

## Test Utilities

### Stubs

Place stub implementations in the `domain/spi/` package with the `@Stub` annotation. Make them behave like real implementations (e.g., repository using an array instead of database).

```kotlin
@Stub
class StubOrderRepository : OrderRepository {
    // In-memory implementation for testing
}
```

### Builders

Use builders from `utils/Builders.kt` for creating test data.

```kotlin
val order = anOrder()
    .withCustomerId(customerId)
    .withShippingMethod(ShippingMethod.EXPRESS)
    .withStatus(OrderStatus.PENDING)
    .build()
```

### @TestToImplement Annotation

Replaces `@Test` to mark tests declared but not yet implemented. Auto-disables the test and suppresses warnings for empty methods/missing assertions.

Use to list test cases for later implementation, or during the RED phase of TDD.

### Test Discovery Workflow

When implementing a new component via TDD:
1. Write initial test cases as `@TestToImplement` stubs
2. Implement one test at a time (RED → GREEN)
3. Discover new cases during implementation, add as stubs
4. At the end, consolidate: keep useful tests, discard redundant ones

### Clock Injection

For time-based tests, inject a `Clock` and control time:

```kotlin
@Test
fun it_cancels_order_after_payment_delay() {
    val clock = Clock.fixed(Instant.parse("2025-01-01T10:00:00Z"), ZoneOffset.UTC)
    val service = OrderService(repository, clock)

    // Act & Assert with controlled time
}
```

## Test Data Naming

Test data should read like a domain scenario, not programmer shorthand.

### Time Constants

Name instants like a schedule: `_00h00`, `_00h30`, `_01h00`.
Name periods like calendar entries: `januaryFirst`, `marchThird`.

### Domain IDs

Use realistic domain names: `product_1`, `warehouse_A`, `customer_alice`.
Not: `p1`, `w1`, `c1`, `id1`, `testId`.

### Static Imports

Statically import factory methods and constants used in test data: `parse`, `eur`, enum values, etc. Test lines should read like domain sentences, not qualified Java.

```java
// BAD
Instant.parse("2025-01-01T10:00:00Z")
ShippingMethod.EXPRESS
Money.eur(100)

// GOOD
import static java.time.Instant.parse;
import static com.example.ShippingMethod.EXPRESS;
import static com.example.Money.eur;

parse("2025-01-01T10:00:00Z")
EXPRESS
eur(100)
```

## Readability

Tests ARE the example mapping, written directly in code. A non-technical team member should read a test body and understand the business rule being verified.

### 1. No Type Unpacking in Helper Calls

Builders and helpers must accept domain types directly. If you need `.toString()`, `.getValue()`, or any accessor to satisfy a helper signature, **overload the helper**.

```java
// BAD — leaks implementation, breaks the sentence
aCustomer().identified(alice.customerId().toString())

// GOOD — reads as a specification
aCustomer().identified(alice)
```

When adding a builder method, provide both overloads — primitive delegates to domain type:

```java
public CustomerBuilder identified(CustomerId id) { ... }
public CustomerBuilder identified(String id) { return identified(new CustomerId(id)); }
```

### 2. Factory Methods Use Indefinite Articles

```java
aCustomerId(), aProductId(), aProduct(), anOrder(), aCustomer()
```

### 3. Variables Carry Scenario Intent

Name after the **role in the scenario**, not the type.

```java
// BAD
var c1 = aCustomerId();
var p1 = aProductId();

// GOOD
var alice = aCustomerId();
var productInStock = aProductId();
```

### 4. Mock Setup Reads Like Given Clauses

```java
catalogService.havingProducts(product);
inventoryService.havingStockFor(productInStock, new StockEntry(AVAILABLE));
paymentService.willReturnNothing();
```

Fluent chaining for multiple conditions:

```java
having.forCustomer(ACME)
    .card("4111-1111-1111-1111").declined()
    .card("5555-5555-5555-4444").accepted();
```

### 5. Builders Read Like Descriptions

```java
anOrder().placedBy(alice)
    .with(aProduct().identified(productOutOfStock))
    .with(aProduct().identified(productInStock))
```

### 6. Reuse Variables Across Related Setup Calls

When the same value appears in multiple test setup calls, extract it to a named variable. Duplication obscures the relationship between setup steps. Add **overloads** to helpers/builders if needed to accept the extracted type.

```java
// BAD — same instant duplicated, relationship hidden
createStockCount("2025-01-01T10:30:00Z", 200)
createSale("2025-01-01T10:30:00Z", eur(100))

// GOOD — shared variable, overloads accept Instant
var _10h30 = parse("2025-01-01T10:30:00Z");
createStockCount(_10h30, 200)
createSale(_10h30, eur(100))
```

If a helper only accepts `String`, add an `Instant` overload rather than calling `.toString()`.

### 7. Fluent Builders for Composite Test Data

When test data combines multiple domain dimensions (price + discount + shipping method), prefer a fluent builder that names each dimension over a flat factory with positional args.

```java
// BAD — positional args, meaning unclear
item(18.0, 15.0, ShippingMethod.EXPRESS)

// GOOD — each dimension named
itemPricedAt(18).discountedTo(15)
```

### Readability Litmus Test

Read the test body aloud, skipping syntax (`var`, `;`, parentheses). If it doesn't sound like a scenario description, refactor until it does.

### Readability Checklist

When writing or reviewing tests, verify:

1. **No unpacking** — Are domain types passed directly to helpers?
2. **Articles** — Do factories start with `a`/`an`?
3. **Intent names** — Do variable names describe the scenario role?
4. **English setup** — Does mock configuration read as Given clauses?
5. **Readable builders** — Does the Arrange section read like a description?

## Anti-Patterns

**Load this reference when:** writing or changing tests, adding mocks, or tempted to add test-only methods to production code.

Tests must verify real behavior, not mock behavior. Mocks are a means to isolate, not the thing being tested.

**Core principle:** Test what the code does, not what the mocks do.

**Following strict TDD prevents these anti-patterns.**

### The Iron Laws

```
1. NEVER test mock behavior
2. NEVER add test-only methods to production classes
3. NEVER mock without understanding dependencies
```

### Anti-Pattern 1: Testing Mock Behavior

**The violation:**
```java
// ❌ BAD: Testing that the mock was called, not that behavior happened
@Test
void it_monitors_stock() {
    stockMonitor.checkStock(warehouseId);
    verify(restockOrderRepository).save(any(RestockOrder.class)); // testing mock interaction
}
```

**Why this is wrong:**
- You're verifying the mock was called, not that the domain behaves correctly
- Test passes when mock is invoked, regardless of correctness
- Tells you nothing about real behavior

**your human partner's correction:** "Are we testing the behavior of a mock?"

**The fix:**
```java
// ✅ GOOD: Use a stub, assert on observable outcome
@Test
void it_reorders_when_product_is_low_on_stock() {
    stockMonitor.checkStock(warehouseId);
    assertThat(restockOrderRepository.findAll()).hasSize(1);
}
```

#### Gate Function

```
BEFORE asserting on any mock interaction (verify):
  Ask: "Am I testing real component behavior or just mock invocation?"

  IF testing mock invocation:
    STOP - Delete the assertion or use a stub with real state

  Test real behavior instead
```

### Anti-Pattern 2: Test-Only Methods in Production

**The violation:**
```java
// ❌ BAD: reset() only used in tests
public class OrderLifecycleService {
    public void reset() { // Looks like production API!
        this.orders.clear();
    }
}

// In tests
@AfterEach void tearDown() { service.reset(); }
```

**Why this is wrong:**
- Production class polluted with test-only code
- Dangerous if accidentally called in production
- Violates YAGNI and separation of concerns
- Confuses object lifecycle with entity lifecycle

**The fix:**
```java
// ✅ GOOD: Use a stub with test-specific access
@Stub
public class StubOrderRepository implements OrderRepository {
    private final List<Order> orders = new ArrayList<>();
    public void clear() { orders.clear(); } // stub method, not production
}
```

#### Gate Function

```
BEFORE adding any method to production class:
  Ask: "Is this only used by tests?"

  IF yes:
    STOP - Don't add it
    Put it in test utilities instead

  Ask: "Does this class own this resource's lifecycle?"

  IF no:
    STOP - Wrong class for this method
```

### Anti-Pattern 3: Mocking Without Understanding

**The violation:**
```java
// ❌ BAD: Mocking the SPI breaks the behavior under test
@Test
void it_ships_order_when_payment_is_accepted() {
    // Mock prevents order lookup that test depends on!
    when(orderRepository.findPending(customerId)).thenReturn(Optional.empty());
    paymentMonitor.onPaymentAccepted(paymentId); // Nothing to ship — test passes vacuously
}
```

**Why this is wrong:**
- Mocked method had side effect test depended on (finding the order)
- Over-mocking to "be safe" breaks actual behavior
- Test passes for wrong reason or fails mysteriously

**The fix:**
```java
// ✅ GOOD: Use a stub with real state
@Test
void it_ships_order_when_payment_is_accepted() {
    orderRepository.save(aPendingOrder(customerId, paymentId));
    paymentMonitor.onPaymentAccepted(paymentId);
    assertThat(orderRepository.findPending(customerId)).isEmpty();
}
```

#### Gate Function

```
BEFORE mocking any dependency:
  STOP - Don't mock yet

  1. Ask: "What side effects does the real method have?"
  2. Ask: "Does this test depend on any of those side effects?"
  3. Ask: "Do I fully understand what this test needs?"

  IF depends on side effects:
    Use test doubles that preserve necessary behavior
    NOT the high-level method the test depends on

  IF unsure what test depends on:
    Run test with real implementation FIRST
    Observe what actually needs to happen
    THEN add minimal mocking at the right level

  Red flags:
    - "I'll mock this to be safe"
    - "This might be slow, better mock it"
    - Mocking without understanding the dependency chain
```

### Anti-Pattern 4: Incomplete Test Doubles

**The violation:**
```java
// ❌ BAD: Partial stub — only fields you think you need
var product = new Product(productId, "keyboard");
// Missing: price, stockLevel, warehouseId that downstream code uses
```

**Why this is wrong:**
- **Partial test data hides structural assumptions** - You only included fields you know about
- **Downstream code may depend on fields you didn't include** - Silent failures
- **Tests pass but integration fails** - Test data incomplete, real data complete
- **False confidence** - Test proves nothing about real behavior

**The Iron Rule:** Build COMPLETE data structures as they exist in reality, not just fields your immediate test uses.

**The fix:**
```java
// ✅ GOOD: Use builders/factory methods that mirror real data
var product = aProduct(productId)
    .withCategory("keyboard")
    .withStockLevel(85)
    .withWarehouse(warehouseId)
    .build();
```

#### Gate Function

```
BEFORE creating test data:
  Check: "Does this mirror the complete real structure?"

  Actions:
    1. Examine actual data structure from production code
    2. Include ALL fields system might consume downstream
    3. Verify test data matches real structure completely

  Critical:
    If you're creating test data, you must understand the ENTIRE structure
    Partial data fails silently when code depends on omitted fields

  If uncertain: Include all fields with realistic defaults
```

### Anti-Pattern 5: Integration Tests as Afterthought

**The violation:**
```
✅ Implementation complete
❌ No tests written
"Ready for testing"
```

**Why this is wrong:**
- Testing is part of implementation, not optional follow-up
- TDD would have caught this
- Can't claim complete without tests

**The fix:**
```
TDD cycle:
1. Write failing test
2. Implement to pass
3. Refactor
4. THEN claim complete
```

### Anti-Pattern 6: Redundant Stubs for Implicit Behavior

**The violation:**
```java
// ❌ BAD: Error handling already returns empty set
inventoryService.havingProductsInWarehouse(warehouseId, new Product[]{});
builder.withoutProduct();
```

**Why this is wrong:**
- The test infrastructure already handles missing stubs
  (e.g. 404 → empty set via error handling)
- Adding explicit empty stubs obscures test intent
- Adds noise that makes the test harder to read

**The fix:**
```java
// ✅ GOOD: Only stub what the test scenario requires
// Unstubbed endpoints return errors, which the
// production code handles by returning empty sets
inventoryService.havingNoWarehouseInInventory(warehouseId);
```

#### Gate Function

```
BEFORE adding a stub that returns empty/default:
  Ask: "What happens if I don't stub this at all?"

  IF error handling produces the same result:
    Don't add the stub — it's noise

  Only stub empty/default when it's meaningful to
  the test scenario (e.g. testing the empty case
  specifically)
```

### Anti-Pattern 7: Testing Compiler-Guaranteed Behavior

**The violation:**
```java
// ❌ BAD: Record accessors are compiler-generated
@Test
void it_exposes_timestamp_and_id() {
    var stockLevel = new RecordedStockLevel<>(TIMESTAMP, ID, 42.5);
    assertThat(stockLevel.timestamp()).isEqualTo(TIMESTAMP);
    assertThat(stockLevel.id()).isEqualTo(ID);
}

// ❌ BAD: implements clause is compiler-enforced
@Test
void it_is_a_recorded_data_point() {
    assertThat(new RecordedStockLevel<>(...))
        .isInstanceOf(RecordedDataPoint.class);
}

// ❌ BAD: Sealed hierarchy exhaustiveness is compiler-checked
@Test
void it_supports_exhaustive_pattern_matching() { ... }
```

**Why this is wrong:**
- Record accessors can't return wrong values — they're generated
- `isInstanceOf` on an `implements` clause duplicates the compiler
- Sealed switch exhaustiveness is a compile error, not a runtime concern
- These tests can never fail without a compilation error first

**What counts as compiler-guaranteed:**
- Record component accessors
- `isInstanceOf` checks on `implements`/`extends` clauses
- Sealed hierarchy exhaustiveness
- Enum values existence

**What is NOT compiler-guaranteed (do test these):**
- Validation logic in compact constructors
- Computed methods on records
- Custom `equals`/`hashCode` behavior
- Business rules in domain types

#### Gate Function

```
BEFORE writing a test:
  Ask: "Can this test fail without a compilation error?"

  IF no → Don't write it
  IF yes → Write it
```

### When Mocks Become Too Complex

**Warning signs:**
- Mock setup longer than test logic
- Mocking everything to make test pass
- Mocks missing methods real components have
- Test breaks when mock changes

**your human partner's question:** "Do we need to be using a mock here?"

**Consider:** Integration tests with real components often simpler than complex mocks

### TDD Prevents These Anti-Patterns

**Why TDD helps:**
1. **Write test first** → Forces you to think about what you're actually testing
2. **Watch it fail** → Confirms test tests real behavior, not mocks
3. **Minimal implementation** → No test-only methods creep in
4. **Real dependencies** → You see what the test actually needs before mocking

**If you're testing mock behavior, you violated TDD** - you added mocks without watching test fail against real code first.

### Anti-Pattern Quick Reference

| Anti-Pattern | Fix |
|--------------|-----|
| Assert on mock elements | Test real component or unmock it |
| Test-only methods in production | Move to test utilities |
| Mock without understanding | Understand dependencies first, mock minimally |
| Incomplete mocks | Mirror real API completely |
| Redundant stubs for defaults | Check what error handling already provides |
| Tests as afterthought | TDD - tests first |
| Over-complex mocks | Consider integration tests |
| Testing compiler guarantees | If it can't fail without compile error, don't test it |

### Red Flags

- Assertion checks for `*-mock` test IDs
- Methods only called in test files
- Mock setup is >50% of test
- Test fails when you remove mock
- Can't explain why mock is needed
- Mocking "just to be safe"
- Stubbing empty results when error handling already provides them
- Testing record accessors, `isInstanceOf` on `implements`, sealed exhaustiveness

### The Bottom Line

**Mocks are tools to isolate, not things to test.**

If TDD reveals you're testing mock behavior, you've gone wrong.

Fix: Test real behavior or question why you're mocking at all.
