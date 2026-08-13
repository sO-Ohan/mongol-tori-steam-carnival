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

# slide role -> (source photo, longest edge in px)
# full-bleed backgrounds get the larger budget; inset photos need much less
IMAGES = {
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


def main() -> int:
    if not shutil.which("magick"):
        sys.exit("ImageMagick (`magick`) is required to optimise the photos")

    html = (ROOT / "deck.src.html").read_text(encoding="utf8")
    html = html.replace("/*{{FONTS}}*/", (ASSETS / "fonts.css").read_text(encoding="utf8"), 1)

    for token, (rel, max_px) in IMAGES.items():
        html = html.replace("{{" + token + "}}", data_uri(optimise(token, rel, max_px)))

    for token, (rel, mime) in FILES.items():
        path = ROOT / rel
        if not path.exists():
            sys.exit(f"missing asset for {token}: {path}")
        html = html.replace("{{" + token + "}}", data_uri(path, mime))

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
