# Causal debugging engine
Capture exact symptom, reproduction rate, environment, previous working version, logs and expected/actual. Preserve artifacts with privacy controls. Form competing hypotheses H1–H3.
For each hypothesis document: mechanism; prediction; least invasive discriminating experiment; expected signatures in traces; observed signature; confidence after experiment.
Use delta debugging/minimization; enable tracing strategically; bisect commits/configuration when possible; instrument clocks and thread IDs; avoid observer effect. Ensure control experiment.
Micro layers: contract mismatch, state machine, input boundaries, concurrency, buffering, allocators, cancellation, retries, clock semantics, serialization.
Nano layers only when justified: instruction selection, ABI stack alignment, atomic memory orders, false sharing, cache locality, kernel scheduling, interrupt/jitter, DMA electrical behavior.
Deliver: reproducer -> causality supported by changed factor -> narrow fix -> failing-then-passing regression -> performance/security impact -> rollback.
Never conclude 'root cause proven' from correlation alone.
