# Mongol-Tori — National STEAM Carnival pitch

Speaker script for `deck.html`. Target run time **8 min 40 s**, leaving buffer inside a 7–10 minute slot.
Press **N** in the deck to read these on your laptop; **T** starts the mission clock in the telemetry rail.

## 01 · Title
`0:00 – 0:25  ·  25s`

> "Assalamu alaikum. We're BRACU Mongol-Tori. This May we finished seventh in the world at the University Rover Challenge, in the Utah desert — and I want to spend the next eight minutes on *how*, not on the trophy."

  - Say the team name in Bangla once — মঙ্গল তরী, Mars Chariot. It lands with this crowd.
  - Don't read the slide. Let the photo do the work.

## 02 · Who we are
`0:25 – 1:00  ·  35s`

> "We started in 2015. Before the rover, BRAC students built Onnesha, the country's first nanosatellite, and Chondrobot, a lunar excavator. Mongol-Tori is the third thing in that line — and it is still 100% student-run."

  - Emphasise the handover: seniors graduate every year, juniors inherit the lab. That's the hard part of a student team, not the engineering.
  - Name-check Dr. Khalilur Rhaman.

## 03 · The competition
`1:00 – 1:40  ·  40s`

> "Four missions, thirty minutes each. The key rule: the operator sits in a tent and cannot see the rover. Every design decision after this slide comes from that one constraint."

  - 116 → 38 → 7th. Say the funnel out loud; the numbers do the bragging so you don't have to.
  - If the audience has rover people, they know the missions — go fast here.

## 04 · The climb
`1:40 – 2:20  ·  40s`

> "This is our ranking since 2018. I'm showing you the whole line, including 2024, when we came 21st."

  - **Own the dip.** An engineering audience trusts the presenter who shows the bad year.
  - Point at 2024: "Nothing exploded. Everything was just slightly worse than it needed to be. That's what a bad year actually looks like."
  - Then: "8th, then 7th — same core people, two years of *not* restarting the design from scratch."

## 05 · Bangladesh at URC
`2:20 – 2:50  ·  30s`

> "Three of the world's top eleven rovers were built in Dhaka. UIU came third — the best any Asian team has ever done. MIST came eleventh. Five Bangladeshi teams reached the finals; no country except the US sent more."

  - This is the slide for the other rover teams in the room. Say the last line slowly and mean it: **we're all competing with Utah, not with each other.**
  - If UIU or MIST people are present, look at them.

## 06 · Meet Taurus
`2:50 – 3:20  ·  30s`

> "This is Taurus. One chassis that has to drill rock, plug a cable into a socket, climb a hill, and then find its own way back with nobody driving."

  - Fast slide — it's a table of contents for the next five.
  - Flag the last line: three radio bands live at once. That's the thread you'll pull on shortly.

## 07 · Structure & mobility
`3:20 – 3:50  ·  30s`

> "Four-wheel rocker-bogie, steel skeleton, aluminium electronics bay, TPU grips we print ourselves. All of it FEA'd at peak load before anything was cut."

  - The tapered roller bearing detail is for the mechanical engineers: radial *and* axial load when turning on a slope.
  - End on the red number: **we failed the rain test at five minutes.** Say it plainly. That single admission buys you the room's trust for the rest of the talk.

## 08 · The arm
`3:50 – 4:20  ·  30s`

> "Seven degrees of freedom, and one cheat: the whole arm rides on a linear rail. Reach goes up, inertia doesn't."

  - Worm gear on the base — can't be back-driven, holds position with the power off. Engineers nod at this one.
  - Close with the framing: "Servicing tasks are a millimetre problem solved from a kilometre away." That hands you the comms slide.

## 09 · The link (comms)
`4:20 – 5:10  ·  50s`

> "Here's the part I actually want to talk about. Three bands, because one band is a single point of failure."

  - **433 MHz SATEL SATELLINE-EASy** — command and telemetry, 25 kHz narrowband, verified past 1.2 km. Narrow channel, low data rate, gets through terrain.
  - **5.8 GHz Ubiquiti Rocket AC**, 2×2 MIMO — primary data and vision, 40 MHz channel, over 900 m non-line-of-sight at −76 dBm.
  - **2.4 GHz Bullet AC** — standby failover on the same mast.
  - Punchline: "We tested the failover by switching off the primary link mid-run. The rover kept driving."
  - Slow down here. This is your most technical slide and the reason you were invited.

## 10 · The antennas / CompleTech
`5:10 – 5:50  ·  40s`

> "A radio's datasheet range was measured somewhere that isn't Bangladesh. So we sat down with the engineers at CompleTech — the Finnish antenna house behind ComAnt — and did it properly."

  - Walk the four steps: simulate our own ground → design antennas to those simulations → 2×2 MIMO omni on the rover, sector at base, Miniflex for 433 → measure it in the field.
  - SATEL gave the radios. SBG Systems gave the inertial unit. CompleTech tuned the antennas.
  - **The takeaway for this room:** every one of those relationships started with a student sending a technical email. Say "Ask." and pause.

## 11 · Autonomy
`5:50 – 6:35  ·  45s`

> "Four sensors that lie in different directions. GNSS drifts, wheels slip, the IMU integrates its own error, stereo depth hates featureless sand. So none of them gets to be right on its own."

  - Left to right: SBG inertial + GNSS (weighted by HDOP) + ZED 2i stereo + ArUco markers → EKF → AMCL seeded by a 360° sweep, then NDT scan-matching → Nav2 with a DWA local planner.
  - The one number: every validated ArUco detection resets accumulated dead-reckoning drift to centimetre level.
  - All onboard on a Jetson Orin Nano, in ROS 2, validated in a Unity sim before it touches hardware.

## 12 · Power & safety
`6:35 – 7:05  ·  30s`

> "Our power distribution board is a backplane with one hot-swappable card per rail. GaN FETs, 95% efficiency, eFuse on every rail, live current telemetry to the base station."

  - Hot-swap matters in the pits: "a rail dies, you pull the card and push in a spare, at night, with a head torch."
  - Two kill switches, deliberately identical circuits, so one spare part fixes either.
  - Land the closing line: buying a PDB is faster; building one is why we can debug it at 2 a.m.

## 13 · Science payload
`7:05 – 7:30  ·  25s`

> "The science mission is looking for signs of life — with an auger, a load cell and a pH probe."

  - Acquire → contain → measure → assay. Four beats, one sentence each. Don't linger.
  - Mention Kacchim by name: our own control board runs the actuators for both the science payload and the rest of the rover. One board to learn, one board to fix.

## 14 · Debrief
`7:30 – 8:05  ·  35s`

> "If you're starting a team today, here's what eight years cost us to learn."

  - Read the four headlines only — the sub-text is for the photo people take of the slide.
  - Number three is the one to sell in this room: **industry will pick up the phone.**
  - Number four saves teams their season: half the teams that never reach Utah are eliminated on paper.

## 15 · Partners
`8:05 – 8:25  ·  20s`

> "None of this happens on a student budget. Twenty-three companies put something real behind this rover."

  - Don't read the logos. Name three that gave engineering, not just money: CompleTech, SATEL, SBG Systems.
  - If a potential sponsor is in the room, this is the moment to look up and say you're always open to another one.

## 16 · Close
`8:25 – 8:40  ·  15s`

> "Mongol Tori means Mars Chariot. Come find us after this — ask us anything: link budgets, gear ratios, what we broke, what it cost. We'd rather Bangladesh had ten good rover teams than one. Thank you."

  - Stop talking. Take questions.
  - Likely questions: total cost / how do you get sponsors / how do you handle graduation turnover / why 433 MHz over LoRa / why not RTK GNSS.
