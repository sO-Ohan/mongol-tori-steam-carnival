# BRACU Mongol-Tori — National STEAM Carnival deck

**Live: https://so-ohan.github.io/mongol-tori-steam-carnival/**

A self-contained HTML slide deck. Everything (fonts, photos, sponsor wall) is inlined,
so it works offline from a USB stick with no network and no dependencies.

## Presenting

Open the live link — or `index.html` from disk — in any browser, and press **F**.

Take the offline copy to the venue regardless. The page is ~2.7 MB over the wire, which
is a few seconds on a bad conference connection and nothing at all once it is cached, but
a laptop with the file on it cannot be let down by the venue wifi.

| Key | Does |
| --- | --- |
| `→` `space` `PgDn` | next slide |
| `←` `PgUp` | previous slide |
| `N` | show / hide speaker notes for the current slide |
| `T` | start / pause the mission clock (MET) in the bottom rail |
| `R` | reset the clock |
| `F` | full screen |
| `Home` / `End` | first / last slide |

The bottom rail also has clickable progress ticks, and `deck.html#9` jumps straight to
slide 9 — handy for rehearsing one section.

The stage is a fixed 1280×720 canvas scaled to the window, so the layout is identical on
your laptop and on the venue projector. Nothing reflows.

## Files

| File | What it is |
| --- | --- |
| `index.html` | **The deliverable.** Complete document — what GitHub Pages serves. Built; do not edit by hand. |
| `deck.html` | Same deck as a body-only fragment, for publishing as a Claude Artifact. Also built. |
| `deck.src.html` | Source template with `{{TOKEN}}` placeholders. **Edit this one.** |
| `notes.json` | Speaker notes + per-slide timings. Feeds both the in-deck panel and `SCRIPT.md`. |
| `SCRIPT.md` | Printable speaker script, 8 min 40 s target. |
| `build.py` | Inlines fonts, photos and the sponsor SVG into both outputs. |
| `assets/` | Font faces, the sponsor-wall SVG, the logo mark, the annotated rover drawing, the advisor photo, and four partner logos cut out of the sponsor sheet. |
| `images/` | URC 2026 photos from Utah. |
| `astonoute/` | Lab and outreach photos — the astronaut visit, the Navy visit, SATEL radios, the CompleTech call, school visits. |
| `build/` | Optimised JPEGs, cached between builds. Not committed. |

## Running order

1. Title · 2. Who we are · 3. Why we do it (research + competition) · 4. The four missions ·
5. Results, URC and IRC · 6. Bangladesh at URC 2026 · 7. Meet Taurus · 8. The radio link ·
9. The antennas, with CompleTech · 10. Autonomy · 11. Our own boards · 12. Drones and the Navy ·
13. Outreach · 14. The astronaut visit · 15. Partners · 16. Close

## Rebuilding and redeploying

```
python3 build.py
git commit -am "update deck" && git push
```

GitHub Pages redeploys on push, usually within a minute. Needs ImageMagick for the photo
optimisation step (1280 px, q66), which is cached in `build/` and skipped when nothing
changed.

To swap a photo, drop the new file in `images/` and point the matching entry in
`build.py`'s `IMAGES` map at it. The sponsor wall is `assets/sponsors.svg`; `build.py`
crops its export margin with a `viewBox` override, so update that crop if you re-export
the SVG at a different size.

## Sources for every number on the slides

- URC 2026 result (7th; 116 teams / 18 countries → 38 finalists / 11 countries; UIU 3rd,
  MIST 11th, AAUB 34th) — Mars Society URC 2026 scores and Bangladeshi press.
- Rank history (13th/2018, 4th/2021, 16th/2023, 21st/2024, 8th/2025) — team site and press.
  2020 is deliberately omitted; the record for that year is inconsistent.
- All rover specifications, test results, radio parameters and the CompleTech
  collaboration — the team's own preliminary design report.
