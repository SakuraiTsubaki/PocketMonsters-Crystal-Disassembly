from __future__ import annotations
import csv, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class ReleaseReportTests(unittest.TestCase):
    def test_release_evidence_is_synchronized(self):
        project=json.loads((ROOT/"project.json").read_text(encoding="utf-8")); report=json.loads((ROOT/"analysis"/"crystal-release-header-report.json").read_text(encoding="utf-8"))
        with (ROOT/"research"/"releases.csv").open(newline="",encoding="utf-8") as stream: rows=list(csv.DictReader(stream))
        p={x["id"]:x for x in project["releases"]}; r={x["id"]:x for x in report["releases"]}; c={x["id"]:x for x in rows}
        self.assertEqual(set(p),set(r)); self.assertEqual(set(p),set(c)); self.assertEqual(len(p),7)
        for release_id,item in p.items(): self.assertEqual(item["status"],"candidate"); self.assertEqual(item["sha256"],r[release_id]["sha256"]); self.assertEqual(item["sha256"],c[release_id]["sha256"]); self.assertTrue(all(r[release_id]["validation"].values()))
    def test_crystal_is_cgb_only_and_region_variants_preserve_ram_header(self):
        releases=json.loads((ROOT/"analysis"/"crystal-release-header-report.json").read_text(encoding="utf-8"))["releases"]
        self.assertTrue(all(x["header"]["cgb_flag"]==0xC0 and x["header"]["sgb_flag"]==0 for x in releases))
        jp=next(x for x in releases if x["id"]=="crystal-jp-rev0"); western=[x for x in releases if x["id"]!="crystal-jp-rev0"]
        self.assertEqual(jp["header"]["ram_size_code"],5); self.assertTrue(all(x["header"]["ram_size_code"]==3 for x in western))
    def test_localized_manufacturer_codes(self):
        releases=json.loads((ROOT/"analysis"/"crystal-release-header-report.json").read_text(encoding="utf-8"))["releases"]
        actual={x["id"]:x["header"].get("manufacturer_code") for x in releases if x["id"].split("-")[1] in {"de","fr","it","es"}}
        self.assertEqual(actual,{"crystal-de-rev0":"BYTD","crystal-fr-rev0":"BYTF","crystal-it-rev0":"BYTI","crystal-es-rev0":"BYTS"})
if __name__=="__main__": unittest.main()
