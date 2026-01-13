#!/usr/bin/env python3

import re
from collections import defaultdict

import aoclib


data = aoclib.get_data(year=2018, day=3).splitlines()

# Populate the seen
seen = defaultdict(int)
claims = [tuple(map(int, re.findall(r"-?\d+", s))) for s in data]
for c, x, y, w, h in claims:
    for i in range(x, x + w):
        for j in range(y, y + h):
            seen[(i, j)] += 1

# Get items seen more than once
print("ONE:", sum(1 for _, b in seen.items() if b > 1))

for c, x, y, w, h in claims:
    # Check if everything is seen exactly once
    if all(seen[(i, j)] == 1 for i in range(x, x + w) for j in range(y, y + h)):
        print("TWO:", c)
        break
