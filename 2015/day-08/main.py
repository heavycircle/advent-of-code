#!/usr/bin/env python3

"""
--- Day 8: Matchsticks ---
"""

import aoclib


stream = aoclib.get_data(day=8, year=2015).splitlines()

ONE = 0
for l in stream:
    ONE += len(l) - len(eval(l))

TWO = 0
for l in stream:
    TWO += 2 + l.count('"') + l.count("\\")

print("Part 1:", ONE)
print("Part 2:", TWO)
