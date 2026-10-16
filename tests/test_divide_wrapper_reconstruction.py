import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':(0x30F0,0x6977),'crystal-en-rev0':(0x3124,0x673E),'crystal-en-rev1':(0x3124,0x673E),'crystal-de-rev0':(0x310E,0x675F),'crystal-fr-rev0':(0x3111,0x6758),'crystal-it-rev0':(0x3112,0x6757),'crystal-es-rev0':(0x310E,0x675D)}
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,(a,t) in E.items():
   m=json.loads((R/f'analysis/{k}-divide-wrapper.json').read_text());f=m['function'];d=json.loads((R/f'analysis/{k}-multiply-wrapper.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,a,18));self.assertEqual(f['rom_offset'],d['function']['range_end_exclusive']);self.assertEqual(f['home_call']['target']['bank'],1);self.assertEqual(f['home_call']['target']['address'],t);self.assertEqual(f['home_call']['saved_rom_bank_hram_address'],0xFF9D);self.assertEqual(f['preserved_registers'],['AF','BC','DE','HL']);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/divide-wrapper-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
