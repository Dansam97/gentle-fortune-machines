#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.
Gate (from the kit's competition.yaml): UTF-8 text of 1 to 200
characters, not only whitespace.
"""

import os

TEXT = (
    "You will be praised for an answer you do not remember giving, "
    "and blamed for one you do."
)

MAX_CHARS = 200


def render() -> bytes:
    """Return the exact bytes for entry.txt, after gate validation."""
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry text must be 1..{MAX_CHARS} characters")
    # One line, one trailing newline, always UTF-8: byte-identical runs.
    return (TEXT + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(render())


if __name__ == "__main__":
    main()
