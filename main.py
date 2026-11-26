#!/usr/bin/env python3
# Pigeon Pitch, One Line - make.fun entry.
# A city pigeon pitches investors for its startup, Coo.ly: drones are
# expensive overhead (charging, permits, a pilot), while pigeons run on
# crumbs and already own every rooftop - so even the burn rate is crumbs.
# Prints exactly one line and writes the same line to /output/entry.txt.
# Deterministic, standard library only, no network, no randomness.

import os

LINE = "Drones need charging, permits and a pilot; we run on crumbs and already own every rooftop. Coo.ly: same-day crumb delivery, burn rate: crumbs."

# Gate: the kit's sealed scorer accepts 1-200 characters. Fail loudly here
# rather than shipping a line the gate would refuse.
MAX_CHARS = 200
assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-200 char gate"


def main() -> None:
    # The graded artifact: the kit's harness reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
