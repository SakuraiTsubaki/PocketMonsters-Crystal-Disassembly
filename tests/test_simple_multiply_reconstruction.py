import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':0x30D1,'crystal-en-rev0':0x3105,'crystal-en-rev1':0x3105,'crystal-de-rev0':0x30EF,'crystal-fr-rev0':0x30F2,'crystal-it-rev0':0x30F3,'crystal-es-rev0':0x30EF}
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E));hashes=set()
  for k,a in E.items():
   m=json.loads((R/f'analysis/{k}-simple-multiply.json').read_text());f=m['function'];d=json.loads((R/f'analysis/{k}-simple-divide.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,a,11));self.assertEqual(f['range_end_exclusive'],d['function']['rom_offset']);self.assertEqual(f['preserved_registers'],['BC']);self.assertTrue(f['zero_shortcut']);self.assertFalse(m['raw_rom_bytes_included']);hashes.add(f['code_sha256'])
  self.assertEqual(len(hashes),1)
 def test_manifest(self):
  m=json.loads((R/'manifests/simple-multiply-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
