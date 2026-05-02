#!/usr/bin/env python3

"""
--- Day 1: Not Quite Lisp ---
"""

import aoclib


stream = aoclib.get_data(day=1, year=2015)

one = stream.count("(") - stream.count(")")
i = 0
for two, c in enumerate(stream):
    if c == "(":
        i += 1
    else:
        i -= 1
    if i == -1:
        break

print("Part 1:", one)
print("Part 2:", two + 1)
