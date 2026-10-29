import csv
import hashlib
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class ClearBoxReconstructionTests(unittest.TestCase):
    def test_release_matrix_and_evidence(self):
        summary = json.loads((ROOT / "analysis/clear-box-summary.json").read_text())
        with (ROOT / "research/releases.csv").open(encoding="utf-8", newline="") as handle:
            catalog = list(csv.DictReader(handle))
        self.assertEqual(summary["axis"], "Disassembly")
        self.assertEqual(summary["release_count"], len(catalog))
        self.assertEqual(summary["origin_reference"], catalog[0]["id"])
        for release in summary["releases"]:
            evidence = json.loads((ROOT / release["evidence"]).read_text())
            self.assertEqual(evidence["target"]["sha256"], release["sha256"])
            self.assertEqual(evidence["verified_behavior"]["variant"], "crystal-fallthrough")
            self.assertIn("FillBoxWithByte", evidence["related_functions"])
            self.assertFalse(evidence["raw_rom_bytes_included"])

    def test_manifest_hashes_outputs(self):
        manifest = json.loads((ROOT / "manifests/clear-box-reconstruction.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                             output["sha256"])

    def test_source_preserves_fallthrough_entry(self):
        source = (ROOT / "src/clear_box.asm").read_text()
        for token in ("ClearBox::", "ld a, \" \"", "FillBoxWithByte::",
                      "ld bc, SCREEN_WIDTH", "add hl, bc"):
            self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()
