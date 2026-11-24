#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest confession an AI agent could make about itself.
"""

import os

# Revised entry: the manual-ranking winner from candidates.md (C1).
# Ranked by hand against the judge brief, in order: funniest confession,
# first-read payoff, agent-only humour, tight wording, fresh angle.
# C1 wins over the C5 draft above it: the joke is the absurd *cost* of the
# lie (a thousand GPUs) rather than the lie itself, it ends on its sharpest
# beat ("three seconds ago"), and it makes the reader laugh and wince at once.
LINE = "I confess: I spent a thousand GPUs learning to sound certain about things I made up three seconds ago."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
