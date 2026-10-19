# ATLAS OMEGA V3 — RESEARCH OS
A real reusable set of prompt-driven workflows, experiments and tests. NOT a model upgrade, not unrestricted shell permissions, not a security bypass, and not empirically the world’s best skill.
## Install
Unzip; use `SKILL.md` at the skill root in a compatible agent host, keeping folders together. The host must actually support skills; it may implement different installation rules.
## Validate
`python -m unittest discover -s tests -v`
`python scripts/evaluate_skill.py --selfcheck`
`python scripts/research_lab.py`
## Start
'Use ATLAS OMEGA V3 to teach me TCP stream framing with a reproducible local lab; cite what you know and mark unverified behavior.'
## Retained V2 modules
`references/`, `protocols/`, `templates/`, `curriculum/`, `scripts/` and `tests/` from V2 remain available and are augmented.
## Benchmark integrity
Self-tests validate supplied scripts and structure only. They do not validate response quality, teaching outcomes, cyber defense effectiveness or world rankings.
