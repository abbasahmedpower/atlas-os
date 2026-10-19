# Reverse engineering safety-first research
Use an owned open-source toy binary compiled by the student, then compare source ↔ compiler output ↔ observed runtime. Track compiler version, ISA/ABI, symbols, optimization flags, and hash.
Static: magic/header, sections, imports, exports, relocations, strings, functions, cross references, CFG and decompilation uncertainty.
Dynamic: breakpoints, watchpoints, registers, stack, heap, syscalls, call trace, timeouts and snapshot restoration; run unknown samples only in controlled isolated environments.
For each decompiled assertion: derive testable hypothesis, verify with disassembly and controlled execution. Control-flow recovery: indirect jumps, tail calls, exceptions, jump tables, obfuscation, dead code, packing and data mixed with code. Score confidence, admit unsupported branches. No claims that a decompiler shows original source faithfully.
