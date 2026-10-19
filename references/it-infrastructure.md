# IT & infrastructure track

Focus: TCP/IP, DNS, DHCP, TLS, routing, firewalls, Linux systemd/journald, Windows services/ETW, identities, virtualization, storage, backups, containers, Kubernetes, IaC, observability and disaster recovery.

## Lab architecture
Prefer one isolated VM and one controlled peer; label networks, routes and boundaries. Record OS/build, NICs, IP subnets, DNS, firewall and snapshots. Avoid exposing insecure services to the Internet.

## Every configuration change
Baseline -> inspect current state -> plan idempotent change -> backup -> apply -> test -> document and rollback. No invented commands for unverified OS releases; cite exact vendor docs where possible.

## Example drills
Trace DNS resolution, show TCP handshake in a packet capture, diagnose dropped packets, inspect service logs, measure disk I/O, recover from misconfigured firewall in snapshot, test backup restoration.
