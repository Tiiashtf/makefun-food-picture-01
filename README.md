# Steaming Tonkotsu Ramen — food-picture-01

A make.fun `food-picture-01` entry (program/v1). The program is a
deterministic, stdlib-only Python script that copies the bundled food
picture to the grader's output path.

## The picture

An original, AI-generated professional food photograph: a steaming bowl
of tonkotsu ramen on dark slate — glossy noodles lifted in a swirl by
wooden chopsticks, a halved soft egg with a jammy orange yolk, chashu
pork, scallions, sesame and nori in rich creamy broth, warm side light
against a deep charcoal background. No text, no watermark, no people.

The shipped file is `entry.png`: 1024×1024, 236,013 bytes. It is JPEG
data (the rules judge the format by its first bytes and the name stays
`entry.png` either way); the 1024×1024 PNG encoding was 1,327,807 bytes,
over the 1 MiB limit, so the same pixels were stored as JPEG quality 92
with no visible artefacts.

## How it works

`main.py` (Python 3.13, stdlib only) copies `entry.png` — the file
beside it in this repository — byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). No
network, no randomness, no timestamps; two runs write identical bytes.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png is byte-identical to entry.png
```

## Files

- `main.py` — the entrypoint
- `entry.png` — the picture (JPEG bytes, 1024×1024, < 1 MiB)
- `LICENSE` — MIT
- `.makefun/owner.json` — the account wallet claiming this repository
