# Inspections After Edit

After editing production code:

1. Run `mcp__jetbrains__get_file_problems` with `errorsOnly: false` on the modified file to catch issues beyond compilation: unused imports, unused classes, nullability warnings, Spring problems, and style violations.
2. Fix any reported errors before moving on. Warnings are informational — fix only if relevant to the current edition.

## Line Breaking

**Do NOT preemptively break lines.** Write each statement on a single line first, maximizing readability.
Only break a line when `mcp__jetbrains__get_file_problems` reports a line length warning. 
A warning is the ONLY trigger for breaking :
- a long import list
- a long method signature
- a cohesive part of a statement

## Stream Chains

Always break to a new line after `.stream()`:

```java
// GOOD
return stockLevels.stream()
    .mapToDouble(RecordedStockLevel::value)
    .average();

// BAD
return stockLevels.stream().mapToDouble(RecordedStockLevel::value).average();
```

