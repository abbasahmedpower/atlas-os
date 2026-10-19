# Depth ladder and instruments
L0 user-facing failure: logs, acceptance tests.
L1 architecture: component diagrams, data lineage, trust boundaries.
L2 module: API contracts, thread ownership, dependencies.
L3 function/state: state transitions, invariants, pre/post conditions.
L4 data/control: AST, CFG, SSA, reaching definitions, taint paths; distinguish static approximation from concrete execution.
L5 runtime: scheduling, GC, file/socket I/O, syscall/ETW/eBPF tracing.
L6 native binary: ABI, registers, calling conventions, disassembly, relocation, heap layout, ASLR; don't infer source-level intent from one disassembly.
L7 hardware: clock domains, caches, memory model, bus timing, electrical integrity; use safe isolation.
Profiling detail: warm-up, clock choice, repetition, system load, power governor, variance, effect sizes. ns estimates require reliable timing setup.
