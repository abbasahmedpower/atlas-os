#!/usr/bin/env python3
"""Safe localhost-only framing demonstration: no command execution, no remote access."""
import socket
import struct
import threading

MAX_LEN = 1024 * 1024


def read_exact(sock, n):
    buf = bytearray()
    while len(buf) < n:
        part = sock.recv(n - len(buf))
        if not part:
            raise EOFError("peer closed before frame completed")
        buf.extend(part)
    return bytes(buf)


def receive_frame(sock):
    (size,) = struct.unpack("!I", read_exact(sock, 4))
    if size > MAX_LEN:
        raise ValueError("frame size exceeds cap")
    return read_exact(sock, size)


def run():
    ready = threading.Event()
    port_box = []
    result = []

    def server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
            listener.bind(("127.0.0.1", 0))
            listener.listen(1)
            port_box.append(listener.getsockname()[1])
            ready.set()
            conn, _ = listener.accept()
            with conn:
                conn.settimeout(3)
                result.append(receive_frame(conn).decode("utf-8"))

    worker = threading.Thread(target=server, daemon=True)
    worker.start()
    if not ready.wait(3):
        raise TimeoutError("listener failed to start")
    data = "Hello TCP framing!".encode("utf-8")
    frame = struct.pack("!I", len(data)) + data
    with socket.create_connection(("127.0.0.1", port_box[0]), timeout=3) as client:
        for chunk in (frame[:2], frame[2:6], frame[6:]):
            client.sendall(chunk)
    worker.join(timeout=4)
    assert not worker.is_alive(), "server did not finish"
    assert result == ["Hello TCP framing!"], result
    print("PASS: split TCP writes reconstructed into one framed message")


if __name__ == "__main__":
    run()
