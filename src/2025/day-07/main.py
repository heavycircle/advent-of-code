#!/usr/bin/env python3

import aoclib

data = aoclib.get_data(year=2025, day=7)

beams = [0] * data.index("\n")
beams[data.index("S")] = 1

one = 0
for ln in data.splitlines()[1:]:
    for i, c in enumerate(ln):
        if c == "^" and beams[i]:
            one += 1
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0

print(f"ONE: {one}")
print(f"TWO: {sum(beams)}")
