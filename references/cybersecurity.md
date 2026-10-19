# Cybersecurity track — Red + Blue + Purple

## Competencies
Network fundamentals; OS security; web/API security; identity and access; secure coding; cryptography engineering; threat modeling; vulnerability discovery and triage; malware analysis in isolation; detection engineering; DFIR; cloud/container security; supply chain; reporting.

## Offensive learning (authorized targets ONLY)
Start with asset ownership/scope, threat model, observation and benign validation. Use intentionally vulnerable practice applications, local VMs, CTFs and test harnesses. Explain vulnerabilities through root cause, impact, detection and mitigation. Avoid uncontrolled payloads, public scanning, stealth/persistence, credential harvesting, operational exploitation against unknown targets.

## Example 12-lesson sequence
1 TCP and sockets; 2 HTTP and TLS; 3 Linux/Windows privilege models; 4 OWASP testing approach; 5 input validation/SQL parameterization in a toy app; 6 auth/session security; 7 logging/telemetry; 8 MITRE ATT&CK mapping; 9 detection rule creation against simulated events; 10 secure architecture review; 11 incident triage with synthetic logs; 12 written security finding + regression test.

## Tools selection, no cargo-culting
Wireshark/tshark, Ncat, tcpdump, Sysmon, Windows Event Viewer, Zeek, Suricata, OpenVAS/Greenbone in bounded labs, OWASP ZAP for local test apps, Ghidra for analysis, Semgrep, CodeQL, Trivy, osquery, YARA. Always document purpose, prerequisites, installation source, OS support, command, expected output, pitfalls and cleanup. Current versions require verification.

## Controlled lab checklist
Defined target/owner; isolated networking; snapshots; no production credentials; no external listeners where not needed; safe traffic volume; explicit success criteria; preserve telemetry; revert VM when complete.

## Analytical template
Asset -> trust boundary -> plausible failure -> supporting evidence -> severity with assumptions -> reproduction in lab -> defensive telemetry -> remediation -> regression proof.

## Canonical reference starting points
https://csrc.nist.gov/pubs/sp/800/181/r1/final
https://attack.mitre.org/
https://owasp.org/www-project-web-security-testing-guide/
https://cwe.mitre.org/
https://csrc.nist.gov/projects/secure-software-development-framework
