# Build like a careful engineer
1. Contract: user stories, threat boundaries, I/O schema, failure modes, performance SLOs, portability.
2. Design: separation of concerns, state transitions, lifecycle, ownership, cancellation and backpressure.
3. Code: small cohesive modules, documented invariants, explicit errors, input validation, bounded resource use, least privilege, structured logs without secrets.
4. Verification: formatting/lint/type checks/build, unit tests, integration tests, property tests, fuzz tests where feasible, static dependency review.
5. Reliability: test timeouts, connection losses, cancellation, thread races, disk-full, malformed payloads, version skew.
6. Performance: profile baseline, warmed/uncached distinction, repetitions/confidence intervals, compare equivalent workloads.
7. Deliver: reproducible setup, demo, tests, metrics caveats, migration and rollback, known issues. Never say 'production-ready' from unit tests alone.
