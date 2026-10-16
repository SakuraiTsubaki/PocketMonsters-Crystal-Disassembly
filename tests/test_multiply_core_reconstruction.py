import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':(0x6917,0x6977),'crystal-en-rev0':(0x66DE,0x673E),'crystal-en-rev1':(0x66DE,0x673E),'crystal-de-rev0':(0x66FF,0x675F),'crystal-fr-rev0':(0x66F8,0x6758),'crystal-it-rev0':(0x66F7,0x6757),'crystal-es-rev0':(0x66FD,0x675D)};H='a3d69fd4f7535c1cb1c25f5cf608f7c88dec9cf2db6f038ffab27b08e71bb7ce'
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,(s,e) in E.items():
   m=json.loads((R/f'analysis/{k}-multiply-core.json').read_text());f=m['function'];w=json.loads((R/f'analysis/{k}-multiply-wrapper.json').read_text());d=json.loads((R/f'analysis/{k}-divide-wrapper.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['rom_offset'],f['range_end_exclusive'],f['length']),(1,s,s,e,96));self.assertEqual(f['code_sha256'],H);self.assertEqual(s,w['function']['far_call']['target']['rom_offset']);self.assertEqual(e,d['function']['home_call']['target']['rom_offset']);self.assertEqual(f['hram_layout']['multiplier'],0xFFB7);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/multiply-core-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
