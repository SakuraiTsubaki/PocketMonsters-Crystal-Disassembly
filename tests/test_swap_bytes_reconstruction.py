import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/swap-bytes-summary.json").read_text());self.assertEqual(s["release_count"],7);self.assertEqual(s["function"],"SwapBytes")
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());f=e["function"];d=json.loads((ROOT/e["cross_reference"]["copy_bytes"]).read_text());self.assertEqual(f["rom_offset"],d["function"]["range_end_exclusive"]);self.assertEqual(f["length"],13);self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/swap-bytes-reconstruction.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
