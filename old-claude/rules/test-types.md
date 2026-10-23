# Test Types

The codebase uses four types of tests, each serving a specific purpose.

## 1. Unit Tests

**Purpose:** Test domain logic in isolation. Do not mock intermediate domain classes.

**Characteristics:**
- Fast execution (no external dependencies)
- Use stub implementations of SPI interfaces
- Located in `src/test/java` mirroring production code structure
- No Spring context

**Example:**

```java
class PaymentMonitorTest {

    private StubOrderRepository orderRepository;
    private PaymentMonitor monitor;

    @BeforeEach
    void setUp() {
        orderRepository = new StubOrderRepository();
        monitor = new PaymentMonitor(orderRepository);
    }

    @Test
    void it_cancels_order_when_payment_declined() {
        // Pure domain logic test with stub
    }
}
```

## 2. Integration Tests

**Purpose:** Test infrastructure adapters (repositories, REST clients, controllers)

**Characteristics:**
- Test integration with external systems using test doubles
- Use `@WebMvcTest` for controller testing
- Use MockRestServiceServer for external HTTP service testing, and make them behave like a real service with internal state
- Test database adapters with TestContainers
- May load partial Spring context

**Example:**

```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private OrderService orderService;

    @Test
    void it_returns_orders_for_customer() throws Exception {
        mockMvc.perform(get("/api/customers/{customerId}/orders", "customer-1"))
            .andExpect(status().isOk());
    }
}
```

## 3. End-to-End (E2E) Tests

**Purpose:** Test complete application flows with real infrastructure

**Characteristics:**
- Full Spring Boot application context
- Real database (PostgreSQL via TestContainers)
- Use `@AppTest` custom annotation
- External services mocked with WireMock
- Tests complete user journeys

**Example:**

```java
@AppTest
class OrderFulfillmentE2ETest {

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private OrderRepository orderRepository;

    @Test
    void it_places_and_ships_an_order() {
        // Test complete flow from API call to database
    }
}
```

## 4. ArchUnit Tests

**Purpose:** Enforce hexagonal architecture rules and integration patterns of bounded contexts according to the strategic design.

**Characteristics:**
- Validate domain isolation (no dependencies on infrastructure or ACL)
- Verify package structure and naming conventions
- Check proper use of annotations
- Fail build if architecture rules are violated

**Example:**

```java
@AnalyzeClasses(packages = "com.example.shop.ordering")
class ArchitectureTest {

    @ArchTest
    static final ArchRule domain_must_not_depend_on_infrastructure =
        classes().that().resideInAPackage("..domain..")
            .should().onlyDependOnClassesThat()
            .resideOutsideOfPackage("..infra..");
}
```

## Test Selection

- **Unit tests:** Domain logic
- **Integration tests:** For adapters and infrastructure components
- **E2E tests:** For critical user journeys and validating integration of all components
- **ArchUnit tests:** Run in CI/CD

## Performance

- Unit tests: Milliseconds per test
- Integration tests: Milliseconds per test
- E2E tests: Seconds per test (Spring context startup)
- ArchUnit tests: Seconds (analyze entire codebase)
