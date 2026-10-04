"""Rebuild sitemap.xml from indexable HTML pages.

Skips noindex files (the old-address redirects). Uses each page's canonical
URL. lastmod is the date of the last git commit for that file.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://band9ai.org"
SITEMAP = ROOT / "sitemap.xml"
CANONICAL = re.compile(r'<link rel="canonical" href="([^"]+)"')
ROBOTS = re.compile(r'<meta name="robots" content="([^"]+)"')


def lastmod(path: Path) -> str:
    import datetime

    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    date = result.stdout.strip()
    if date:
        return date
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()


def priority(loc: str) -> str:
    if loc.rstrip("/") == ORIGIN:
        return "1.0"
    if loc.rstrip("/").endswith("/ielts") or loc.rstrip("/").endswith("/toefl"):
        return "0.9"
    return "0.8"


def pages() -> list[tuple[str, str]]:
    found: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*.html")):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        robots = ROBOTS.search(text)
        if robots and "noindex" in robots.group(1):
            continue
        canonical = CANONICAL.search(text)
        if canonical:
            loc = canonical.group(1).strip()
        else:
            rel = path.relative_to(ROOT).as_posix()
            if rel == "index.html":
                loc = ORIGIN + "/"
            elif rel.endswith("/index.html"):
                loc = ORIGIN + "/" + rel[: -len("index.html")]
            else:
                loc = ORIGIN + "/" + rel
        if not loc.startswith(ORIGIN):
            continue
        found[loc] = lastmod(path)
    home = ORIGIN + "/"
    ordered = sorted(found, key=lambda loc: (loc != home, loc))
    return [(loc, found[loc]) for loc in ordered]


def render(entries: list[tuple[str, str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, modified in entries:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <lastmod>{modified}</lastmod>",
                "    <changefreq>monthly</changefreq>",
                f"    <priority>{priority(loc)}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    xml = render(pages())
    SITEMAP.write_text(xml, encoding="utf-8", newline="\n")
    print(f"wrote {SITEMAP.relative_to(ROOT)} ({xml.count('<loc>')} urls)")


if __name__ == "__main__":
    main()
