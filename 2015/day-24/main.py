#!/usr/bin/env python3

"""
--- Day 24: It Hangs in the Balance ---
"""

from functools import reduce
from itertools import combinations
from operator import mul

import aoclib

stream = aoclib.get_data(year=2015, day=24).splitlines()
data = sorted(list(map(int, stream)), reverse=True)


def solve(d, p):
    """Find smallest QES for a given number of groups"""
    t = sum(d) // p
    for i in range(len(d)):
        q = [reduce(mul, c) for c in combinations(d, i) if sum(c) == t]
        if q:
            return min(q)


print("Part 1:", solve(data, 3))
print("Part 2:", solve(data, 4))
