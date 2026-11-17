"""TRACER teams adaptation: assignment, relay and speed/balance mode (docs/adaptations/teams.md).

Standard library only. Inputs are plain dicts so the MCP server can pass JSON straight in.
"""

from __future__ import annotations

LEVELS = {"new": 2.0, "guided": 1.4, "autonomous": 1.0, "reference": 0.8}
CEILING = {"new": 2, "guided": 3}
INTEGRATION = 0.2


def effective_r(card: dict, repos: dict) -> int:
    return max([card["r"]] + [repos.get(r, {}).get("r_floor", 1) for r in card["repos"]])


def expected_time(card: dict, person: dict, repos: dict) -> float:
    total = 0.0
    for r in card["repos"]:
        level = person.get("expertise", {}).get(r, "new")
        factor = person.get("repo_factor", {}).get(r, LEVELS[level])
        total += card["c"] / len(card["repos"]) * repos.get(r, {}).get("k", 1.0) * factor
    total *= person.get("type_factor", {}).get(card.get("type", "execution"), 1.0)
    return round(total * (1 + INTEGRATION * (len(card["repos"]) - 1)), 2)


def r_ceiling(person: dict, card: dict) -> int:
    ceil = person["r_max"]
    for r in card["repos"]:
        ceil = min(ceil, CEILING.get(person.get("expertise", {}).get(r, "new"), ceil))
    return ceil


def checks(r: int) -> list[float]:
    return [0.5] if r <= 2 else [0.4, 0.7] if r == 3 else [0.25, 0.5, 0.75]


def _free(p: dict) -> float:
    return p["h"] * (1 - p.get("margin", 0.2))


def assign(people: list[dict], repos: dict, cards: list[dict], rotation: float = 0.2) -> dict:
    """Assign each card (highest effective R first) to the eligible person with the lowest expected time.

    people: {name, h (hours this sprint), margin, r_max, budget, expertise{repo: level}, repo_factor{}, type_factor{}}
    repos:  {name: {k, r_floor, critical}}
    cards:  {id, c, r, repos[], type}
    """
    load = {p["name"]: 0.0 for p in people}
    rload = {p["name"]: 0 for p in people}
    out, rotated, low = [], 0, 0
    for card in sorted(cards, key=lambda c: -effective_r(c, repos)):
        er = effective_r(card, repos)
        rows = []
        for p in people:
            t = expected_time(card, p, repos)
            fits = load[p["name"]] + t <= _free(p) and rload[p["name"]] + er <= p.get("budget", 99)
            rows.append((t, p, fits, er <= r_ceiling(p, card)))
        eligible = sorted([r for r in rows if r[2] and r[3]], key=lambda r: r[0])
        entry = {"card": card["id"], "effective_r": er, "checks": checks(er)}
        if er <= 2:
            low += 1
        learners = [r for r in eligible if any(p_lvl in ("new", "guided") for p_lvl in
                    (r[1].get("expertise", {}).get(x, "new") for x in card["repos"]))]
        if er <= 2 and learners and rotated < rotation * max(low, 1):
            chosen, rotated = learners[0], rotated + 1
            entry["rotation"] = True
        elif eligible:
            chosen = eligible[0]
        else:
            capacity_only = sorted([r for r in rows if r[2]], key=lambda r: r[0])
            holders = [r for r in rows if r[3] and r[1]["r_max"] >= er]
            if capacity_only and holders:
                chosen = capacity_only[0]
                entry["co_holder"] = holders[0][1]["name"]
            else:
                entry["unassigned"] = "nobody fits: split the card, move it or replan with the PO"
                out.append(entry)
                continue
        t, p = chosen[0], chosen[1]
        load[p["name"]] += t
        rload[p["name"]] += er
        relay = [r[1]["name"] for r in sorted(rows, key=lambda r: r[0]) if r[1]["name"] != p["name"] and r[3]][:2]
        if len(relay) < 2:
            entry["relay_gap"] = "fewer than two others may hold this card: the relay ends at the LT; raise the bus factor"
        relay.append("LT")
        entry.update({"primary": p["name"], "expected_time": t, "relay": relay})
        out.append(entry)
    return {"assignments": out, "load": load,
            "rule": "Relay A → B → C → LT, never back to A. A missed check reassigns at that moment."}


def velocity(people: list[dict], repos: dict, cards: list[dict]) -> float:
    """Cards' complexity deliverable in the sprint, assigning each to the fastest person with capacity."""
    load = {p["name"]: 0.0 for p in people}
    done = 0.0
    for card in sorted(cards, key=lambda c: -effective_r(c, repos)):
        best = None
        for p in people:
            t = expected_time(card, p, repos)
            if load[p["name"]] + t <= _free(p) and (best is None or t < best[0]):
                best = (t, p["name"])
        if best:
            load[best[1]] += best[0]
            done += card["c"]
    return done


def bus_factor(people: list[dict], repo: str) -> int:
    return sum(1 for p in people if p.get("expertise", {}).get(repo) in ("autonomous", "reference"))


def team_balance(people: list[dict], repos: dict, cards: list[dict], slip: float = 0.0,
                 mode: str = "cruise", x: float = 0.10, y: float = 0.60) -> dict:
    """Nominal and worst-case velocity, bus factors and the mode for the next sprint (with hysteresis).

    slip: how far the forecast is behind the committed date, as a share (0.15 = 15 % late).
    """
    nominal = velocity(people, repos, cards)
    worst, without = nominal, None
    for p in people:
        v = velocity([q for q in people if q is not p], repos, cards)
        if v < worst:
            worst, without = v, p["name"]
    ratio = worst / nominal if nominal else 1.0
    buses = {r: bus_factor(people, r) for r, info in repos.items() if info.get("critical")}
    exposed = [r for r, n in buses.items() if n < 2]
    why = []
    if ratio < y or exposed:
        nxt = "balance"
        why.append(f"worst-case velocity is {ratio:.0%} of nominal" if ratio < y else f"bus factor under 2 in {exposed}")
        if slip > x:
            why.append("balance wins over speed unless the company records otherwise")
    elif slip > x:
        nxt, _ = "speed", why.append(f"forecast {slip:.0%} late")
    elif mode == "speed" and slip > x / 2:
        nxt, _ = "speed", why.append("still late beyond X/2")
    elif mode == "balance" and ratio < y + 0.10:
        nxt, _ = "balance", why.append("worst-case not yet above Y + 10 %")
    else:
        nxt, _ = "cruise", why.append("within thresholds")
    rotation = {"speed": 0.075, "cruise": 0.20, "balance": 0.35}[nxt]
    return {"nominal_velocity": nominal, "worst_case_velocity": worst, "without": without,
            "worst_case_share": round(ratio, 2), "bus_factor": buses, "mode": nxt, "why": why,
            "rotation_share": rotation,
            "note": "Change the mode only at the end of a sprint or slice. Critical repositories keep a bus factor of 2 in every mode."}
