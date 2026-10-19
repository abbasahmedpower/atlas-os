# Reverse engineering track

## Legitimate scope
Owned binaries, permitted research, sample training programs, malware under isolated analysis and interoperability research. Preserve legal constraints, provenance and safety.

## Levels
0 file identification and hashes; 1 compiler/toolchain hypotheses; 2 format PE/ELF/Mach-O; 3 symbols/imports/strings; 4 function boundaries and CFG; 5 call graph and data flow; 6 decompilation vs actual assembly; 7 dynamic tracing and stack/register state; 8 ABI calling conventions and memory layout; 9 indirect branches/jump tables; 10 optimizations and obfuscation; 11 symbolic execution; 12 evidence report.

## Practical lab progression
Write a tiny C program with two branches and a switch. Build debug and optimized binaries; inspect with `file`, `objdump` or platform equivalents, Ghidra, debugger; map source-to-assembly; compare CFG and call sites; alter test inputs; write one hypothesis and confirm it with a trace.

## Never overclaim
Decompilation is an approximation; unreachable code requires proof; padding heuristics are probabilistic; indirect branches may require runtime observation. Track confidence and false positives explicitly.

## Tools
Ghidra, radare2/Cutter, LLDB/GDB, WinDbg, x64dbg, Binary Ninja where licensed, Frida for authorized instrumentation, angr for controlled symbolic examples, Detect It Easy, `readelf`, `objdump`, `nm`.

## Report
Binary hash and origin; architecture; OS/ABI; observed vs inferred; function and basic block evidence; test conditions; uncertainty; safe next experiment.
