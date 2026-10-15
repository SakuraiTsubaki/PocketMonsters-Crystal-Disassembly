import csv, hashlib, json, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
EXPECTED={
 'crystal-jp-rev0':(0x2F71,0x6DEA,0xCFAA),'crystal-en-rev0':(0x2F9F,0x6DD8,0xCFB6),
 'crystal-en-rev1':(0x2F9F,0x6DD8,0xCFB6),'crystal-de-rev0':(0x2F89,0x6DD9,0xCFB6),
 'crystal-fr-rev0':(0x2F8C,0x6DDB,0xCFB6),'crystal-it-rev0':(0x2F8D,0x6DD9,0xCFB6),
 'crystal-es-rev0':(0x2F89,0x6DD9,0xCFB6)}
class Tests(unittest.TestCase):
 def test_all_catalogued_releases(self):
  rows={r['id']:r for r in csv.DictReader((ROOT/'research/releases.csv').read_text(encoding='utf-8').splitlines())};self.assertEqual(set(rows),set(EXPECTED))
  for release,(address,target,temp) in EXPECTED.items():
   m=json.loads((ROOT/f'analysis/{release}-battle-random.json').read_text());f=m['function'];r=json.loads((ROOT/f'analysis/{release}-random.json').read_text())
   self.assertEqual(m['target']['sha256'],rows[release]['sha256']);self.assertEqual((f['bank'],f['address'],f['length']),(0,address,18));self.assertEqual(f['rom_offset'],r['function']['range_end_exclusive']);self.assertEqual(f['target']['bank'],15);self.assertEqual(f['target']['address'],target);self.assertEqual(f['temporary_wram'],temp);self.assertEqual(f['hROMBank'],0xFF9D);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/battle-random-reconstruction.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);[self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256']) for o in m['outputs']]
if __name__=='__main__':unittest.main()
