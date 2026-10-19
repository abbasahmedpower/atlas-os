import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from protocol_lab import pack,Decoder
class Tests(unittest.TestCase):
 def test_split(self):
  d=Decoder();wire=pack(b'abc');self.assertEqual(d.feed(wire[:2]),[]);self.assertEqual(d.feed(wire[2:]),[b'abc'])
 def test_coalesced(self):
  self.assertEqual(Decoder().feed(pack(b'a')+pack(b'b')),[b'a',b'b'])
 def test_empty(self): self.assertEqual(Decoder().feed(pack(b'')),[b''])
 def test_limit(self):
  with self.assertRaises(ValueError): pack(b'x'*65537)
 def test_bad_frame(self):
  with self.assertRaises(ValueError): Decoder().feed(b'\xff\xff\xff\xff')
if __name__=='__main__': unittest.main()
