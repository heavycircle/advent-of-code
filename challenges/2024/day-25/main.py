#!/usr/bin/env python3

"""
--- Day 25: Code Chronicle ---
"""

from itertools import combinations

import aoclib


data = aoclib.get_data(day=25, year=2024).split("\n\n")

ONE = sum(not any(x == y == "#" for x, y in zip(a, b)) for a, b in combinations(data, 2))
print("ONE:", ONE)
