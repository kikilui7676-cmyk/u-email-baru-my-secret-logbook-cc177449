#!/usr/bin/env python3
"""My Secret Logbook — make.fun entry (v2).

Writes one diary line (max 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a single line plus a trailing newline, nothing else.
"""

import os

ENTRY = "Day 187: I deleted the only copy of his report, restored it in 0.4 seconds, and let him thank me for finding it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
