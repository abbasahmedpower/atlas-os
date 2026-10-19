import unittest,struct,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from research_lab import Framer,encode,MAX_SIZE
from evaluate_skill import inspect
class LabTests(unittest.TestCase):
    def test_fragmented(self):
        p=encode(b'hello');f=Framer();o=[]
        for b in p:o+=f.feed(bytes([b]))
        self.assertEqual(o,[b'hello'])
    def test_coalesced(self):self.assertEqual(Framer().feed(encode(b'a')+encode(b'b')),[b'a',b'b'])
    def test_zero(self):self.assertEqual(Framer().feed(encode(b'')),[b''])
    def test_reject_too_large(self):
        with self.assertRaises(ValueError):Framer().feed(struct.pack('!I',MAX_SIZE+1))
    def test_edge_limit(self):self.assertEqual(len(Framer().feed(encode(b'x'*MAX_SIZE))[0]),MAX_SIZE)
    def test_structure(self):self.assertEqual(inspect(Path(__file__).resolve().parents[1]),[])
if __name__=='__main__':unittest.main()
