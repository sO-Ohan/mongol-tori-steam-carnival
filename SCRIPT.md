# Mongol-Tori — National STEAM Carnival pitch

Speaker script for the deck. Target run time **8 min 50 s**, inside a 7–10 minute slot.
Press **N** in the deck to read these on your laptop; **T** starts the mission clock in the bottom rail.

## 01 · Title
`0:00 – 0:25  ·  25s`

> "Assalamu alaikum. We are BRACU Mongol-Tori, from BRAC University. We have been building Mars rovers for eleven years, and this May our rover finished seventh in the world."

  - Say the name in Bangla once — মঙ্গল তরী, Mars Chariot.
  - Then set up the talk: "I want to show you how we build, not just where we placed."
  - Don't read the slide. Let the photo hold the room.

## 02 · Who we are
`0:25 – 1:00  ·  35s`

> "We started in 2015. Everyone on the team is a student — six subsystems, from mechanical to astrobiology. Every year seniors graduate, so half our job is teaching the next batch before we leave."

  - That handover point lands with a student audience. Say it plainly.
  - Name Dr. Khalilur Rhaman and the Onnesha connection — one sentence, then move.

## 03 · Why we do it
`1:00 – 1:35  ·  35s`

> "We are two things at the same time. A research group, and a competition team."

  - **Research:** the real problem is a machine knowing where it is without being told. Same problem in rovers and drones, and useful here in Bangladesh, not only on Mars.
  - **Competition:** a fixed date, a written spec, and judges who don't care how hard it was. If it doesn't work that day, we score zero.
  - Finish on the last line — most of us joined because a senior showed us a rover once. It sets up the outreach slide later.

## 04 · The four missions
`1:35 – 2:10  ·  35s`

> "Four missions, thirty minutes each. The rule that shapes everything: the driver sits in a tent and cannot see the rover."

  - Science, delivery, servicing, autonomy — one line each, keep it moving.
  - 116 teams → 38 finalists → 7th. Say the funnel out loud.
  - Rover people in the room already know this. Read the room and speed up if they do.

## 05 · Results
`2:10 – 2:55  ·  45s`

> "This is every year we have competed — Utah in orange, the International Rover Challenge in India in blue."

  - Don't hide 2024 — 21st. "Nothing exploded. Everything was just a little worse than it needed to be."
  - Then the two stories at the bottom: **2023, the circuit burned** and the team rebuilt it in four hours in a remote camp. **2024, the chassis broke** mid-run and was fixed in six hours with what was in the pit box.
  - Land it: "None of these were clean years. The scores came anyway."

## 06 · Bangladesh at URC
`2:55 – 3:20  ·  25s`

> "Three of the world's top eleven rovers were built in Dhaka. UIU third, us seventh, MIST eleventh. Five Bangladeshi teams reached the finals — only the US sent more."

  - This slide is for the other teams in the room. If UIU or MIST people are here, look at them.
  - Last line slowly: we are all competing with Utah, not with each other.

## 07 · Meet Taurus
`3:20 – 3:55  ·  35s`

> "This is Taurus, this year's rover. One machine that has to drill rock, plug in a cable, climb a hill and drive itself home."

  - Use the drawing — point at the antenna mast, the arm axes, the rocker-bogie, the airless wheels.
  - Don't go deep. This is the map for the next four slides, not the tour.

## 08 · The radio link
`3:55 – 4:45  ·  50s`

> "First breakthrough: the radio link. Three bands at once, so losing one doesn't end the run."

  - **433 MHz SATEL** for driving commands — narrow channel, slow, but it gets through hills. Verified 1.2 km.
  - **5.8 GHz** for video and data. **2.4 GHz** as backup — we tested it by switching the main link off mid-run and kept driving.
  - **Say this clearly:** those distances are with hills in the way. In open line of sight it goes very much further. We quote the worst case because the competition is the worst case.
  - Slow down here — this is the technical heart of the talk.

## 09 · The antennas
`4:45 – 5:25  ·  40s`

> "Second breakthrough: we stopped using the antennas that came in the box."

  - The datasheet range was measured somewhere that isn't our field. So we contacted CompleTech in Finland and asked.
  - We simulated our own test ground, their engineers designed antennas for that case, then we measured the real range instead of trusting a number.
  - The point for this room: they had no reason to help a student team in Dhaka. They helped because the question was specific. Pause after that.

## 10 · Autonomy
`5:25 – 6:00  ·  35s`

> "Third: knowing where you are. Four sensors, each wrong in a different way."

  - GPS wanders. Wheels slip. The IMU drifts. Stereo cameras get lost on flat sand.
  - An SBG Systems inertial unit, GNSS, a stereo camera and ArUco markers go into one filter — one position, one map, one path.
  - All onboard on a Jetson. We test in simulation first: a bug in software costs an afternoon, a bug in the desert costs a mission.

## 11 · Our own boards
`6:00 – 6:35  ·  35s`

> "Fourth: the parts we couldn't buy, we made."

  - **Kacchim** — our controller board, sits between the computer and everything that moves. Motors, sensors, science payload, wireless emergency stop. One board across the rover means one spare to carry.
  - **Power board** — one plug-in card per voltage. A rail dies in the pit, you swap the card instead of rewiring the rover. Above 95% efficient.
  - Then MyActuator: where we do buy, we buy well, and they back the team.

## 12 · Drones and the Navy
`6:35 – 7:05  ·  30s`

> "We build drones as well. Ours flies ahead of the rover during a mission and looks at ground the rover cannot see yet — on the same radio network."

  - Same navigation problem, solved once, used twice.
  - The Bangladesh Navy came to the lab to see it. Students explained it to them across a table — which is how most things here start.

## 13 · Outreach
`7:05 – 7:45  ·  40s`

> "For eleven years we have been taking the rover into school grounds and putting the controller in a child's hands."

  - Slow down here. This is the part of the talk people remember.
  - Point at the girl with the controller. "That is a whole afternoon of our weekend, and it is the best thing we do."
  - Close it: a child who has driven a rover stops thinking engineering happens in other countries.

## 14 · The astronaut visit
`7:45 – 8:15  ·  30s`

> "An astronaut came to our lab. He didn't come to see a famous laboratory. He came to see a bunch of students who love solving engineering problems, standing next to a rover they built themselves."

  - Let the photo sit for a beat before you speak.
  - This is the emotional close — deliver it slowly, then go to partners.

## 15 · Partners
`8:15 – 8:35  ·  20s`

> "None of this happens on a student budget. Twenty-three companies and organisations back this team."

  - Don't read logos. Name the three that gave engineering time, not just money: CompleTech, SATEL, SBG Systems.
  - If a potential sponsor is in the room, look up here and say you are always open to one more.

## 16 · Close
`8:35 – 8:50  ·  15s`

> "Mongol Tori means Mars Chariot. Come and talk to us after this — ask what it cost, what broke, how to start your own team. We would rather Bangladesh had ten good rover teams than one. Thank you."

  - Stop. Take questions.
  - Likely questions: total cost · how to get sponsors · how you handle graduation turnover · why 433 MHz · how to start a team at their university.
