"""news-image-20261117 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file (JPEG bytes under the
entry.png name, which the rules allow); the program copies it to
/output/entry.png. Deterministic: every run writes the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).with_name("entry.png")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
