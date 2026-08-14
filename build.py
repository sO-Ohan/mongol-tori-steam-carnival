#!/usr/bin/env python3
"""Assemble the Mongol-Tori decks from their .src.html templates + local assets.

Everything (fonts, photos, sponsor wall) is inlined as data: URIs or inline SVG,
so each result is a single file that works offline with no network access.

Two decks, each built twice:

  index.html   / deck.html    the carnival talk — complete document / body-only fragment
  school.html  / school.deck.html   the school talk, same engine, bigger type

The complete documents are what get hosted and opened locally; the fragments are
for publishing as a Claude Artifact, whose wrapper supplies <!doctype>, <html>,
<head> and <body> itself.

A token is only resolved if the template actually uses it, so the two decks share
one image registry without paying for each other's photos.

Requires ImageMagick (`magick`) for the photo optimisation step, which is cached
in build/ and skipped when the optimised file is newer than its source.
"""
import base64, json, pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).parent
ASSETS = ROOT / "assets"
BUILD = ROOT / "build"

# token -> (source photo, longest edge in px)
# full-bleed backgrounds get the larger budget; inset photos need much less
IMAGES = {
    # ---- the carnival deck ----
    "IMG_HERO":       ("images/WhatsApp Image 2026.28.20 PM.jpeg", 1280),          # title
    "IMG_LANDER":     ("images/WhatsApp Image 2026-08-13 at 2.28.20 PM.jpeg", 1280),  # the four missions
    "IMG_WIDE":       ("images/WhatsApp Image 2026-08-13 at 2.M.jpeg", 1280),      # close
    "IMG_TEAM":       ("images/WhatsApp Image 2026-08-13 PM.jpeg", 900),           # who we are
    "IMG_ASTRONAUT":  ("astonoute/austronaute-visit.jpg", 1280),                   # the visit
    "IMG_NAVY":       ("astonoute/navy-visit", 1000),                              # drones
    "IMG_SATEL":      ("astonoute/satel.jpg", 800),                                # the radio link
    "IMG_COMPLETECH": ("astonoute/complitech-and-our-mongotori-enginer-workingon-customcantenan-degine.jpg", 900),
    "IMG_SCHOOL":     ("astonoute/school-outrich.jpg", 900),                       # outreach
    "IMG_KID":        ("astonoute/youne-student-curicity.jpg", 700),               # outreach
    "IMG_CROWD":      ("astonoute/outreach.jpg", 700),                             # outreach

    # ---- the school deck ----
    "SCH_HERO":       ("images/WhatsApp Image 2026.28.20 PM.jpeg", 1280),          # title
    "SCH_ASTRO":      ("astonoute/austronaute-visit.jpg", 1280),                   # the hook
    "SCH_TEAM":       ("images/WhatsApp Image 2026-08-13 PM.jpeg", 900),           # who we are
    "SCH_DESERT":     ("images/WhatsApp Image 2026-08-13 at 2.M.jpeg", 1280),      # this is not Mars
    "SCH_LANDER":     ("images/WhatsApp Image 2026-08-13 at 2.28.20 PM.jpeg", 1280),  # the four jobs
    "SCH_ROVER_TALL": ("images/WhatsApp Image t 2.28.22 PM.jpeg", 1280),           # the torch-beam slide
    "SCH_SATEL":      ("astonoute/satel.jpg", 800),                                # radio
    "SCH_COMPLETECH": ("astonoute/complitech-and-our-mongotori-enginer-workingon-customcantenan-degine.jpg", 900),
    "SCH_NAVY":       ("astonoute/navy-visit", 1000),                              # drones
    "SCH_SCHOOL":     ("astonoute/school-outrich.jpg", 800),                       # your turn
    "SCH_KIDDRIVE":   ("astonoute/kid in schhol with rover.jpg", 800),             # your turn
    "SCH_KIDRIDE":    ("astonoute/kid and roverjpg", 800),                         # your turn
    "SCH_YOUNG":      ("astonoute/youne-student-curicity.jpg", 1280),              # close
}

# graphics that are already the right size — inlined as-is
FILES = {
    "LOGO_FULL":     ("assets/logo-full.png", "image/png"),
    "LOGO_MARK":     ("assets/logo-emblem.png", "image/png"),
    "ROVER_DIAGRAM": ("assets/rover-diagram.png", "image/png"),
    "ADVISOR":       ("assets/advisor.jpg", "image/jpeg"),
    "P_SATEL":       ("assets/partner-satel.png", "image/png"),
    "P_SBG":         ("assets/partner-sbg.png", "image/png"),
    "P_MYACTUATOR":  ("assets/partner-myactuator.png", "image/png"),
    "P_COMPLETECH":  ("assets/partner-completech.png", "image/png"),
}

# (template, speaker notes, body-only fragment, standalone document)
DECKS = [
    ("deck.src.html",   "notes.json",        "deck.html",        "index.html"),
    ("school.src.html", "school-notes.json", "school.deck.html", "school.html"),
]

QUALITY = 66

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
"""


def optimise(token: str, rel: str, max_px: int) -> pathlib.Path:
    src = ROOT / rel
    if not src.exists():
        sys.exit(f"missing photo for {token}: {src}")
    BUILD.mkdir(exist_ok=True)
    out = BUILD / f"{token.lower()}.jpg"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    subprocess.run(
        ["magick", str(src), "-auto-orient", "-resize", f"{max_px}x{max_px}>", "-strip",
         "-sampling-factor", "4:2:0", "-quality", str(QUALITY),
         "-define", "jpeg:dct-method=float", "-interlace", "JPEG", str(out)],
        check=True,
    )
    return out


def data_uri(path: pathlib.Path, mime: str = "image/jpeg") -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


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


def build(src: str, notes_file: str, fragment: str, standalone: str) -> None:
    html = (ROOT / src).read_text(encoding="utf8")
    html = html.replace("/*{{FONTS}}*/", (ASSETS / "fonts.css").read_text(encoding="utf8"), 1)

    for token, (rel, max_px) in IMAGES.items():
        marker = "{{" + token + "}}"
        if marker in html:
            html = html.replace(marker, data_uri(optimise(token, rel, max_px)))

    for token, (rel, mime) in FILES.items():
        marker = "{{" + token + "}}"
        if marker not in html:
            continue
        path = ROOT / rel
        if not path.exists():
            sys.exit(f"missing asset for {token}: {path}")
        html = html.replace(marker, data_uri(path, mime))

    notes = json.loads((ROOT / notes_file).read_text(encoding="utf8"))
    html = html.replace("{{NOTES}}", json.dumps(notes, ensure_ascii=False), 1)
    if "{{SPONSORS_SVG}}" in html:
        html = html.replace("{{SPONSORS_SVG}}", sponsor_svg(), 1)

    left = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if left:
        sys.exit(f"{src}: unreplaced tokens: " + ", ".join(sorted(set(left))))

    # fragment for the Artifact wrapper
    (ROOT / fragment).write_text(html, encoding="utf8")

    # standalone document for hosting and for opening straight off disk;
    # without a doctype the browser renders in quirks mode
    split = html.index("</style>") + len("</style>")  # charset, title and the stylesheet go in <head>
    doc = HEAD + html[:split] + "\n</head>\n<body>\n" + html[split:] + "\n</body>\n</html>\n"
    (ROOT / standalone).write_text(doc, encoding="utf8")

    for name in (fragment, standalone):
        size = (ROOT / name).stat().st_size / 1024 / 1024
        print(f"wrote {name}  ({size:.2f} MB)")


def main() -> int:
    if not shutil.which("magick"):
        sys.exit("ImageMagick (`magick`) is required to optimise the photos")
    for deck in DECKS:
        build(*deck)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
