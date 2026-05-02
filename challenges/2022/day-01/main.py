#!/usr/bin/env python3

"""
--- Day 1: Calorie Counting ---
"""

import aoclib


d = [z.split() for z in aoclib.get_data(day=1, year=2022).split("\n\n")]

# Part 1
n = [sum([int(x) for x in z]) for z in d]
print("Part 1:", max(n))

# Part 2
n = sorted(n, reverse=True)
print("Part 2:", sum(n[:3]))
