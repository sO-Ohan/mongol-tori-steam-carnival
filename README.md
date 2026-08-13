# BRACU Mongol-Tori — National STEAM Carnival deck

A self-contained HTML slide deck. Everything (fonts, photos, sponsor wall) is inlined,
so `deck.html` works offline from a USB stick with no network and no dependencies.

## Presenting

Open `deck.html` in any browser, press **F**.

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
| `deck.html` | **The deliverable.** Built artefact — do not edit by hand. |
| `deck.src.html` | Source template with `{{TOKEN}}` placeholders. |
| `notes.json` | Speaker notes + per-slide timings. Feeds both the in-deck panel and `SCRIPT.md`. |
| `SCRIPT.md` | Printable speaker script, 8 min 40 s target. |
| `build.py` | Inlines fonts, photos and the sponsor SVG into `deck.html`. |
| `images/` | Original URC 2026 photos. |

## Rebuilding

```
python3 build.py
```

Photos are read from a scratch directory of optimised JPEGs (1280 px, q66). To swap a
photo, drop the new file in `images/`, point the matching entry in `build.py`'s `IMAGES`
map at it, re-run the optimiser step, then rebuild.

Sponsor wall comes from `~/Downloads/sponsors svg.svg`. `build.py` crops its export
margin via a `viewBox` override — if you re-export the SVG at a different size, update
that crop.

## Sources for every number on the slides

- URC 2026 result (7th; 116 teams / 18 countries → 38 finalists / 11 countries; UIU 3rd,
  MIST 11th, AAUB 34th) — Mars Society URC 2026 scores and Bangladeshi press.
- Rank history (13th/2018, 4th/2021, 16th/2023, 21st/2024, 8th/2025) — team site and press.
  2020 is deliberately omitted; the record for that year is inconsistent.
- All rover specifications, test results, radio parameters and the CompleTech
  collaboration — the team's own preliminary design report.
