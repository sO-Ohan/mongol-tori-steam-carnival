# BRACU Mongol-Tori — presentation decks

**Live: https://so-ohan.github.io/mongol-tori-steam-carnival/**

Two self-contained HTML slide decks, same engine, different rooms. Everything (fonts,
photos, sponsor wall) is inlined, so they work offline from a USB stick with no network
and no dependencies.

| Deck | For | Runs | Open |
| --- | --- | --- | --- |
| **Carnival** | The National STEAM Carnival — judges, sponsors, other rover teams | 8 min 50 s, 16 slides | `index.html` (live link above) |
| **School** | Class 5–10 students, school visits and outreach | 19 min + questions, 17 slides | `school.html`, or `/school.html` on the live site |

The school deck is the same story told for a school hall: photographs first, one idea per
slide, type a size up, and the numbers that make a thirteen-year-old sit forward. Slide 8
is interactive — the pointer drags a camera beam across a dark desert, which is all the
driver of a rover is allowed to see.

## Presenting

Open the live link — or `index.html` / `school.html` from disk — in any browser, and press **F**.

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
| `index.html` | **The carnival deliverable.** Complete document — what GitHub Pages serves. Built; do not edit by hand. |
| `deck.html` | Same deck as a body-only fragment, for publishing as a Claude Artifact. Also built. |
| `deck.src.html` | Carnival source template with `{{TOKEN}}` placeholders. **Edit this one.** |
| `notes.json` | Carnival speaker notes + per-slide timings. Feeds the in-deck panel and `SCRIPT.md`. |
| `SCRIPT.md` | Printable carnival script, 8 min 50 s target. |
| `school.html` | **The school deliverable.** Complete document. Built. |
| `school.deck.html` | School deck as a body-only fragment, for the Artifact wrapper. Built. |
| `school.src.html` | School source template. **Edit this one.** |
| `school-notes.json` | School speaker notes, including the ask-the-room prompts. |
| `SCHOOL-SCRIPT.md` | Printable school script, 19 min, with a pre-visit checklist. |
| `build.py` | Inlines fonts, photos and the sponsor SVG into every output. A photo is only inlined into a deck that actually uses its token. |
| `assets/` | Font faces, the sponsor-wall SVG, the logo mark, the annotated rover drawing, the advisor photo, and four partner logos cut out of the sponsor sheet. |
| `images/` | URC 2026 photos from Utah. |
| `astonoute/` | Lab and outreach photos — the astronaut visit, the Navy visit, SATEL radios, the CompleTech call, school visits. |
| `build/` | Optimised JPEGs, cached between builds. Not committed. |

## Running order — carnival deck

1. Title · 2. Who we are · 3. Why we do it (research + competition) · 4. The four missions ·
5. Results, URC and IRC · 6. Bangladesh at URC 2026 · 7. Meet Taurus · 8. The radio link ·
9. The antennas, with CompleTech · 10. Autonomy · 11. Our own boards · 12. Drones and the Navy ·
13. Outreach · 14. The astronaut visit · 15. Partners · 16. Close

## Running order — school deck

1. Title · 2. **The astronaut** (the hook — open on it) · 3. Nobody handed us a robot ·
4. This is not Mars · 5. Why robots go first (the four Mars numbers) · 6. Meet Taurus ·
7. The four jobs · 8. The driver cannot see the rover (interactive) · 9. Radio ·
10. Driving itself · 11. Make it, or ask · 12. It breaks · 13. The scoreboard ·
14. Drones · 15. Your turn · 16. How to start this week · 17. Close

Slide 6 is the planned break: if the rover came with you, stop there, go outside, come back.
Slide 16 is the one that has to be specific — name a club, a teacher or a contest they can
actually turn up to.

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
- Mars figures on school slide 5 — average surface temperature ≈ −60 °C (NASA; the range
  runs from about +20 °C to −153 °C); atmosphere ~95% carbon dioxide with no breathable
  oxygen; one-way radio delay between Earth and Mars ranges from about 3 to 22 minutes
  with the planets' distance, which is why the slide says "up to twenty minutes" rather
  than a single number.
- The +35 °C on the same slide is **Utah, not Mars** — Hanksville averages highs of ~23 °C
  rising to ~29 °C through May and sits around 29–35 °C in June, which is when URC runs.
  The slide names both on purpose: the −60 °C belongs to the planet, the +35 °C to the
  desert the team actually stands in, and the two used to be easy to confuse.
