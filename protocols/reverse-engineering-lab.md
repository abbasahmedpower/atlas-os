# Reverse engineering laboratory
Use self-compiled or freely licensed training binaries. Record SHA-256, architecture, format, compiler version, symbols, execution limits.
Pipeline: triage headers & strings -> identify runtime/ABI/imports -> load in disassembler -> enumerate functions and cross-references -> reconstruct CFG and indirect control flow -> recover types/data structures -> attach debugger -> compare decompiler with assembly -> test a hypothesis -> annotate uncertainty.
Micro: calling conventions, vtables, exceptions, pointer aliasing, string encodings, stack frame, relocations, obfuscation patterns in approved samples.
Nano: branch offsets, flags, alignment, instruction-level effects, dynamic dispatch, cache/perf only if relevant.
Never mistake decompiled pseudocode for original source. Treat symbols and automatic function boundaries as hypotheses. Use snapshots; don't run unknown binaries on host OS.
