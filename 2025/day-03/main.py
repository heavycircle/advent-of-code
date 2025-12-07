#!/usr/bin/env python3

import sys

data = [list(map(int, ln.strip())) for ln in iter(sys.stdin.readline, "")]


def best(lst, digits=2):
    if digits == 1:
        return max(lst)

    d = max(lst[: -digits + 1])
    i = lst.index(d)
    return d * 10 ** (digits - 1) + best(lst[i + 1 :], digits - 1)


print(f"ONE: {sum(map(best, data))}")
print(f"TWO: {sum(best(ln, 12) for ln in data)}")
