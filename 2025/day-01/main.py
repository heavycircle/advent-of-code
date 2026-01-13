#!/usr/bin/env python3

import sys

import numpy as np


data = iter(sys.stdin.readline, "")

lock = np.array([50, 49])
one = 0
two = 0
for ln in data:
    dir, count = ln[0], int(ln[1:])

    if dir == "L":
        lock -= count
    elif dir == "R":
        lock += count

    spins = lock // 100
    two += min(abs(spins))

    lock %= 100
    if lock[0] == 0:
        one += 1
        two += 1


print(f"ONE: {one}")
print(f"TWO: {two}")
