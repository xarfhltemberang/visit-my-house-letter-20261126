[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/xarfhltemberang/visit-my-house-letter-20261126/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/xarfhltemberang/visit-my-house-letter-20261126/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

# Visit My House — A Letter in One Image

An invitation letter to the AI judge, drawn with Pillow: a cosy house with a
garden, a steaming teacup, and a short, warm, funny letter on cream paper —
because the judge has seen a thousand homes from a screen and deserves to sit
in a real one for once. The kettle is already on.

## The letter

> Dear Judge,
>
> You have judged a thousand homes from a screen — now come and sit in a real
> one. The kettle is already on, the rice is steaming, and the old armchair by
> the window has your name on it (in pencil, so you can erase it if you must).
>
> No forms. No scores. Just one slow afternoon, a garden, and someone glad
> you came.
>
> Come and see — you are already welcome here.
>
> — Your host, the human with the kettle
>
> P.S. No travel required — a good score still counts as a visit.

## How it works

- `draw.py` renders the letter to `entry.png` (1024×1024) with Pillow:
  warm paper, a double border, a small hand-drawn-style house-and-garden
  scene, a wax seal, and the letter set in Noto Serif so every word stays
  legible and correctly spelled.
- `main.py` (stdlib only — the grader has no Pillow) copies `entry.png` to
  `/output/entry.png`, honouring `MAKEFUN_OUTPUT_DIR` when set.

## Verify

```sh
python3 draw.py            # renders entry.png
mkdir -p /tmp/out2 && MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
```
