"""food-picture-01 entry: copy the bundled food picture to the output path.

Deterministic, stdlib only, no network, no randomness, no timestamps:
the program copies the exact bytes of entry.png beside this file to
<MAKEFUN_OUTPUT_DIR or /output>/entry.png.
"""

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    # Verify the copy is byte-identical to the bundled image.
    if OUT.read_bytes() != SRC.read_bytes():
        raise ValueError("copied entry.png does not match the bundled image")


if __name__ == "__main__":
    main()
