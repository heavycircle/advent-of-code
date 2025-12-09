#!/usr/bin/env python3

import itertools as it
import math
import sys

data = [tuple(map(int, ln.split(","))) for ln in iter(sys.stdin.readline, "")]

one = max(math.prod(abs(y - x) + 1 for x, y in zip(a, b)) for a, b in it.combinations(data, 2))
print(one)


def inside(pt1, pt2, polygon):
    xmin, xmax = sorted([pt1[0], pt2[0]])
    ymin, ymax = sorted([pt1[1], pt2[1]])

    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if y1 == y2 and ymin < y1 < ymax and (min(x1, x2) <= xmin < max(x1, x2) or min(x1, x2) < xmax <= max(x1, x2)):
            return False
        elif x1 == x2 and xmin < x1 < xmax and (min(y1, y2) <= ymin < max(y1, y2) or min(y1, y2) < ymax <= max(y1, y2)):
            return False
    return True


two = max(math.prod(abs(y - x) + 1 for x, y in zip(a, b)) for a, b in it.combinations(data, 2) if inside(a, b, data))
print(two)
