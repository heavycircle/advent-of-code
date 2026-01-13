#!/usr/bin/env python3

"""
--- Day 3: Mull It Over ---
"""

import re

import aoclib


data = aoclib.get_data(day=3, year=2024)

matches = re.findall(r"mul\((\d+),(\d+)\)", data)
ONE = sum(int(x) * int(y) for x, y in matches)
print("ONE:", ONE)

matches = re.findall(r"mul\(\d+\,\d+\)|do\(\)|don't\(\)", data)
TWO = 0
DO = True
for match in matches:
    nums = re.findall(r"\d+", match)
    if len(nums) == 0:
        DO = "don" not in match
    elif DO:
        TWO += int(nums[0]) * int(nums[1])
print("TWO:", TWO)
