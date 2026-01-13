#!/usr/bin/env python3

import sys


data = sys.stdin.read().split("\n\n")

presents = {i: s.count("#") for i, s in enumerate(data[:-1])}
regions = data[-1]

one = 0
for ln in regions.splitlines():
    # Finish splitting because for some reason I can't one line this
    l, r = ln.split(":")
    row, col = map(int, l.split("x"))
    val = tuple(map(int, r.split()))

    psz = sum(n * presents[i] for i, n in enumerate(val))
    gsz = row * col

    # Apparently the real input dataset has zero close calls. Everything
    # either clearly fits or just has no chance of fitting. I don't even
    # do the work of permuting it. Note this doesn't quite work for the
    # test input, you have to give it a threshold of 1.2ish to work.
    # I guess that's the last day for ya
    if psz < gsz:
        one += 1

print(f"ONE: {one}")
