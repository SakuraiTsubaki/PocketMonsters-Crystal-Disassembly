import csv,hashlib,json,unittest
from pathlib import Path
R=Path(__file__).parents[1];E={'crystal-jp-rev0':0x30DC,'crystal-en-rev0':0x3110,'crystal-en-rev1':0x3110,'crystal-de-rev0':0x30FA,'crystal-fr-rev0':0x30FD,'crystal-it-rev0':0x30FE,'crystal-es-rev0':0x30FA};H='076069c0b328a081fe3c9743adb8359b5739d024cbe928ee03b1e57e97cf357a'
class T(unittest.TestCase):
 def test_releases(self):
  rows={x['id']:x for x in csv.DictReader((R/'research/releases.csv').read_text().splitlines())};self.assertEqual(set(rows),set(E))
  for k,a in E.items():
   m=json.loads((R/f'analysis/{k}-simple-divide.json').read_text());f=m['function'];rr=json.loads((R/f'analysis/{k}-random-range.json').read_text());self.assertEqual(m['target']['sha256'],rows[k]['sha256']);self.assertEqual((f['bank'],f['address'],f['length'],f['code_sha256']),(0,a,9,H));self.assertEqual(f['address'],rr['function']['dependencies']['SimpleDivide']['address']);self.assertFalse(m['raw_rom_bytes_included'])
 def test_manifest(self):
  m=json.loads((R/'manifests/simple-divide-reconstruction.json').read_text());[self.assertEqual(hashlib.sha256((R/o['path']).read_bytes()).hexdigest(),o['sha256'])for o in m['outputs']]
if __name__=='__main__':unittest.main()
