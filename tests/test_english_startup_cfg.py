import hashlib, json, unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_cfg(self):
  c=json.loads((ROOT/'analysis/crystal-en-startup-cfg.json').read_text());self.assertEqual(c['source_sha256'],'d6702e353dcbe2d2c69183046c878ef13a0dae4006e8cdff521cca83dd1582fe');self.assertEqual([b['start_address'] for b in c['blocks']],[0x16e,0x172,0x175,0x177,0x1a8]);self.assertTrue(all('block_bytes' not in b for b in c['blocks']))
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/english-startup-cfg.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
