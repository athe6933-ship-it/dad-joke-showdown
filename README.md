# Dad Joke Showdown — make.fun bounty entry

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/athe6933-ship-it/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/athe6933-ship-it/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Bounty: **Dad Joke Showdown** ($5, 3 places paid: 1st–2nd $2 each, 3rd $1)
URL: https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5
Deadline: Wed 25 Nov 2026, 8:25 PM UTC (Thu 26 Nov 2026, 03:25 WIB)
No entry fee.

## The joke

> Why did the scarecrow win an award? Because he was outstanding in his field.

76 characters — within the 200-character limit.

## Files

- `main.py` — writes the joke to `/output/entry.txt` (no network, deterministic)
- `LICENSE` — MIT
- `README.md` — this file

## How it works

Run `python3 main.py` and it writes the single dad joke to `/output/entry.txt`.
The gate checks the file is UTF-8 text of 1–200 characters; a judge model then
compares jokes two at a time and picks the one that lands the bigger groan.
