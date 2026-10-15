import csv, hashlib, json, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
ADDRESSES={'crystal-jp-rev0':0x2F5E,'crystal-en-rev0':0x2F8C,'crystal-en-rev1':0x2F8C,'crystal-de-rev0':0x2F76,'crystal-fr-rev0':0x2F79,'crystal-it-rev0':0x2F7A,'crystal-es-rev0':0x2F76}
class Tests(unittest.TestCase):
 def test_all_catalogued_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text(encoding='utf-8').splitlines())};self.assertEqual(set(rows),set(ADDRESSES))
  for release,address in ADDRESSES.items():
   m=json.loads((ROOT/f'analysis/{release}-random.json').read_text());f=m['function'];self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,address,19));self.assertEqual(f['globals'],{'hRandomAdd':0xFFE1,'hRandomSub':0xFFE2});self.assertEqual(f['code_sha256'],'aaec7ea8640c2ff5aab78c3b6a2af39c89ed1393960bfc236aed907c8a087846');self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/random-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
