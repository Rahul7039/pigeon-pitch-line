#!/usr/bin/env python3
# Pigeon Pitch, One Line - make.fun one-line entry.
# Prints exactly one line: the entry text, nothing else.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = 'Drones need charging, permits and a pilot; we run on crumbs and already own every rooftop in the city. Coo.ly: same-day crumb delivery, now raising crumbs.'


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
