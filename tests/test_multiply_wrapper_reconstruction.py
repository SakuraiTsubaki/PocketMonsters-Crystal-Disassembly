import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':(0x30E5,0x6917),'crystal-en-rev0':(0x3119,0x66DE),'crystal-en-rev1':(0x3119,0x66DE),'crystal-de-rev0':(0x3103,0x66FF),'crystal-fr-rev0':(0x3106,0x66F8),'crystal-it-rev0':(0x3107,0x66F7),'crystal-es-rev0':(0x3103,0x66FD)}
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,(a,t) in E.items():
   m=json.loads((R/f'analysis/{k}-multiply-wrapper.json').read_text());f=m['function'];d=json.loads((R/f'analysis/{k}-simple-divide.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,a,11));self.assertEqual(f['rom_offset'],d['function']['range_end_exclusive']);self.assertEqual(f['far_call']['target']['address'],t);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/multiply-wrapper-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
