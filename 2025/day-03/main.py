#!/usr/bin/env python3

from itertools import combinations

import aoclib

data = aoclib.get_data(year=2025, day=3)

one, two = 0, 0
for ln in data.splitlines():
    one += max(int("".join(x)) for x in combinations(ln, 2))
    two += max(int("".join(x)) for x in combinations(ln, 12))

print(f"ONE: {one}")
print(f"TWO: {two}")
