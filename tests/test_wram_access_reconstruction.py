import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class T(unittest.TestCase):
 def test_releases(self):
  s=json.loads((ROOT/"analysis/wram-access-summary.json").read_text());self.assertEqual(s["release_count"],7);self.assertEqual(s["functions"],["FarCopyWRAM","GetFarWRAMByte","GetFarWRAMWord"])
  for r in s["releases"]:
   e=json.loads((ROOT/r["evidence"]).read_text());f=e["functions"];d=json.loads((ROOT/e["cross_reference"]["far_access"]).read_text());self.assertEqual(f["FarCopyWRAM"]["rom_offset"],d["functions"]["GetFarWord"]["range_end_exclusive"]);self.assertEqual(f["GetFarWRAMByte"]["rom_offset"],f["FarCopyWRAM"]["range_end_exclusive"]);self.assertEqual(f["GetFarWRAMWord"]["rom_offset"],f["GetFarWRAMByte"]["range_end_exclusive"]);self.assertEqual(e["hardware"]["wram_bank_register"],"0xFF70");self.assertFalse(e["raw_rom_bytes_included"])
 def test_manifest(self):
  m=json.loads((ROOT/"manifests/wram-access-reconstruction.json").read_text())
  for x in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/x["path"]).read_bytes()).hexdigest(),x["sha256"])
if __name__=="__main__":unittest.main()
