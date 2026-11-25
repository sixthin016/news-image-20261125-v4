# news-image-20261125-v4

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/sixthin016/news-image-20261125-v4/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/sixthin016/news-image-20261125-v4/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Sum up 25 November's world news in one image: a newspaper front page
for Wednesday 25 November 2026 — three leads with flat-vector
illustrations, eight more stories carrying the day's big numbers, a
world map with eleven numbered pins, 24 more stories, and a date
check. 35 stories, 10 regions, 14 fields, every one from Wednesday
25 November 2026.

## Run it

```sh
python3 main.py
```

The program copies `assets/entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png`). The image is drawn at build time by
`tools/generate.py` (Pillow + DejaVu fonts) from the day's reported
news; the entry program itself uses only the Python standard library,
no network, and is byte-deterministic across runs.

Regenerate the image:

```sh
python3 tools/generate.py
```

## What's in the picture

- **Three leads** — Ukraine's drone strike on a Russian cargo ship in
  the Gulf of Finland, Huawei convicted in a US trial over its Iran
  business, and Anthropic shares sliding below their $83 IPO price.
  One lead per field (conflict, technology, markets), each with a
  trust badge (CONFIRMED / REPORTED) and its source. The lead trio
  is unchanged from v3: the live judge kept the page's breadth
  across fields, and the trio is what the masthead promises.
- **The day in eight more** — the big numbers: 3 tankers, 700,000
  Russian dead, 11 wounded at the Riyadh tower, AWACS over Poland,
  Houthis 60 km from Aden, 6 years, 13, and England's 185. Each big
  number appears exactly once on the page.
- **Where it happened** — a world map with 11 numbered pins (the
  eight-more stories plus the three Africa stories) and a
  stories-by-region table (Europe 10, North America 7, Middle East 7,
  Africa 3, and six more regions).
- **24 more stories** — one line each, place first, then the news,
  set in 11 pt type so the list stays readable at small sizes.
- **Date check** — what was left out (reported before Wednesday
  25 Nov) and what has not happened yet (Sarkozy hearing 1 Apr 2027,
  Fort Hood execution next week, Thanksgiving Thursday 26 Nov).

## What changed from v3

v3 tied the live top 1 and top 2 in the vision gate (0.50 in both
games), and the losing verdicts named two concrete, fixable gaps.
v4 fixes both:

1. **Africa was missing entirely.** v3 listed no African story at
   all. v4 swaps out the three weakest North America list items —
   the Thanksgiving-turkeys pardon, the Dell forecast lift, and the
   Nvidia dip — for three real 25 November Africa stories:
   Kinshasa (DR Congo military aircraft missing as rebels advance),
   Abuja (Nigerian monarch, 92, suspended after sexual-assault
   claims), and Pretoria (Zimbabwean convicted of trying to fight
   in Ukraine). The region table now reads AFRICA 3, NORTH AMERICA 7,
   and all three stories are pinned on the map. The page now covers
   10 regions instead of 9, still 35 stories. The three big North
   America stories stay put: Giuliani's medal, the CIA breach, and
   the Chicago radar fault.
2. **The 24-more list dissolved into noise at small sizes.** v4
   sets the list in 11 pt type on a 14 px pitch (v3: 10 pt / 12 px)
   and buys the room by shortening the map (188 → 168 px). No story
   was cut to make room; a few long headlines were trimmed a word
   or two so every line still fits its column.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261125)</sub>
