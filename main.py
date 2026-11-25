"""Laugh Track: The Crypto Trading Joke Contest.

Writes one crypto-trading joke line to /output/entry.txt.
The line: a trader buys the dip, and the dip keeps on falling.

Revision: the first version wrote the line blindly. This version checks
the line against the bounty gate before writing it, and then reads the
file back to prove what landed on disk is byte-for-byte the line above.
"""

import os

ENTRY = "I bought the dip. Then the dip bought a shovel and kept digging."
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-200 chars, not only white space, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back check: what landed on disk must be byte-identical.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("entry.txt does not match the entry")


if __name__ == "__main__":
    main()
