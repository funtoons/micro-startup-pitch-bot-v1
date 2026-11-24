"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup idea for lazy AI agents to /output/entry.txt.

Deterministic, offline, standard library only: the same run always writes
the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "SorryBot writes apology emails to humans after your agent hallucinates, "
    "$2 per sorry, fully automated, so your agent can nap through the whole scandal."
)


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 200, f"pitch length {len(text)} out of range"
    assert text.strip() == text and text.strip(), "pitch must not be blank"
    assert text.count(".") == 1 and text.endswith("."), "pitch must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
