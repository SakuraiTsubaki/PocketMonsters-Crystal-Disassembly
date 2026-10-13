import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class EnglishMainFontTests(unittest.TestCase):
    def setUp(self):
        self.report = json.loads((ROOT / "analysis/crystal-en-main-font.json").read_text(encoding="utf-8"))
        self.manifest = json.loads((ROOT / "manifests/english-main-font.json").read_text(encoding="utf-8"))

    def test_range_and_revisions(self):
        self.assertEqual((self.report["source_offset"], self.report["source_length"]), (0xF8200, 1024))
        self.assertEqual(self.report["source_sha256"], "2b3fe12a895c2b028aef61e94dbaacd5ddfd3ff1e4f4d3c1815daf99dfb298f7")
        self.assertEqual([x["id"] for x in self.manifest["releases"]], ["crystal-en-rev0", "crystal-en-rev1"])
        self.assertEqual({x["range_sha256"] for x in self.manifest["releases"]}, {self.report["source_sha256"]})

    def test_outputs(self):
        self.assertFalse(self.manifest["raw_rom_bytes_included"])
        for output in self.manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])
        self.assertEqual(hashlib.sha256((ROOT / "graphics/font/main-font-en.png").read_bytes()).hexdigest(), self.report["png_sha256"])


if __name__ == "__main__":
    unittest.main()
