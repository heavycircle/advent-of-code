#!/usr/bin/env python3

from __future__ import annotations

import sys


# Data, adding high and low
data = sorted(map(int, sys.stdin.readlines()))
lo, hi = 0, max(data) + 3
data = [lo] + data + [hi]

# ONE: 1s and 3s in list
diffs = [b - a for a, b in zip(data, data[1:], strict=False)]
one = diffs.count(1) * diffs.count(3)
print("ONE:", one)

# TWO: DP for number of paths
ways = {0: 1}
for s in data:
    if s != 0:
        ways[s] = ways.get(s - 1, 0) + ways.get(s - 2, 0) + ways.get(s - 3, 0)
print("TWO:", ways[hi])
