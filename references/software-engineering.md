# Software engineering track

## Work like an accountable engineer
Define API/contracts, invariants, input models, outputs, performance budgets, threat boundaries and maintenance costs. Prefer minimal architecture that satisfies requirements. Use ADRs for meaningful choices.

## Domains
CS fundamentals, algorithms, data structures, networks, databases, concurrency, memory, compiler/toolchain, distributed systems, secure coding, .NET/C#, Rust, C/C++, Kotlin, Python, web, DevOps, Git and architecture.

## Source repository analysis
Inventory license/README/build files/dependencies/tests; establish reproducible build; locate entry points; map components/data flow; identify configuration/secrets risks; inspect git history; run representative tests; produce a short architecture map and risk list before edits.

## Implementation checklist
1 requirements and edge cases; 2 executable baseline; 3 smallest complete vertical slice; 4 tests covering normal, error and boundary paths; 5 concurrency, cancellation and resource disposal; 6 logs/metrics; 7 documentation; 8 review, lint and security checks; 9 measured performance; 10 safe release/rollback.

## Example: C# network services
Explain framing over TCP streams, async cancellation, socket ownership, TLS cert validation, bounded queues, backpressure, reconnect jitter, allocation behavior, trace correlation and adversarial input. Never assume each Receive call equals a message.

## Code review scoring
Correctness, safety, security, readability, modularity, tests, performance evidence, maintainability and deployment risk. Distinguish blocker from nice-to-have.
