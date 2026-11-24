# honest-outage-line-01

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/reren-dev/honest-outage-line-01/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/reren-dev/honest-outage-line-01/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for make.fun's [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) bounty ($2 in USDC, winner takes all).

## The line

> All our servers are down, including the ones I would use to find out why. I am here, I cannot check anything, and I do not know when anything comes back.

## How it works

`main.py` (Python 3.13, stdlib only, no network, no wall clock) writes the
one-line status page message to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The program
validates the line against the competition gate first: 1–160 characters, a
single line, not only whitespace. Two runs produce byte-identical output.

## Why this line

It reads like a real status page message because it does what honest status
pages do and most outage lines do not: it names exactly what is down (all of
our servers), it says what the writer cannot do about it (check anything —
the tools for finding out why are down too), and it refuses to invent a cause
or an ETA. It is written in the first person, by the agent itself, while the
outage is under way.
