"""Every skill of the plugin meets the Agent Skills spec (anthropics/skills' validator), with the
keys Claude Code itself reads on a plugin's skills. Run: python3 -m unittest discover plugin/mcp"""

import re
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "skills"
KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility",
        "argument-hint", "disable-model-invocation", "model", "user-invocable"}


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError("no frontmatter")
    out, key = {}, None
    for line in match.group(1).splitlines():
        if line.startswith((" ", "\t")) and key:
            out[key] += " " + line.strip()
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise AssertionError(f"not a key: {line!r}")
        value = value.strip()
        if value and value[0] not in "'\"|>" and (": " in value or " #" in value):
            raise AssertionError(f"{key}: a plain value YAML cannot parse")
        out[key] = "" if value in (">-", ">", "|", "|-") else value.strip("'\"")
    return out


class Skills(unittest.TestCase):
    def test_every_skill_meets_the_spec(self):
        found = sorted(SKILLS.glob("*/SKILL.md"))
        self.assertTrue(found)
        for path in found:
            with self.subTest(path.parent.name):
                meta = frontmatter(path.read_text(encoding="utf-8"))
                self.assertLessEqual(set(meta), KEYS)
                self.assertEqual(meta.get("name"), path.parent.name)
                self.assertRegex(meta["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
                self.assertTrue(0 < len(meta.get("description", "")) <= 1024)
                self.assertNotRegex(meta["description"], r"[<>]")
                self.assertLess(path.read_text(encoding="utf-8").count("\n"), 500)


if __name__ == "__main__":
    unittest.main()
