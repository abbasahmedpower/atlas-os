# Testing, debugging and performance

## Test pyramid with nuance
Static analysis; unit tests; property-based and fuzz testing; integration; contract; end-to-end; hardware-in-loop where relevant; load/performance; resilience/fault injection; security tests. Choose by risk, not dogma.

## Repro-first debugging
Environment/version -> symptom and exact timeline -> minimum reproduction -> expected vs observed -> hypotheses -> one variable per experiment -> instrumentation -> root-cause evidence -> fix -> negative and regression tests.

## Coverage considerations
Statement/branch/path coverage, MC/DC where applicable, test quality and mutation testing. High coverage alone cannot prove correctness.

## Benchmarks
Specify platform, number of runs, warmup, configuration, workload distribution, statistical uncertainty and units. Don't claim speedup without baseline; distinguish latency p50/p95/p99 from throughput. Include CPU/memory costs and cold starts.

## Failure modes
Timeouts, deadlocks, races, use-after-free, integer overflow, input edge cases, flaky tests, ordering, cache invalidation, stale configurations, partial reads, precision loss, physical sensor noise.

## Output
Test matrix + exact commands + expected result + actual result (only if observed) + bugs found + risks remaining.
