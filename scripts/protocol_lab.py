#!/usr/bin/env python3
"""Offline-safe TCP framing demonstration: no sockets, no network, no dependencies."""
import struct

def pack(message: bytes) -> bytes:
    if len(message) > 65536: raise ValueError("message too large")
    return struct.pack('!I', len(message)) + message

class Decoder:
    def __init__(self): self.buf = bytearray()
    def feed(self, chunk):
        self.buf.extend(chunk)
        out=[]
        while len(self.buf) >= 4:
            size = struct.unpack('!I', self.buf[:4])[0]
            if size > 65536: raise ValueError('frame too large')
            if len(self.buf) < size+4: break
            out.append(bytes(self.buf[4:size+4]))
            del self.buf[:size+4]
        return out

if __name__ == '__main__':
    d=Decoder()
    wire=pack(b'hello')+pack(b'world')
    found=[]
    for chunk in [wire[:1],wire[1:5],wire[5:8],wire[8:13],wire[13:]]:
        found.extend(d.feed(chunk))
    assert found == [b'hello',b'world']
    print('PASS: fragmented and coalesced frames decoded')
