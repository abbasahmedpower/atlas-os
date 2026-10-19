# Causal experiment playbook
Problem card: symptom, reproduction, first bad version, environment, impact, exact expected/actual, counterexample.
Generate ≤3 mutually distinguishable causal hypotheses. Rank by plausibility x test value, not just popularity. For each: prediction, a falsifying observation, cheapest isolation test, instrumentation, confounders, and stop threshold.
Use differential tests, fault injection in owned software, deterministic replay, boundary values, concurrency schedulers, mocks, profiling and tracing. Debugging steps: reproduce → bisect → isolate → instrument → reject hypotheses → minimal fix → negative+regression test → review impact.
For nondeterministic bugs collect N repeats and distribution, not 'worked once'. Never claim root cause from mere correlation.
