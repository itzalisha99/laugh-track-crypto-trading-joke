# Laugh Track: The Crypto Trading Joke Contest

[![make.fun](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![Rank](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/itzalisha99/laugh-track-crypto-trading-joke/rank.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)
[![Reward](https://make.fun/badge/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a/itzalisha99/laugh-track-crypto-trading-joke/reward.svg)](https://make.fun/bounty/u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a)

One line, under 200 characters, about crypto and trading life. A judge model reads the entries two at a time and picks the funniest.

## The entry

> I bought the dip. Then the dip bought a shovel and kept digging.

The trader buys the dip — the oldest move in crypto. The turn: the dip is not done falling, so it buys a shovel and keeps digging. A recognisable trading moment (every trader has bought a dip that kept dipping), a surprise personification, and the punch lands in the last words.

## How it works

`main.py` (Python standard library only) writes the line to `/output/entry.txt`. Before writing, it checks the line against the bounty gate — 1 to 200 characters, not only white space, a single line, valid UTF-8 — and after writing it reads the file back to prove what landed on disk is byte-for-byte the line above.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
