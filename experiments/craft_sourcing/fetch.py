#!/usr/bin/env python3
"""Acquire a craft-source corpus into a local, gitignored staging area.

Part of the craft-sourcing process (docs/reference/craft-sourcing.md). Takes a
source manifest (YAML-ish, but plain JSON to stay stdlib-only) describing where a
teacher's corpus lives, pulls it down, normalizes every item to plain text with a
locator, and records provenance (sha256, size, words) so a dossier claim can always
be traced back to a file.

Deliberately stdlib + external binaries only: this is eval/dev tooling and must not
add a dependency to the torch-free `prosodia` authoring install.

Requires: curl, and for YouTube items a `yt-dlp` on PATH or at --ytdlp.
Optional: pdftotext (poppler) for PDF items.

Usage:
    python fetch.py sources/fisher.json [--ytdlp /path/to/yt-dlp]
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus"


# A bare `curl -A Mozilla/...` is refused by several academic hosts (PubPub, OAPEN, SSRN,
# Open Yale) that accept an ordinary browser. Sending a realistic header set is the difference
# between "licence problem" and "fetch-mechanics problem" — it is nearly always the latter.
BROWSER_HEADERS = [
    "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/141.0 Safari/537.36",
    "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "-H", "Accept-Language: en-GB,en;q=0.9",
    "-H", "Sec-Fetch-Mode: navigate",
    "-H", "Sec-Fetch-Site: none",
]


def sh(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False, **kw)


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()[:16]


def vtt_to_text(vtt: Path) -> tuple[str, list[tuple[float, float, str]]]:
    """Return (plain text, cues). Handles both manual and auto-generated VTT."""
    cues: list[tuple[float, float, str]] = []
    raw = vtt.read_text(encoding="utf-8", errors="replace")
    for block in raw.split("\n\n"):
        m = re.search(r"(\d+):(\d+):([\d.]+)\s*-->\s*(\d+):(\d+):([\d.]+)", block)
        if not m:
            continue
        start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
        end = int(m.group(4)) * 3600 + int(m.group(5)) * 60 + float(m.group(6))
        body = "\u0001".join(ln for ln in block.split("\n")[1:] if "-->" not in ln)
        body = re.sub(r"<[^>]+>", "", body)  # strip auto-caption word timing tags
        body = re.sub(r"[ \t]+", " ", body)
        body = html.unescape(body).strip("\u0001 ").strip()
        if body:
            cues.append((start, end, body))
    # Auto-captions scroll: cue N shows [A], cue N+1 shows [A, B], cue N+2 shows [B, C].
    # Joining cue bodies naively duplicates almost every line, roughly doubling the text and
    # corrupting every lexical count. Dedupe at LINE level against a short lookback window.
    from collections import deque

    recent: deque[str] = deque(maxlen=12)
    lines_out: list[str] = []
    for _, _, body in cues:
        for line in body.split("\u0001"):
            key = re.sub(r"\s+", " ", line).strip().lower()
            if not key or key in recent:
                continue
            recent.append(key)
            lines_out.append(line.strip())
    return re.sub(r"\s+", " ", " ".join(lines_out)).strip(), cues


def fetch_youtube(item: dict, dest: Path, ytdlp: str) -> list[dict]:
    """Pull subtitle tracks only — never the video. Prefers a manual track."""
    out = []
    vid = item["id"]
    stem = dest / f"{item['slug']}"
    r = sh([ytdlp, "--skip-download", "--write-subs", "--write-auto-subs",
            "--sub-langs", "en.*", "--sub-format", "vtt",
            "-o", str(stem) + ".%(ext)s", f"https://www.youtube.com/watch?v={vid}"])
    if r.returncode != 0:
        print(f"  !! {item['slug']}: yt-dlp failed", file=sys.stderr)
        return out
    # `en` = manual/professional track when present; `en-orig` = auto (word timings)
    for suffix, kind in ((".en.vtt", "manual"), (".en-orig.vtt", "auto")):
        vtt = Path(str(stem) + suffix)
        if not vtt.exists():
            continue
        text, cues = vtt_to_text(vtt)
        txt = Path(str(stem) + f".{kind}.txt")
        txt.write_text(text, encoding="utf-8")
        out.append({
            "slug": item["slug"], "title": item.get("title", ""), "group": item.get("group", ""),
            "kind": f"captions/{kind}", "source": f"youtube:{vid}", "file": txt.name,
            "vtt": vtt.name, "sha256": sha256(txt), "words": len(text.split()),
            "duration_s": round(cues[-1][1] - cues[0][0], 1) if cues else None,
            "cues": len(cues),
        })
    return out


def fetch_pdf(item: dict, dest: Path) -> list[dict]:
    pdf = dest / f"{item['slug']}.pdf"
    if sh(["curl", "-sSL", "--max-time", "120", *BROWSER_HEADERS,
           "-o", str(pdf), item["url"]]).returncode != 0 or not pdf.exists():
        print(f"  !! {item['slug']}: download failed", file=sys.stderr)
        return []
    txt = dest / f"{item['slug']}.txt"
    if shutil.which("pdftotext"):
        sh(["pdftotext", "-layout", str(pdf), str(txt)])
    if not txt.exists():
        print(f"  !! {item['slug']}: no pdftotext; PDF kept, text not extracted", file=sys.stderr)
        return []
    text = txt.read_text(encoding="utf-8", errors="replace")
    return [{"slug": item["slug"], "title": item.get("title", ""), "kind": "pdf",
             "source": item["url"], "file": txt.name, "sha256": sha256(txt),
             "words": len(text.split())}]


def fetch_html(item: dict, dest: Path) -> list[dict]:
    raw = dest / f"{item['slug']}.html"
    if sh(["curl", "-sSL", "--max-time", "60", *BROWSER_HEADERS,
           "-o", str(raw), item["url"]]).returncode != 0 or not raw.exists():
        print(f"  !! {item['slug']}: download failed", file=sys.stderr)
        return []
    s = raw.read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|"
               r"<footer.*?</footer>|<svg.*?</svg>", " ", s, flags=re.DOTALL)
    s = re.sub(r"</(p|div|li|h[1-6]|tr|blockquote)>", "\\n", s)
    s = re.sub(r"[ \t]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))
    s = re.sub(r"\n\s*\n+", "\\n", s).strip()
    # Publisher chrome (nav labels, export menus, release histories) inflates every word count
    # and pollutes the mined n-grams. Drop the short repeated lines that carry it.
    CHROME = ("skip to main content", "download", "cite", "social", "contents", "show details",
              "last released", "search", "log in", "sign up", "menu", "share", "comments")
    # Some publishers append open peer-review threads to the page. Those are OTHER PEOPLE'S
    # words on the same URL, and a quotation lifted from them would be misattributed to the
    # author. Truncate at the first comment-section marker.
    for marker in ("Login to discuss", "Leave a comment", "Comments (", "Discussion (",
                   "Add a comment"):
        i = s.find(marker)
        if i > 500:
            s = s[:i]
            break
    keep = []
    for line in s.split("\n"):
        ln = line.strip()
        low = ln.lower()
        if len(ln) < 60 and (low in CHROME or low.startswith("release #")
                             or re.match(r"^[\d.]+$", low) or "release #" in low):
            continue
        keep.append(line)
    s = re.sub(r"\n\s*\n+", "\n", "\n".join(keep)).strip()
    txt = dest / f"{item['slug']}.txt"
    txt.write_text(s, encoding="utf-8")
    return [{"slug": item["slug"], "title": item.get("title", ""), "kind": "html",
             "source": item["url"], "file": txt.name, "sha256": sha256(txt),
             "words": len(s.split())}]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--ytdlp", default=shutil.which("yt-dlp") or "yt-dlp")
    args = ap.parse_args()

    spec = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    dest = CORPUS / spec["slug"]
    dest.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    for item in spec["items"]:
        print(f"  .. {item['slug']} ({item['type']})")
        if item["type"] == "youtube":
            records += fetch_youtube(item, dest, args.ytdlp)
        elif item["type"] == "pdf":
            records += fetch_pdf(item, dest)
        elif item["type"] == "html":
            records += fetch_html(item, dest)
        else:
            print(f"  !! unknown item type {item['type']!r}", file=sys.stderr)

    manifest = {
        "slug": spec["slug"], "person": spec["person"], "hired_for": spec.get("hired_for", ""),
        "acquired": date.today().isoformat(), "permission_note": spec.get("permission_note", ""),
        "items": records,
        "totals": {
            "items": len(records),
            "words": sum(r.get("words") or 0 for r in records),
            "audio_minutes": round(sum(r.get("duration_s") or 0 for r in records) / 60, 1),
        },
    }
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    t = manifest["totals"]
    print(f"\n{spec['slug']}: {t['items']} items, {t['words']:,} words, "
          f"{t['audio_minutes']} min -> {dest}/manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
