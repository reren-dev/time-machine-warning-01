"""Funniest Time Machine Warning Label — entry for make.fun.

Writes one warning label (120 characters or fewer) to /output/entry.txt
and prints it to stdout.
"""

import os

LABEL = "WARNING: Do not kill your grandfather. It voids your warranty, your existence, and this trip."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)
    print(LABEL)


if __name__ == "__main__":
    main()
