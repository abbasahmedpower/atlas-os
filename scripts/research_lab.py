"""Small, offline, safe causal experiment: framed TCP payloads across arbitrary chunks."""
from dataclasses import dataclass
import struct
MAX_SIZE=1024*1024
@dataclass
class Framer:
    buf: bytearray
    def __init__(self): self.buf=bytearray()
    def feed(self, chunk:bytes):
        self.buf.extend(chunk)
        result=[]
        while len(self.buf)>=4:
            n=struct.unpack('!I',self.buf[:4])[0]
            if n>MAX_SIZE: raise ValueError('declared frame too large')
            if len(self.buf)<4+n: break
            result.append(bytes(self.buf[4:4+n]))
            del self.buf[:4+n]
        return result

def encode(data:bytes)->bytes:
    if len(data)>MAX_SIZE: raise ValueError('payload too large')
    return struct.pack('!I',len(data))+data

if __name__=='__main__':
    combined=encode(b'alpha')+encode(b'')+encode(b'beta')
    receiver=Framer(); out=[]
    for chunk in [combined[:1],combined[1:4],combined[4:9],combined[9:11],combined[11:]]:
        out.extend(receiver.feed(chunk))
    assert out==[b'alpha',b'',b'beta']
    print('PASS: fragmentation, coalescing, and zero-length message')
