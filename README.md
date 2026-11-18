# Sum up 17 November's world news in one image

Entry for the make.fun bounty
[`news-image-20261117`](https://make.fun/bounty/news-image-20261117):
a newspaper front page that sums up the world news of
**Tuesday 17 November 2026** in a single 1024×1024 image.

## What it shows

| Panel | Story (all reported on 17 Nov 2026) |
| --- | --- |
| Hero | **Kerch Bridge falls** — a Ukrainian strike drops the road arch into the Kerch Strait, cutting Russia's road link to Crimea |
| Gulf | **US strikes Qeshm; tankers burn in Hormuz** — US jets hit an IRGC missile site on Qeshm Island; mines hit tankers in the strait; Brent nears $94 |
| Asia | **Trump in Asia, heads for Xi–Putin talks** — Quad summit in Manila; three-way meeting due in Shenzhen |
| Tech | **Nvidia: $115.8bn, up 103%** — first earnings report since Jensen Huang quit |
| France | **146,000 march in France** — unions strike over living costs |
| USA | **US no longer measles-free** — first loss of measles-elimination status in 26 years |
| Ticker | Russian An-12 crash kills all 19 aboard · Mongolia's president resigns · Biden's memoir published |

Facts were checked against same-day reporting (BBC, Bloomberg via
military.com, Euronews/AP, Le Monde, CNN, Foreign Exchanges) on 18 Nov 2026.
The Depardieu appeal story, widely listed in 17 Nov digests, was excluded:
it happened on Monday 16 November.

## How it was built

- `compose.py` (Python + Pillow) lays out the front page: masthead with the
  date, six photo panels with crisp vector-drawn headlines, and a ticker.
- The six panel pictures in `assets/` are AI-generated illustrations made
  for this entry (no text inside them, so nothing can garble); all words
  are drawn by `compose.py`, which is why the text is sharp at any size.
- `entry.png` holds JPEG bytes under the `entry.png` name, which the
  bounty rules allow (PNG or JPEG, told apart by magic bytes). It is
  1024×1024 and 370,649 bytes — well under the 1 MiB cap.
- `main.py` copies `entry.png` to `/output/entry.png`. It is deterministic:
  every run writes the same bytes.

## Reproduce

```sh
python3 compose.py          # rebuilds entry.png from assets/
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
