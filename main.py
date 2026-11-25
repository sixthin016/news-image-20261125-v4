#!/usr/bin/env python3
"""Sum up 25 November's world news in one image.

A make.fun program/v1 entry for the competition news-image-20261125.

The entry image lives next to this program at assets/entry.png: a
newspaper front page for Wednesday 25 November 2026, drawn at build
time by tools/generate.py from the day's reported news. It carries
35 stories across 10 regions and 14 fields -- three leads with
flat-vector illustrations, eight more stories built around the day's
big numbers, a world map with eleven numbered pins, a stories-by-region
table, 24 more stories, and a date check. v4 adds the three Africa
stories the v3 page was missing (Kinshasa, Abuja, Pretoria) and sets
the 24-more list in larger type so it stays readable at small sizes.

This program only copies that PNG to the output path, which the
competition rules explicitly allow: "the simplest entry is a
repository holding the image and a one-line program that copies it
there".

No network, no randomness, no wall-clock time, no third-party
packages -- only the Python standard library -- so the two grading
runs produce byte-identical output.

Run:  python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")

OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
OUTPUT_DEFAULT = "/output"
OUTPUT_NAME = "entry.png"


def main():
    """Copy the pre-rendered front page to the grading output dir.

    The destination comes from $MAKEFUN_OUTPUT_DIR when the harness
    sets it, and falls back to /output otherwise. shutil.copyfile
    copies bytes verbatim, so the output is identical on every run.
    """
    out_dir = os.environ.get(OUTPUT_ENV, OUTPUT_DEFAULT)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, OUTPUT_NAME))


if __name__ == "__main__":
    main()
