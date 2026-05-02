#!/usr/bin/env python3

import math
import sys


problems = [list(ln) for ln in iter(sys.stdin.readline, "")]
cols = zip(*problems)

one, two = 0, 0
while col := next(cols, None):
    # Get the operation
    op = sum if col[-1] == "+" else math.prod

    # Accumulators for operation digits
    n1 = col[:-1]
    n2 = ["".join(c for c in col if c.isdigit())]

    # Get the rest of the digits (1: horizontal, 2: vertical)
    while (col := next(cols)) and not all(c.isspace() for c in col):
        n1 = [n + c for n, c in zip(n1, col)]
        n2.append("".join(c for c in col if c.isdigit()))

    one += op(map(int, n1))
    two += op(map(int, n2))


print(f"ONE: {one}")
print(f"TWO: {two}")
