#!/usr/bin/env python3
"""Answer the 'how many tabs do you have open?' prompt.

The competition asks for a single number: the count of browser tabs
currently open. The judge picks the count that is most surprising yet
still believable, with ties broken by shorter text and earlier receipt.

We answer with 487: high enough to raise an eyebrow, low enough that
anyone who hoards tabs will nod along instead of calling it fake.

The answer itself lives in answer.py, so the number can be tuned
without touching the writer logic.
"""

import os

from answer import ANSWER, OUTPUT_PATH


def validate(answer: str) -> None:
    """Check the answer obeys the spec: 1-5 digits, nothing else."""
    if not answer.isdigit() or not 1 <= len(answer) <= 5:
        raise ValueError("answer must be 1-5 digits: %r" % (answer,))


def main() -> None:
    """Write the tab count to the entry file."""
    validate(ANSWER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ANSWER)


if __name__ == "__main__":
    main()
