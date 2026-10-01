import hashlib,json,unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]

class TitleLogoTests(unittest.TestCase):
 def setUp(self):
  self.manifest=json.loads((ROOT/'manifests/title-logos.json').read_text(encoding='utf-8'))
 def test_official_languages_and_priority(self):
  self.assertEqual({a['language'] for a in self.manifest['artifacts']},{'ja','en','de','fr','it','es'})
  self.assertEqual(self.manifest['origin_reference'],'crystal-jp-rev0')
  self.assertIsNone(self.manifest['korean_release'])
 def test_reports_and_pngs_are_hash_linked(self):
  for artifact in self.manifest['artifacts']:
   report=json.loads((ROOT/artifact['report']).read_text(encoding='utf-8'))
   png=(ROOT/artifact['png']).read_bytes()
   self.assertEqual(hashlib.sha256(png).hexdigest(),report['png_sha256'])
   self.assertEqual(report['format'],'pokemon-gen2-lz-to-game-boy-2bpp')
   self.assertEqual(report['decompressed_length'],report['tile_count']*16)
 def test_english_revisions_share_art(self):
  reports=[json.loads((ROOT/f'analysis/crystal-en-rev{n}-title-logo.json').read_text()) for n in (0,1)]
  self.assertEqual(reports[0]['decompressed_sha256'],reports[1]['decompressed_sha256'])
  self.assertNotEqual(reports[0]['rom_sha256'],reports[1]['rom_sha256'])
 def test_localized_art_is_not_substituted(self):
  ids=('en-rev0','de-rev0','fr-rev0','it-rev0','es-rev0')
  hashes={json.loads((ROOT/f'analysis/crystal-{x}-title-logo.json').read_text())['decompressed_sha256'] for x in ids}
  self.assertEqual(len(hashes),len(ids))

if __name__=='__main__':unittest.main()
