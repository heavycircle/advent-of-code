#!/usr/bin/env python3

"""
--- Day 12: JSAbacusFramework.io ---
"""

import json
import re

import aoclib

stream = aoclib.get_data(day=12, year=2015)

one = sum(map(int, re.findall(r"-?\d+", stream)))
print("Part 1:", one)


def recurse(obj):
    """Recursively sum all numbers in a JSON object"""
    if isinstance(obj, int):
        return obj
    if isinstance(obj, list):
        return sum(recurse(x) for x in obj)
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(recurse(x) for x in obj.values())
    return 0


two = recurse(json.loads(stream))
print("Part 2:", two)
