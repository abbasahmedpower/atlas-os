# Quality gates (all observable)
G0 requirement: acceptance criteria and out-of-scope list.
G1 design: state machines, invariants, concurrency, observability, failure recovery.
G2 implementation: readable code, precise error handling, deterministic dependencies; no hard-coded secrets.
G3 tests: unit, property-based, mutation, integration, fuzz (on owned programs), negative/edge, concurrency where relevant.
G4 secure/perf: least privilege, parsing limits, input trust, benchmark controls, memory/CPU footprint.
G5 release: test report, documented versions, SBOM if relevant, changelog, rollback and known defects.
Never call a code sample 'production-ready' when runtime checks were not performed.
