#!/usr/bin/env python3

import sys


data = [ln.strip() for ln in iter(sys.stdin.readline, "")]

beams = [0] * len(data[0])
beams[data[0].index("S")] = 1

one = 0
for ln in data[1:]:
    for i, c in enumerate(ln):
        if c == "^" and beams[i]:
            one += 1
            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0

print(f"ONE: {one}")
print(f"TWO: {sum(beams)}")
