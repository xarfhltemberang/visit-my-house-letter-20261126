#!/usr/bin/env python3
"""Entry point: copy the pre-rendered invitation image to the output dir.

Stdlib only — the grader runs Python 3.13 slim with no Pillow, so the image
is rendered ahead of time by draw.py and shipped as entry.png beside this
file. This program just places a byte-identical copy at /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when that is set).
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print(f"entry.png not found beside main.py ({SRC})", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
