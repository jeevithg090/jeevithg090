#!/usr/bin/env python3
"""Render a GitHub-style contribution calendar as light and dark SVGs.

Reads the public contribution calendar for a user (the same data GitHub shows on
the profile page, including private contributions when the profile setting is on)
and draws it with GitHub's own colours. Standard library only.

    python3 scripts/contrib_calendar.py --user jeevithg090 --out dist
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
import urllib.request
from pathlib import Path

# GitHub (Primer) contribution colours.
PALETTES = {
    "dark": {
        "levels": ["#151b23", "#033a16", "#196c2e", "#2ea043", "#56d364"],
        "fg": "#f0f6fc", "muted": "#9198a1", "border": "#3d444d",
        "cell_stroke": "#ffffff", "cell_stroke_opacity": "0.05",
    },
    "light": {
        "levels": ["#eff2f5", "#aceebb", "#4ac26b", "#2da44e", "#116329"],
        "fg": "#1f2328", "muted": "#59636e", "border": "#d1d9e0",
        "cell_stroke": "#1f2328", "cell_stroke_opacity": "0.06",
    },
}
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
CELL, GAP = 10, 3
STEP = CELL + GAP
PAD, LABEL_W, TITLE_H, MONTH_H = 16, 30, 34, 20

DAY_TAG = re.compile(r"<td\b[^>]*\bContributionCalendar-day\b[^>]*>", re.I)


def fetch(user: str) -> str:
    req = urllib.request.Request(
        f"https://github.com/users/{user}/contributions",
        headers={"User-Agent": "contribution-calendar-renderer"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def _attr(tag: str, name: str) -> str | None:
    m = re.search(rf'\b{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def parse(page: str) -> tuple[dict[dt.date, int], str]:
    days: dict[dt.date, int] = {}
    for tag in DAY_TAG.findall(page):
        date, level = _attr(tag, "data-date"), _attr(tag, "data-level")
        if date and level is not None and level.isdigit():
            days[dt.date.fromisoformat(date)] = min(int(level), 4)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", page))
    m = re.search(r"([\d,]+) contributions? in the last year", text)
    total = m.group(1) if m else f"{len(days)} days of"
    return days, total


def render(days: dict[dt.date, int], total: str, theme: str, updated: dt.date) -> str:
    pal = PALETTES[theme]
    start = min(days)
    first_sunday = start - dt.timedelta(days=(start.weekday() + 1) % 7)
    weeks = (max(days) - first_sunday).days // 7 + 1

    grid_x = PAD + LABEL_W
    grid_y = TITLE_H + PAD + MONTH_H
    width = grid_x + weeks * STEP - GAP + PAD
    legend_y = grid_y + 7 * STEP - GAP + 22
    height = legend_y + PAD

    title = f"{total} contributions in the last year"
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'role="img" aria-label="{html.escape(title)}" font-family="{FONT}">',
        f"<title>{html.escape(title)}</title>",
        f'<text x="1" y="22" font-size="16" fill="{pal["fg"]}">{html.escape(title)}</text>',
        f'<rect x="0.5" y="{TITLE_H + 0.5}" width="{width - 1}" height="{height - TITLE_H - 1}" rx="6" '
        f'fill="none" stroke="{pal["border"]}"/>',
    ]

    # Month labels: at the first column whose first day starts a new month.
    last_label_col, prev_month = -10, None
    for w in range(weeks):
        col_start = max(first_sunday + dt.timedelta(days=7 * w), start)
        if col_start.month != prev_month:
            prev_month = col_start.month
            if w - last_label_col >= 3 and w <= weeks - 3:
                out.append(
                    f'<text x="{grid_x + w * STEP}" y="{grid_y - 8}" font-size="12" fill="{pal["fg"]}">'
                    f'{col_start.strftime("%b")}</text>'
                )
                last_label_col = w

    for row, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        out.append(
            f'<text x="{PAD}" y="{grid_y + row * STEP + CELL - 1}" font-size="12" fill="{pal["fg"]}">{name}</text>'
        )

    stroke = f'stroke="{pal["cell_stroke"]}" stroke-opacity="{pal["cell_stroke_opacity"]}"'
    for day, level in sorted(days.items()):
        w = (day - first_sunday).days // 7
        r = (day.weekday() + 1) % 7
        out.append(
            f'<rect x="{grid_x + w * STEP}" y="{grid_y + r * STEP}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{pal["levels"][level]}" {stroke}><title>{day.isoformat()}</title></rect>'
        )

    # Footer: last updated (left) and the Less/More legend (right).
    out.append(
        f'<text x="{grid_x}" y="{legend_y}" font-size="12" fill="{pal["muted"]}">'
        f'Updated {updated.strftime("%-d %b %Y")}</text>'
    )
    more_x = width - PAD
    out.append(f'<text x="{more_x}" y="{legend_y}" font-size="12" fill="{pal["muted"]}" text-anchor="end">More</text>')
    sq_right = more_x - 36
    for i, colour in enumerate(reversed(pal["levels"])):
        x = sq_right - (i + 1) * STEP + GAP
        out.append(
            f'<rect x="{x}" y="{legend_y - CELL}" width="{CELL}" height="{CELL}" rx="2" fill="{colour}" {stroke}/>'
        )
    less_x = sq_right - 5 * STEP + GAP - 6
    out.append(f'<text x="{less_x}" y="{legend_y}" font-size="12" fill="{pal["muted"]}" text-anchor="end">Less</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--user", required=True, help="GitHub username")
    ap.add_argument("--out", default="dist", help="output directory (default: dist)")
    ap.add_argument("--html", help="read the calendar from a saved HTML file instead of GitHub")
    args = ap.parse_args()

    page = Path(args.html).read_text(encoding="utf-8") if args.html else fetch(args.user)
    days, total = parse(page)
    if len(days) < 300:
        print(f"error: parsed only {len(days)} days from the calendar; refusing to publish", file=sys.stderr)
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    today = dt.datetime.now(dt.timezone.utc).date()
    for theme in PALETTES:
        (out / f"contributions-{theme}.svg").write_text(render(days, total, theme, today), encoding="utf-8")
    print(f"rendered {len(days)} days, {total} contributions -> {out}/contributions-{{dark,light}}.svg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
