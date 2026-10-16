import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':0x6977,'crystal-en-rev0':0x673E,'crystal-en-rev1':0x673E,'crystal-de-rev0':0x675F,'crystal-fr-rev0':0x6758,'crystal-it-rev0':0x6757,'crystal-es-rev0':0x675D};H='2e71a8372f131546642602ad73d97165dd7c6d92e2b2dfcf3f06c0c3327c8e0c'
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,s in E.items():
   m=json.loads((R/f'analysis/{k}-divide-core.json').read_text());f=m['function'];w=json.loads((R/f'analysis/{k}-divide-wrapper.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['rom_offset'],f['range_end_exclusive'],f['length']),(1,s,s,s+131,131));self.assertEqual(f['code_sha256'],H);self.assertEqual(s,w['function']['home_call']['target']['rom_offset']);self.assertEqual(f['hram_layout']['divisor'],0xFFB7);self.assertEqual(f['hram_layout']['quotient'],[0xFFB3,0xFFB4,0xFFB5,0xFFB6]);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/divide-core-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
