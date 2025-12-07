#!/usr/bin/env python3

import itertools as it
import sys

coords = set(
    (r, c)
    for r, ln in enumerate(iter(sys.stdin.readline, ""))
    for c, ch in enumerate(ln.strip())
    if ch == "@"
)


def valid(lst):
    """Check how many deltas are in each direction"""
    return set(
        (x, y)
        for x, y in lst
        if sum((x + dx, y + dy) in lst for dx, dy in it.product((-1, 0, 1), repeat=2))
        <= 4
    )


# Part One
one = len(valid(coords))
print(f"ONE: {one}")

# Part Two
i = it.accumulate(it.repeat(None), lambda x, y: x - valid(x), initial=coords)
u = next(s for s, t in it.pairwise(i) if s == t)
two = len(coords - u)
print(f"TWO: {two}")
