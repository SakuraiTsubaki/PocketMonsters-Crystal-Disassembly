import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':0x3102,'crystal-en-rev0':0x3136,'crystal-en-rev1':0x3136,'crystal-de-rev0':0x3120,'crystal-fr-rev0':0x3123,'crystal-it-rev0':0x3124,'crystal-es-rev0':0x3120}
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E));hashes=set()
  for k,a in E.items():
   m=json.loads((R/f'analysis/{k}-subtract-absolute.json').read_text());f=m['function'];d=json.loads((R/f'analysis/{k}-divide-wrapper.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,a,7));self.assertEqual(f['rom_offset'],d['function']['range_end_exclusive']);self.assertEqual(m['semantics']['carry'],'set exactly when the original A was less than B');self.assertFalse(m['raw_rom_bytes_included']);hashes.add(f['code_sha256'])
  self.assertEqual(len(hashes),1)
 def test_manifest(self):
  m=json.loads((R/'manifests/subtract-absolute-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
