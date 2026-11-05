"""Tests for the design catalog and its MCP server. Run: python3 -m unittest discover plugin/mcp"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import catalog_server as cs  # noqa: E402


class Catalog(unittest.TestCase):
    def setUp(self):
        self.systems = cs.load("systems.json")
        self.styles = cs.load("styles.json")
        self.ids = {s["id"] for s in self.systems["systems"]}

    def test_every_system_is_sourced(self):
        for s in self.systems["systems"]:
            with self.subTest(s["id"]):
                self.assertTrue(s["docs"].startswith("https://"))
                self.assertTrue(s["owner"])
                self.assertTrue(set(s["categories"]) <= set(self.systems["categories"]))
                for p in s["packages"]:
                    self.assertTrue(p["license"], p["name"])

    def test_ids_are_unique(self):
        self.assertEqual(len(self.ids), len(self.systems["systems"]))

    def test_every_style_names_carriers_that_exist(self):
        for st in self.styles["styles"]:
            with self.subTest(st["id"]):
                self.assertTrue(st["carriers"])
                self.assertTrue(set(st["carriers"]) <= self.ids, set(st["carriers"]) - self.ids)
                self.assertTrue(st["risks"])

    def test_a_style_is_in_one_family(self):
        seen = [m for st in self.styles["styles"] for m in st["members"]]
        self.assertEqual(len(seen), len(set(seen)))


class Queries(unittest.TestCase):
    def test_japanese_public_service(self):
        r = cs.search_design_systems("public service for a japanese local government, forms for everyone", japanese=True)
        self.assertEqual(r["results"][0]["id"], "digital-agency-jp")

    def test_dense_b2b(self):
        r = cs.search_design_systems("b2b admin dashboard with dense data tables")
        top = [x["id"] for x in r["results"][:3]]
        self.assertTrue({"ant-design", "carbon"} & set(top), top)

    def test_platform_filter(self):
        r = cs.search_design_systems("native app", platform="ios")
        self.assertTrue(all(x["id"] in {"fluent-2", "apple-hig"} for x in r["results"]))

    def test_style_by_member_name(self):
        r = cs.search_styles("a landing in the wabi-sabi-craft style for a tea brand")
        self.assertEqual(r["results"][0]["id"], "calm-craft")
        self.assertEqual(cs.get_style("soft-neumorphism-wellness")["id"], "soft-3d")

    def test_unknown_id(self):
        with self.assertRaises(KeyError):
            cs.get_design_system("made-up")

    def test_brief(self):
        md = cs.design_system_brief("carbon", "technical-dark")["markdown"]
        self.assertIn("@carbon/react", md)
        self.assertIn("Apache-2.0", md)
        self.assertIn("| Base token or rule |", md)


class Contrast(unittest.TestCase):
    def test_known_ratios(self):
        self.assertEqual(cs.contrast("#000", "#fff"), 21.0)
        self.assertEqual(cs.contrast("#fff", "#fff"), 1.0)
        self.assertEqual(cs.contrast("#767676", "#ffffff"), 4.54)

    def test_draft_values_from_the_research_are_checked_not_trusted(self):
        # The research's corporate blue was said to pass AAA; it passes AA only.
        c = cs.check_contrast("#ffffff", "#2563EB")
        self.assertTrue(c["AA_text"])
        self.assertFalse(c["AAA_text"])

    def test_bad_color(self):
        with self.assertRaises(ValueError):
            cs.luminance("blue")


class Overlay(unittest.TestCase):
    TABLE = """
| Base token or rule | Base value | Overlay value | Reason |
| --- | --- | --- | --- |
| $interactive | #0f62fe | #8a3ffc | brand purple |
| focus ring | 2px | remove the focus ring | cleaner look |
| | | rounded corners | |
| text: #999999 on #ffffff | | | |
"""

    def test_problems_are_named(self):
        r = cs.check_overlay("carbon", self.TABLE)
        text = "\n".join(r["problems"])
        self.assertIn("weakens visible keyboard focus", text)
        self.assertIn("names no base token", text)
        self.assertIn("under AA", text)
        self.assertFalse(r["ok"])

    def test_clean_overlay(self):
        ok = "| Base token or rule | Base value | Overlay value | Reason |\n| --- | --- | --- | --- |\n| $interactive | #0f62fe | #6929c4 | brand purple, #ffffff on #6929c4 |\n"
        r = cs.check_overlay("carbon", ok)
        self.assertTrue(r["ok"], r["problems"])


class Protocol(unittest.TestCase):
    def call(self, *msgs):
        p = subprocess.run([sys.executable, str(Path(cs.__file__))], input="\n".join(json.dumps(m) for m in msgs) + "\n",
                           capture_output=True, text=True, timeout=30)
        return [json.loads(line) for line in p.stdout.splitlines()]

    def test_session(self):
        out = self.call(
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_design_system", "arguments": {"id": "govuk"}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "get_design_system", "arguments": {"id": "nope"}}},
        )
        self.assertEqual([m["id"] for m in out], [1, 2, 3, 4])
        self.assertEqual(out[0]["result"]["serverInfo"]["name"], "tracer-design-catalog")
        self.assertEqual(len(out[1]["result"]["tools"]), len(cs.TOOLS))
        self.assertIn("govuk-frontend", out[2]["result"]["content"][0]["text"])
        self.assertTrue(out[3]["result"]["isError"])


if __name__ == "__main__":
    unittest.main()


class Limits(unittest.TestCase):
    def test_every_system_has_limits(self):
        for s in cs.load("systems.json")["systems"]:
            with self.subTest(s["id"]):
                self.assertTrue(s["limits"]["fixed"])
                for p in s.get("css_tokens", {}).get("prefixes", []):
                    self.assertTrue(p.startswith("--") and p.endswith("-"), p)

    def test_a_row_on_a_fixed_part_is_refused(self):
        table = "| Base token or rule | Base value | Overlay value | Reason |\n| --- | --- | --- | --- |\n| spacing scale | 8px steps | 10px steps | roomier |\n"
        r = cs.check_overlay("carbon", table)
        self.assertTrue(any("keeps fixed" in p for p in r["problems"]), r["problems"])

    def test_a_system_used_as_published_refuses_any_row(self):
        table = "| Base token or rule | Base value | Overlay value | Reason |\n| --- | --- | --- | --- |\n| link color | #1d70b8 | #6929c4 | brand |\n"
        self.assertFalse(cs.check_overlay("govuk", table)["ok"])

    def test_brief_tells_how_to_check_the_render(self):
        md = cs.design_system_brief("carbon")["markdown"]
        self.assertIn('check_design_system', md)
        self.assertIn('"--cds-"', md)
        self.assertIn("Fixed by the base", md)
