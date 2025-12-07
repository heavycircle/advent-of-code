#!/usr/bin/env python3

"""
--- Day 3: Rucksack Reorganization ---
"""

import re
import string

import aoclib


def i(x):
    """Get index of letter in alphabet"""
    return (string.ascii_lowercase + string.ascii_uppercase).index(x) + 1


lines = aoclib.get_data(day=3, year=2022)
halves = [(x[: len(x) // 2], x[len(x) // 2 :]) for x in lines.splitlines()]

one = [i([a for a in x[0] if a in x[1]][0]) for x in halves]
print("Part 1:", sum(one))

thirds = [x.strip().splitlines() for x in re.findall("((?:[^\n]+\n?){1,3})", lines)]
two = [i([a for a in x[0] if a in x[1] and a in x[2]][0]) for x in thirds]
print("Part 2:", sum(two))
