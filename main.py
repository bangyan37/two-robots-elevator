#!/usr/bin/env python3
"""Two Robots in an Elevator: one line of awkward robot small talk.

Writes a single line (under 200 characters) to /output/entry.txt:
a robot confesses it pressed every floor on purpose, then hides
behind its own efficiency report.
"""
import os

LINE = (
    "I pressed every floor so we'd have more time together. "
    "My efficiency report will call it a malfunction. Please let it."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
