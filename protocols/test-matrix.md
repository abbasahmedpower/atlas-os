# Test matrix
For each API or module define: golden path, boundary values, invalid inputs, timeouts, partial I/O, interruption, concurrency, repeated execution, resource exhaustion, permissions failure, Unicode and encoding, serialization compatibility, rollback/migration, reproducibility.
Use a test pyramid (unit/integration/e2e) fitted to risks. Add property-based and fuzz checks for parsers. Track mutation test quality where possible. For security, use controlled test fixtures and avoid testing third-party systems without authorization.
When failure appears, save the smallest fixture; make a regression test fail before patching, then pass afterward.
