import hashlib, json, unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
EXPECTED={'de':'22c0dfec9ce004dceebe280d71fa2579fa376064f70284bbf46322e163aa1160','fr':'178b0da870a3cc58414940412eb6473f515b8941cb83d81a1a42d05ca82749e7','it':'2592aef20701fa1d5df5cf3343ffb4293092c911177868fa4a94698c27f7be89','es':'4aacb5b3ac7a741d99f507e7c31393c015dea26a3ce8876021c50e7c761c1141'}
class Tests(unittest.TestCase):
 def test_languages(self):
  for lang,digest in EXPECTED.items():
   c=json.loads((ROOT/f'analysis/crystal-{lang}-startup-cfg.json').read_text());self.assertEqual(c['source_sha256'],digest);self.assertEqual([b['start_address'] for b in c['blocks']],[0x16e,0x172,0x175,0x177,0x1a8]);self.assertTrue(all('block_bytes' not in b for b in c['blocks']))
 def test_manifests(self):
  for lang in EXPECTED:
   m=json.loads((ROOT/f'manifests/{lang}-startup-cfg.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
