#!/usr/bin/env python3

import aoclib

data = aoclib.get_data(year=2025, day=5).split("\n\n")

ranges = sorted(tuple(map(int, ln.split("-"))) for ln in data[0].splitlines())
ids = list(map(int, data[1].splitlines()))

# Part One
one = sum(any(lo <= i <= hi for lo, hi in ranges) for i in ids)
print(f"ONE: {one}")


# Part Two
def merge():
    """Get all unique ranges"""
    it = iter(ranges)
    lo, hi = next(it)
    for l, h in it:
        if l <= hi:
            hi = max(hi, h)
        else:
            yield (lo, hi)
            lo, hi = l, h
    yield (lo, hi)


two = sum(hi - lo + 1 for lo, hi in merge())
print(f"TWO: {two}")
