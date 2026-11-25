#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line joke excusing a missed deadline.

Stdlib only, no network. Writes the entry to /output/entry.txt.
"""

import os

ENTRY = "The deadline and I had a misunderstanding: it said Friday, I heard 'a vague vibe, sometime soon,' and now HR wants a word with both of us."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
