---
name: clean-code:comments
description: Use when code contains comments. Iterate on naming and structure until every comment is redundant and can be removed. Only "why" comments survive.
---

# Comments Are Code Smells

A comment is an admission that the code failed to express itself. The goal is **zero comments**, reached by iterating on the code until each comment becomes redundant.

## The Rule

1. See a comment explaining *what* or *how* → **iterate on the code** until the comment is redundant
2. Delete the redundant comment
3. Only keep comments that explain *why* something non-obvious exists

## Process: Eliminate a Comment

For every comment, ask: **"Can I change the code so this comment is unnecessary?"**

### Rename to replace the comment

```java
// BAD
// Check if the device has not sent data for more than 24 hours
if (Duration.between(device.lastSeen(), now).toHours() > 24) {

// ITERATION 1 - extract to method, delete comment
if (device.isUnreachableSince(now, Duration.ofHours(24))) {

// ITERATION 2 - push behavior into the object
if (device.isUnreachable()) {
```

### Extract method to replace the comment

```java
// BAD - comment separating a section
void supervise(SiteId siteId) {
    var devices = deviceRepository.findBySite(siteId);

    // Filter devices with anomalies
    var anomalies = devices.stream()
        .filter(d -> d.batteryLevel() < 10 || d.isUnreachable())
        .toList();

    anomalies.forEach(this::raiseAlert);
}

// GOOD - the method name IS the comment
void supervise(SiteId siteId) {
    var devices = deviceRepository.findBySite(siteId);
    var anomalies = detectAnomalies(devices);

    anomalies.forEach(this::raiseAlert);
}
```

### Introduce a domain concept to replace the comment

```java
// BAD
// 10% is considered low battery
if (device.batteryLevel() < 10) {

// GOOD - the domain concept speaks for itself
if (device.hasLowBattery()) {
// Inside Device, the threshold is a named constant or part of BatteryLevel value object
```

### Replace conditional comment with expressive boolean

```java
// BAD
// Only raise alert if device is active and not in maintenance
if (device.status() == ACTIVE && !maintenanceWindows.contains(device.id())) {

// GOOD
var shouldSupervise = device.isActive() && !device.isUnderMaintenance();
if (shouldSupervise) {
```

## The Only Surviving Comments

Comments that explain **why** — a business rule, a workaround, a non-obvious constraint. These cannot be expressed in code.

```java
// DST transitions produce 23h or 25h days, so we use calendar days, not duration
var dayBoundaries = computeCalendarDayBoundaries(zone);

// Legal requirement: alerts must be retained for 5 years even after resolution
var retentionCutoff = now.minus(Period.ofYears(5));
```

If you can turn the "why" into a well-named method or constant, do it. The comment only survives when it truly can't be expressed otherwise.

## Checklist

For every comment in the code:

1. **Is it explaining how/what?** → Rename, extract, or restructure until it's redundant, then delete it
2. **Is it separating sections?** → Each section becomes its own method
3. **Is it explaining why?** → Keep it, but try once more to express it in code
4. **Is it a TODO?** → Acceptable as short-lived markers. Handle each TODO before moving to another task, in its own commit
