# 🧪 Sample: TCP streams vs messages (authorized localhost)

**Goal:** Explain why one `recv` does not necessarily equal one application message.

**Theory:** TCP provides an ordered byte stream. Sender `send()` boundaries are NOT guaranteed to match receiver `recv()` boundaries. Multiple writes can appear as one read or one write as multiple reads.

**Safe lab:** Implement localhost-only Python server and client using `127.0.0.1` with explicit 4-byte network-byte-order message length, read_exact loop, 1 MiB maximum length, and test split deliveries. See `scripts/tcp_framing_lab.py`.

**Failure analysis:** Partial reads, timeout, premature EOF, oversized header, invalid text encoding. Verify graceful close and errors.

**Recall:** What does recv(4096) promise? Why length-prefix? What if peer closes halfway?
