#!/usr/bin/env python3
"""TRACER design catalog: an MCP server over stdio, standard library only.

It answers from the catalog in ../catalog: documented design systems
(systems.json) and visual styles (styles.json). It never invents a design
system: a style is always applied as a brand overlay on a documented one, and
an overlay is checked against the base it changes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from team import assign as team_assign, team_balance  # noqa: E402

CATALOG = Path(__file__).resolve().parent.parent / "catalog"
PROTOCOL = "2025-06-18"
VERSION = "0.12.0"

# Rules a brand overlay may never weaken: they are the base system's
# accessibility and behaviour, not its look.
PROTECTED = {
    "focus": "visible keyboard focus",
    "contrast": "text and control contrast",
    "target": "touch target size",
    "label": "labels and accessible names",
    "motion": "reduced-motion handling",
    "error": "error messages and validation behaviour",
    "spacing scale": "the spacing scale",
    "grid": "the layout grid",
}
WEAKEN = re.compile(r"\b(remove|drop|disable|hide|no|without|ignore|skip|reduce)\b", re.I)
HEX = re.compile(r"#(?:[0-9a-fA-F]{3}){1,2}\b")


def load(name: str) -> dict:
    return json.loads((CATALOG / name).read_text(encoding="utf-8"))


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9.+#-]+", text.lower()) if len(w) > 1}


# --- Contrast (WCAG 2.x relative luminance) ---------------------------------

def _channel(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(f"not a hex color: {hex_color!r}")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast(fg: str, bg: str) -> float:
    a, b = sorted((luminance(fg), luminance(bg)), reverse=True)
    return round((a + 0.05) / (b + 0.05), 2)


def check_contrast(foreground: str, background: str) -> dict:
    ratio = contrast(foreground, background)
    return {
        "foreground": foreground,
        "background": background,
        "ratio": ratio,
        "AA_text": ratio >= 4.5,
        "AA_large_text": ratio >= 3.0,
        "AA_non_text": ratio >= 3.0,
        "AAA_text": ratio >= 7.0,
        "AAA_large_text": ratio >= 4.5,
    }


# --- Catalog queries ---------------------------------------------------------

def list_categories() -> dict:
    systems = load("systems.json")
    styles = load("styles.json")
    return {
        "system_categories": {
            cat: {"means": text, "systems": [s["id"] for s in systems["systems"] if cat in s["categories"]]}
            for cat, text in systems["categories"].items()
        },
        "style_families": {s["id"]: s["name"] for s in styles["styles"]},
        "checked": systems["checked"],
    }


def _score(entry: dict, ctx: set[str], text: str) -> tuple[int, list[str]]:
    score, why = 0, []
    for fit in entry.get("fits", []):
        if fit in text or words(fit) <= ctx:
            score += 3
            why.append(f"fits '{fit}'")
    for cat in entry.get("categories", []):
        if words(cat.replace("-", " ")) & ctx:
            score += 2
            why.append(f"category {cat}")
    for avoid in entry.get("avoid_for", []):
        hit = words(avoid) & ctx - {"the", "and", "for", "that", "not", "is", "be"}
        if len(hit) >= 2:
            score -= 4
            why.append(f"but: avoid for {avoid}")
    return score, why


def search_design_systems(context: str, platform: str = "", category: str = "",
                          japanese: bool = False, limit: int = 5) -> dict:
    text = context.lower()
    ctx = words(context)
    found = []
    for s in load("systems.json")["systems"]:
        if platform and platform.lower() not in s["platforms"]:
            continue
        if category and category not in s["categories"]:
            continue
        if japanese and "japanese" not in s["categories"]:
            continue
        score, why = _score(s, ctx, text)
        found.append({"id": s["id"], "name": s["name"], "owner": s["owner"], "docs": s["docs"],
                      "score": score, "why": why or ["no keyword in common: weak match"],
                      "license_note": s.get("license_note")})
    found.sort(key=lambda r: (-r["score"], r["id"]))
    result = [r for r in found if r["score"] > 0][:limit] or found[:limit]
    return {
        "context": context,
        "results": result,
        "note": "Ranking by the context's words only. Choose with the outcome owner, read the system's own documentation, and record the choice in docs/tracer/design-system.md.",
    }


def get_design_system(id: str) -> dict:
    for s in load("systems.json")["systems"]:
        if s["id"] == id:
            return {**s, "checked": load("systems.json")["checked"]}
    raise KeyError(f"no design system '{id}'; see list_categories")


def search_styles(context: str, limit: int = 3) -> dict:
    text = context.lower()
    ctx = words(context)
    found = []
    for st in load("styles.json")["styles"]:
        score, why = _score(st, ctx, text)
        for m in st["members"]:
            if m in text:
                score += 5
                why.append(f"names '{m}'")
        found.append({"id": st["id"], "name": st["name"], "score": score, "why": why,
                      "carriers": st["carriers"], "risks": st["risks"]})
    found.sort(key=lambda r: (-r["score"], r["id"]))
    return {"context": context, "results": [r for r in found if r["score"] > 0][:limit],
            "note": "A style is never a design system: apply it as a brand overlay on one of its carriers."}


def get_style(id: str) -> dict:
    styles = load("styles.json")
    for st in styles["styles"]:
        if st["id"] == id or id in st["members"]:
            return {**st, "about": styles["about"]}
    raise KeyError(f"no style '{id}'; see list_categories")


def design_system_brief(system: str, style: str = "") -> dict:
    s = get_design_system(system)
    st = get_style(style) if style else None
    lines = [
        "# Design system",
        "",
        f"Base: **{s['name']}** by {s['owner']} — {s['docs']}",
        f"Catalog checked: {s['checked']} (packages and licenses from the npm registry)",
        "",
        "## Packages",
        "",
        "| Package | Role | License |",
        "| --- | --- | --- |",
    ]
    lines += [f"| `{p['name']}` | {p['role']} | {p['license']} |" for p in s["packages"]] or ["| (native platform, no package) | | |"]
    lines += [
        "",
        "## What the base decides",
        "",
        "Every rule of the base system holds unless a row of the overlay below changes it. "
        "Components, behaviour, accessibility, spacing scale and grid come from the base and its documentation, never from memory.",
        "",
        f"Theming in this system: {s['theming']}",
        "",
        "A brand may adjust: " + ("; ".join(s["limits"]["adjustable"]) or "nothing") + ".",
        "Fixed by the base: " + "; ".join(s["limits"]["fixed"]) + ".",
        f"Japanese and CJK text: {s.get('cjk', 'not stated')}",
    ]
    if s.get("license_note"):
        lines += ["", f"**License:** {s['license_note']}"]
    if st:
        lines += [
            "",
            f"## Style: {st['name']}",
            "",
            "Traits the overlay brings: " + "; ".join(st["traits"]) + ".",
            "",
            "Risks to check in every slice:",
            *[f"- {r}" for r in st["risks"]],
        ]
        if system not in st["carriers"]:
            lines += ["", f"Note: {s['name']} is not one of this style's usual carriers ({', '.join(st['carriers'])}). Say why it was chosen."]
    css = s.get("css_tokens")
    lines += [
        "",
        "## Checking the render",
        "",
        "Every slice with an interface runs layout-inspector's `check_design_system` on its screens"
        + (f" with `token_prefixes` {json.dumps(css['prefixes'])} (read from `{css['read_from']}`)" if css else
           ", passing the system's values in `extra_tokens` (this system's tokens are not CSS custom properties with one prefix)")
        + " and every overlay value in `extra_tokens`. Contrast failures block; an off-token value is a missing overlay row or a hand-made style.",
    ]
    lines += [
        "",
        "## Brand overlay",
        "",
        "Only the changes. Each row names the base token or rule it changes; nothing here may weaken focus, contrast, target size, labels, motion handling or error behaviour.",
        "",
        "| Base token or rule | Base value | Overlay value | Reason |",
        "| --- | --- | --- | --- |",
        "| | | | |",
    ]
    return {"markdown": "\n".join(lines) + "\n", "write_to": "docs/tracer/design-system.md"}


def _fixed_hit(rule: str, fixed: list[str]) -> str | None:
    """The fixed part of the base a row's rule names, if any."""
    low = rule.lower()
    for item in fixed:
        if item.startswith("everything"):
            return item
        core = item.split(" (")[0].lower()
        if core and (core in low or all(w in low for w in core.split() if len(w) > 3)):
            return item
    return None


def check_overlay(base: str, overlay: str) -> dict:
    """Read the overlay table of a design-system.md and say what breaks."""
    fixed = get_design_system(base).get("limits", {}).get("fixed", [])
    rows, problems = [], []
    for line in overlay.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or set("".join(cells)) <= set("-: ") or cells[0].lower().startswith("base token"):
            continue
        if not any(cells):
            continue
        rows.append(cells)
        rule, base_value, value, reason = cells[:4]
        if not rule:
            problems.append(f"row '{' | '.join(cells)}': names no base token or rule — an overlay only changes what the base defines")
        if not reason:
            problems.append(f"row '{rule}': no reason")
        hit = _fixed_hit(rule, fixed) if rule else None
        if hit:
            problems.append(f"row '{rule}': changes {hit}, which {base} keeps fixed; use what it lets a brand adjust")
        low = f"{rule} {value}".lower()
        for key, what in PROTECTED.items():
            if key in low and WEAKEN.search(value):
                problems.append(f"row '{rule}': weakens {what}, which the base owns and an overlay may not change")
    pairs = []
    for line in overlay.splitlines():
        m = re.search(r"(#[0-9a-fA-F]{3,6})\s+on\s+(#[0-9a-fA-F]{3,6})", line)
        if m:
            c = check_contrast(m.group(1), m.group(2))
            pairs.append(c)
            if not c["AA_text"]:
                problems.append(f"{m.group(1)} on {m.group(2)}: {c['ratio']}:1 is under AA for text (4.5:1)")
    return {"base": base, "rows": len(rows), "contrast_pairs": pairs, "problems": problems,
            "ok": not problems and bool(rows)}


# --- Genericity: the defaults a generator reaches for -----------------------

_RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
_TAG = re.compile(r"<[^>]+>")


def _blocks(css: str) -> list[tuple[str, str]]:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return [(sel.strip(), body.lower()) for sel, body in _RULE.findall(css)]


def check_genericity(html: str, css: str = "") -> dict:
    """Count the traits of the "Identity, not template" family in a page's markup and styles.

    A count above its limit is a question for the builder, not a verdict: each
    finding names the catalog entry and asks for the reason from the client's
    world. Styles inside <style> elements of the html are read too.
    """
    styles = css + "\n" + "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    blocks = _blocks(styles)
    body = re.sub(r"<(script|style|title)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
    text = re.sub(r"\s+", " ", _TAG.sub(" ", body))
    counts = {
        "eyebrow labels": sum(1 for _, b in blocks if "uppercase" in b and "letter-spacing" in b),
        "middle-dot metadata": len(re.findall(r"\S\s+[·•]\s+\S", text)),
        "decorative monospace": len({b for _, b in blocks if re.search(r"font-family:[^;]*mono", b)}),
        "entrance effects": len(re.findall(r"@keyframes", styles, re.I))
        + len(re.findall(r"animation-timeline\s*:\s*view", styles, re.I)),
        "motion on its own": len(re.findall(r"\binfinite\b", styles, re.I)),
        "hover on every card": sum(1 for sel, b in blocks if ":hover" in sel and re.search(r"transform|box-shadow|translate|scale", b)),
        "arrows glued to buttons": len(re.findall(r"<(?:a|button)\b[^>]*>[^<]*(?:→|->|&rarr;)\s*</(?:a|button)>", html, re.I)),
        "orphans in a grid": len(re.findall(r"repeat\(\s*auto-(?:fit|fill)", styles, re.I)),
        "numbering without a sequence": len(re.findall(r"(?<![\d.,])0[1-9](?![\d.,%])", text)),
        "one word in color": len(re.findall(r"<h[1-3][^>]*>[^<]*<(?:em|span|strong|i)\b[^>]*>[^<]{1,24}</(?:em|span|strong|i)>[^<]*</h[1-3]>", html, re.I)),
    }
    shadows = {}
    for _, b in blocks:
        m = re.search(r"box-shadow:([^;]+)", b)
        r = re.search(r"border-radius:([^;]+)", b)
        if m and r:
            key = (m.group(1).strip(), r.group(1).strip())
            shadows[key] = shadows.get(key, 0) + 1
    counts["same card everywhere"] = max(shadows.values(), default=0)
    limits = {"eyebrow labels": 1, "middle-dot metadata": 1, "decorative monospace": 0, "entrance effects": 2,
              "motion on its own": 0, "hover on every card": 2, "arrows glued to buttons": 0, "orphans in a grid": 0,
              "numbering without a sequence": 3, "one word in color": 0, "same card everywhere": 3}
    findings = [{"entry": k, "count": counts[k], "limit": limits[k],
                 "ask": f"Name the reason for each from the client's world or the audience's task, or remove it ('{k}' in the anti-pattern catalog, family 14)."}
                for k in counts if counts[k] > limits[k]]
    return {"counts": counts, "findings": findings, "ok": not findings,
            "note": "Heuristics on the source, not the render: a finding is a question; the verifier still walks the page."}


# --- MCP over stdio ----------------------------------------------------------

def _schema(props: dict, required: list[str]) -> dict:
    return {"type": "object", "properties": props, "required": required, "additionalProperties": False}


S = {"type": "string"}
A = {"type": "array", "items": {"type": "object"}}
TOOLS = {
    "list_categories": (list_categories, "List the catalog's categories of documented design systems and its style families.", _schema({}, [])),
    "search_design_systems": (search_design_systems,
        "Rank documented design systems for a product context (audience, product type, density, language, platform). Returns reasons; the choice is the outcome owner's.",
        _schema({"context": S, "platform": S, "category": S, "japanese": {"type": "boolean"}, "limit": {"type": "integer"}}, ["context"])),
    "get_design_system": (get_design_system, "One documented design system: owner, documentation, packages and licenses, how it is themed.", _schema({"id": S}, ["id"])),
    "search_styles": (search_styles, "Rank visual styles for a context. A style is applied as a brand overlay on a documented system, never as a system.", _schema({"context": S, "limit": {"type": "integer"}}, ["context"])),
    "get_style": (get_style, "One visual style: traits, fits, accessibility risks and the systems that can carry it.", _schema({"id": S}, ["id"])),
    "design_system_brief": (design_system_brief, "The starting text of docs/tracer/design-system.md for a base system and an optional style: sources, packages, licenses and an empty overlay table.", _schema({"system": S, "style": S}, ["system"])),
    "check_overlay": (check_overlay, "Check a brand overlay table against its base: every row names a base rule, has a reason, weakens no protected rule, and every 'X on Y' color pair passes AA.", _schema({"base": S, "overlay": S}, ["base", "overlay"])),
    "check_genericity": (check_genericity, "Count the traits of the anti-pattern family 'Identity, not template' in a page's HTML and CSS (eyebrow labels, middle dots, decorative monospace, entrance effects, endless motion, hover on every card, arrows in buttons, auto-fit grids, fake numbering, one word in color, one card style everywhere). Each count over its limit is a question for the builder.", _schema({"html": S, "css": S}, ["html"])),
    "team_assign": (team_assign, "Teams adaptation: assign cards (C, R, repositories, type) to people by lowest expected time within capacity, free margin, responsibility ceiling (role and repository expertise) and budget; gives the relay, the checks, co-holders and rotation cards.", _schema({"people": A, "repos": {"type": "object"}, "cards": A, "rotation": {"type": "number"}}, ["people", "repos", "cards"])),
    "team_balance": (team_balance, "Teams adaptation: nominal and worst-case velocity (without the most critical person), bus factor of critical repositories, and the speed / cruise / balance mode for the next sprint with its rotation share.", _schema({"people": A, "repos": {"type": "object"}, "cards": A, "slip": {"type": "number"}, "mode": S, "x": {"type": "number"}, "y": {"type": "number"}}, ["people", "repos", "cards"])),
    "check_contrast": (check_contrast, "WCAG contrast ratio of two hex colors, with AA and AAA verdicts.", _schema({"foreground": S, "background": S}, ["foreground", "background"])),
}


def handle(msg: dict) -> dict | None:
    method, mid = msg.get("method"), msg.get("id")
    if mid is None:
        return None  # a notification
    if method == "initialize":
        version = msg.get("params", {}).get("protocolVersion") or PROTOCOL
        result = {"protocolVersion": version, "capabilities": {"tools": {}},
                  "serverInfo": {"name": "tracer-design-catalog", "version": VERSION}}
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": [{"name": n, "description": d, "inputSchema": s, "annotations": {"readOnlyHint": True}}
                            for n, (_, d, s) in TOOLS.items()]}
    elif method == "tools/call":
        params = msg.get("params", {})
        name = params.get("name")
        if name not in TOOLS:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"unknown tool {name}"}}
        try:
            out = TOOLS[name][0](**(params.get("arguments") or {}))
            result = {"content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False, indent=2)}]}
        except (KeyError, ValueError, TypeError) as exc:
            result = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
    else:
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"method not found: {method}"}}
    return {"jsonrpc": "2.0", "id": mid, "result": result}


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}
        else:
            reply = handle(msg)
        if reply is not None:
            sys.stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
