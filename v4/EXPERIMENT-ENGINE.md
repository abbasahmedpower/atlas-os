# Causal investigation
- State symptom, expected invariant, observed trace, frequency, severity and environment.
- Build causal directed graph: trigger → state transition → observable failure. Separate correlation and causation.
- Rank at most 3 hypotheses; for each create **prediction / falsifier / smallest safe experiment / measured signal / cost / risk**.
- Prefer discriminating experiments that split hypotheses rather than merely confirming favorites.
- Prevent experiment confounders with fixed versions, random seeds, clocks, input datasets, hardware and environment.
- For concurrency: trace event ordering, happens-before, locks, atomics, memory-order assumptions, schedules; use stress tests and race detectors when available.
- For performance: cold vs warm, sample size, noise, warm-up, percentile latencies, confidence intervals, counter instrumentation overhead.
- Stop rule: if evidence cannot discriminate, state unknown, do not invent root cause. Create regression reproducer before patch.
