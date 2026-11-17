"""Tests for the teams adaptation. Run: python3 -m unittest discover plugin/mcp"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import team  # noqa: E402

REPOS = {"payments": {"k": 1.5, "r_floor": 4, "critical": True}, "site": {"k": 1.0, "r_floor": 1}}


def person(name, r_max=5, h=40, **exp):
    return {"name": name, "h": h, "margin": 0.2, "r_max": r_max, "budget": 12, "expertise": exp}


class Team(unittest.TestCase):
    def test_repository_floor_raises_r(self):
        self.assertEqual(team.effective_r({"r": 1, "c": 2, "repos": ["payments"]}, REPOS), 4)

    def test_fastest_not_most_senior(self):
        people = [person("senior", r_max=5), person("semi", r_max=4, payments="reference")]
        out = team.assign(people, REPOS, [{"id": "k1", "c": 4, "r": 2, "repos": ["payments"]}])
        self.assertEqual(out["assignments"][0]["primary"], "semi")

    def test_expertise_caps_responsibility(self):
        new = person("new", r_max=5)
        self.assertEqual(team.r_ceiling(new, {"repos": ["payments"]}), 2)

    def test_above_ceiling_needs_a_co_holder(self):
        people = [person("junior", r_max=2, payments="reference"), person("lead", r_max=5, h=1, payments="autonomous")]
        a = team.assign(people, REPOS, [{"id": "k", "c": 4, "r": 4, "repos": ["payments"]}])["assignments"][0]
        self.assertEqual((a["primary"], a["co_holder"]), ("junior", "lead"))

    def test_margin_is_never_planned(self):
        people = [person("a", h=10, site="reference")]
        a = team.assign(people, REPOS, [{"id": "big", "c": 11, "r": 1, "repos": ["site"]}])["assignments"][0]
        self.assertIn("unassigned", a)

    def test_checks_by_responsibility(self):
        self.assertEqual(team.checks(1), [0.5])
        self.assertEqual(len(team.checks(5)), 3)

    def test_concentration_forces_balance(self):
        people = [person("ana", payments="reference"), person("bo"), person("cy")]
        cards = [{"id": f"p{i}", "c": 8, "r": 3, "repos": ["payments"]} for i in range(4)]
        out = team.team_balance(people, REPOS, cards, slip=0.3)
        self.assertEqual(out["mode"], "balance")
        self.assertEqual(out["bus_factor"]["payments"], 1)

    def test_late_and_balanced_goes_to_speed(self):
        people = [person(n, payments="autonomous", site="autonomous") for n in ("ana", "bo", "cy")]
        cards = [{"id": f"s{i}", "c": 4, "r": 1, "repos": ["site"]} for i in range(6)]
        out = team.team_balance(people, REPOS, cards, slip=0.2)
        self.assertEqual(out["mode"], "speed")


if __name__ == "__main__":
    unittest.main()
