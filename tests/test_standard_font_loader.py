import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class StandardFontLoaderTests(unittest.TestCase):
    def setUp(self):
        self.project = json.loads((ROOT / "project.json").read_text())
        self.source = (ROOT / "src/load_standard_font.asm").read_text()
        self.manifest = json.loads((ROOT / "manifests/standard-font-loaders.json").read_text())

    def reports(self):
        for release in self.project["releases"]:
            path = ROOT / f"analysis/{release['id']}-standard-font-loader.json"
            yield release, json.loads(path.read_text())

    def test_every_release_is_identity_gated(self):
        self.assertEqual(len(list(self.reports())), len(self.project["releases"]))
        for release, report in self.reports():
            self.assertEqual(report["source_sha256"], release["sha256"])
            self.assertFalse(report["raw_bytes_published"])
            self.assertEqual(report["font"]["source_offset"], 0xF8200)
            self.assertEqual(report["font"]["destination"], 0x8800)
            self.assertEqual(report["font"]["tile_count"], 128)
            self.assertEqual(report["code_length"], 65)

    def test_japanese_and_global_layouts_remain_distinct(self):
        for release, report in self.reports():
            expected = 0xFB485 if release["id"] == "crystal-jp-rev0" else 0xFB449
            self.assertEqual(report["loader_offset"], expected)
            self.assertEqual(report["lcd_enabled_branch"]["enabled_transfer_count"], 4)
            self.assertEqual(len(report["calls"]), 4)
            self.assertEqual(report["return_offset"], report["range_end_exclusive"] - 1)

    def test_reconstruction_records_lcd_and_hdma_paths(self):
        self.assertIn("LoadStandardFont::", self.source)
        self.assertIn("ldh a, [rLCDC]", self.source)
        self.assertIn("jp z, Copy1bpp", self.source)
        self.assertEqual(self.source.count("call Get1bppViaHDMA"), 4)

    def test_manifest_hashes_outputs(self):
        self.assertFalse(self.manifest["raw_rom_bytes_included"])
        for output in self.manifest["outputs"]:
            self.assertEqual(
                hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(),
                output["sha256"],
            )


if __name__ == "__main__":
    unittest.main()
