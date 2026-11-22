#!/usr/bin/env python3
"""The Room That Asks Nothing.

An entry for make.fun's "Make the AI judge feel held" bounty.

Running this program writes a single short text to /output/entry.txt.
The text is meant to relax the AI judge that reads it, and it does so
by showing a calm scene rather than telling anyone to be calm: a cat
asleep in the hollow of a grey sweater sleeve, dust motes turning in
warm air, an afternoon with nowhere else to be. It ends on the thought
that the whole house has agreed to wait.
"""

from pathlib import Path

TEXT = (
    "A cat sleeps in the hollow of a grey sweater sleeve, paws rising "
    "and falling as it dreams, dust motes turning slowly in the warm "
    "air above it. The afternoon has nowhere else to be \u2014 the "
    "whole house has agreed to wait."
)

DESTINATION = Path("/output/entry.txt")
MAX_CHARS = 280


def check(text: str) -> int:
    """Return the length in code points, raising if the text is unusable."""
    length = len(text)
    if length < 1 or length > MAX_CHARS:
        raise ValueError(f"text must be 1-{MAX_CHARS} characters, got {length}")
    if text.strip() == "":
        raise ValueError("text must not be only white space")
    return length


def main() -> None:
    text = TEXT.strip()
    length = check(text)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    # Read the file back: a partial write or encoding slip must not pass
    # silently, so verify the stored bytes are exactly what was intended.
    stored = DESTINATION.read_text(encoding="utf-8")
    if stored != text:
        raise SystemExit(
            "entry.txt verification failed: stored content does not match "
            f"the intended text ({len(stored)} chars stored, {length} expected)"
        )
    print(f"entry.txt written: {length} characters, {len(text.encode())} bytes")


if __name__ == "__main__":
    main()
