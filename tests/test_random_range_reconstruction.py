import csv,hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
EXPECTED={'crystal-jp-rev0':(0x2F83,0x30DC),'crystal-en-rev0':(0x2FB1,0x3110),'crystal-en-rev1':(0x2FB1,0x3110),'crystal-de-rev0':(0x2F9B,0x30FA),'crystal-fr-rev0':(0x2F9E,0x30FD),'crystal-it-rev0':(0x2F9F,0x30FE),'crystal-es-rev0':(0x2F9B,0x30FA)}
class Tests(unittest.TestCase):
 def test_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text(encoding='utf-8').splitlines())};self.assertEqual(set(rows),set(EXPECTED))
  for release,(address,divide) in EXPECTED.items():
   m=json.loads((ROOT/f'analysis/{release}-random-range.json').read_text());f=m['function'];r=json.loads((ROOT/f'analysis/{release}-random.json').read_text());w=json.loads((ROOT/f'analysis/{release}-battle-random.json').read_text())
   self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((f['address'],f['length']),(address,26));self.assertEqual(f['rom_offset'],w['function']['range_end_exclusive']);self.assertEqual(f['dependencies']['Random']['address'],r['function']['address']);self.assertEqual(f['dependencies']['hRandomAdd'],0xFFE1);self.assertEqual(f['dependencies']['SimpleDivide']['address'],divide);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/random-range-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
