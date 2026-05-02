#!/usr/bin/env python3
from __future__ import annotations

import sys

import numpy as np

from advent_of_code.api import ui


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


ui.out_success(f"ONE: {one}")
ui.out_success(f"TWO: {two}")
