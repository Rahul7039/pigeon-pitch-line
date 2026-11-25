#!/usr/bin/env python3
# Pigeon Pitch, One Line - make.fun one-line entry.
# A city pigeon pitches investors: drones are expensive overhead,
# pigeons already own the rooftops and run on crumbs - so even the
# startup's burn rate is crumbs. Prints exactly one line, nothing else.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "Drones need charging, permits and a pilot; we run on crumbs and already own every rooftop. Coo.ly: same-day crumb delivery, burn rate: crumbs."


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
