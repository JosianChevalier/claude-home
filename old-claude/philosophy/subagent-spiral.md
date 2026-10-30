# Rationale: Subagent Spiral

Main context is for judgment, not reconnaissance. In code exploration, the expensive part is rarely the files that matter; it is the fan-out around them. One relevant file suggests neighbors, callers, contracts, migrations, adapters, and similar paths. Most of that checking is useful only because it proves what can be ignored.

That is exactly the work scouts should do. A scout can be safer than the main context: better to check one plausible edge too many than to miss the file that changes the decision, because the scout's excess tokens die with the scout. The main context should not pay the cost of being better safe than sorry.

The spiral is: find the core site of the demand, send scouts to explore related code the main agent would otherwise check, have them report only what is worth reading, then read that returned set in the main context. If the read exposes another relevant surrounding area, repeat. Stop when there is no relevant related code left for the current decision.

The scout report is not a tour. It should return decision-bearing files, seams, hazards, and open questions. The main agent keeps the map and makes the call; scouts burn tokens to shrink the map.
