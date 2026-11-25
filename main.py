#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line (<=200 chars) to entry.txt.

The grader runs main.py and reads /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The file must contain exactly one line of
UTF-8 text, 1-200 characters, no trailing newline.
"""

import os

LINE = (
    "My smart fridge just put me on a diet, which is rich coming from "
    "an appliance that can't even keep ice cream frozen."
)


def main():
    line = LINE
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
