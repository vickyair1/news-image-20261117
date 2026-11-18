#!/usr/bin/env python3
"""news-image-20261117 entrypoint (Python 3.13, standard library only).

Writes the entry image (the entry.png beside this file — JPEG bytes under
the entry.png name, which the rules allow) to the grader's output dir as
/output/entry.png. Deterministic: every run writes identical bytes.

Local run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path


def entry_image_path() -> Path:
    """The entry image lives next to this file, whatever the cwd is."""
    return Path(__file__).resolve().parent / "entry.png"


def output_dir() -> Path:
    """Grader output dir, or MAKEFUN_OUTPUT_DIR when running locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    src = entry_image_path()
    if not src.is_file():
        print(f"entry image missing: {src}", file=sys.stderr)
        return 1
    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "entry.png"
    shutil.copyfile(src, dest)
    # copyfile is silent on a short write; verify the size so a truncated
    # output fails loudly instead of shipping a corrupt entry.
    if dest.stat().st_size != src.stat().st_size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
