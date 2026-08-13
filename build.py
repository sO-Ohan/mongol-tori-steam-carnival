#!/usr/bin/env python3
"""Assemble the Mongol-Tori deck from deck.src.html + local assets.

Everything (fonts, photos, sponsor wall) is inlined as data: URIs or inline SVG,
so the result is a single file that works offline with no network access.

Two outputs, same content:

  index.html  a complete HTML document — this is what gets hosted / opened locally
  deck.html   body-only fragment for publishing as a Claude Artifact, whose
              wrapper supplies <!doctype>, <html>, <head> and <body> itself

Requires ImageMagick (`magick`) for the photo optimisation step, which is cached
in build/ and skipped when the optimised file is newer than its source.
"""
import base64, json, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).parent
IMG_SRC = ROOT / "images"
ASSETS = ROOT / "assets"
BUILD = ROOT / "build"

# slide role -> source photo in images/
IMAGES = {
    "IMG_HERO": "WhatsApp Image 2026.28.20 PM.jpeg",            # rover + lander, wide -> title
    "IMG_TEAM": "WhatsApp Image 2026-08-13 PM.jpeg",            # team at the MDRS sign -> who we are
    "IMG_LANDER": "WhatsApp Image 2026-08-13 at 2.28.20 PM.jpeg",  # working at the lander -> the competition
    "IMG_ROVER": "WhatsApp Image 2 at 2.28.21 PM.jpeg",         # rover 3/4, arm up -> meet Taurus
    "IMG_ARM": "WhatsApp Image t 2.28.22 PM.jpeg",              # gripper close-up -> the arm
    "IMG_MAST": "WhatsA2026-08-13 at 2.28.21 PM.jpeg",          # antenna mast -> antennas
    "IMG_WIDE": "WhatsApp Image 2026-08-13 at 2.M.jpeg",        # wide sky -> close
}

# a projected slide never needs more than this; keeps the whole deck under ~4 MB
MAX_PX = 1280
QUALITY = 66

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
"""


def optimise(token: str, filename: str) -> pathlib.Path:
    src = IMG_SRC / filename
    if not src.exists():
        sys.exit(f"missing photo for {token}: {src}")
    BUILD.mkdir(exist_ok=True)
    out = BUILD / f"{token.lower()}.jpg"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    subprocess.run(
        ["magick", str(src), "-auto-orient", "-resize", f"{MAX_PX}x{MAX_PX}>", "-strip",
         "-sampling-factor", "4:2:0", "-quality", str(QUALITY),
         "-define", "jpeg:dct-method=float", "-interlace", "JPEG", str(out)],
        check=True,
    )
    return out


def data_uri(path: pathlib.Path) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


def sponsor_svg() -> str:
    svg = (ASSETS / "sponsors.svg").read_text(encoding="utf8")
    # crop the export's generous empty margin so the logos fill the slide,
    # and let it scale to its container
    return svg.replace(
        '<svg width="4320" height="1463" viewBox="0 0 4320 1463"',
        '<svg viewBox="370 250 3600 930" role="img" '
        'aria-label="Logos of the 23 partners and sponsors of BRACU Mongol-Tori" '
        'style="width:100%;height:auto;display:block"',
        1,
    )


def main() -> int:
    if not shutil.which("magick"):
        sys.exit("ImageMagick (`magick`) is required to optimise the photos")

    html = (ROOT / "deck.src.html").read_text(encoding="utf8")
    html = html.replace("/*{{FONTS}}*/", (ASSETS / "fonts.css").read_text(encoding="utf8"), 1)

    for token, filename in IMAGES.items():
        html = html.replace("{{" + token + "}}", data_uri(optimise(token, filename)))

    notes = json.loads((ROOT / "notes.json").read_text(encoding="utf8"))
    html = html.replace("{{NOTES}}", json.dumps(notes, ensure_ascii=False), 1)
    html = html.replace("{{SPONSORS_SVG}}", sponsor_svg(), 1)

    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        sys.exit("unreplaced tokens: " + ", ".join(sorted(set(left))))

    # fragment for the Artifact wrapper
    (ROOT / "deck.html").write_text(html, encoding="utf8")

    # standalone document for hosting and for opening straight off disk;
    # without a doctype the browser renders in quirks mode
    split = html.index("</style>") + len("</style>")  # charset, title and the stylesheet go in <head>
    standalone = HEAD + html[:split] + "\n</head>\n<body>\n" + html[split:] + "\n</body>\n</html>\n"
    (ROOT / "index.html").write_text(standalone, encoding="utf8")

    for name in ("deck.html", "index.html"):
        size = (ROOT / name).stat().st_size / 1024 / 1024
        print(f"wrote {name}  ({size:.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
