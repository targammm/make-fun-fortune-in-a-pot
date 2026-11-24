#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant to /output/entry.txt.
The fortune is a single line of at most 120 characters, written for
the plant on the windowsill: warm, specific, and carrying its joke
in the last words.
"""

import os

FORTUNE = "By Friday, one brave root will find the drainage hole, and your human will call it ambition."

def main():
    # Gate the line before writing it: the sealed scorer only judges
    # UTF-8 text of 1-120 characters, not only whitespace, on one line.
    assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"
    assert FORTUNE.strip() == FORTUNE, "fortune must not start/end with whitespace"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
