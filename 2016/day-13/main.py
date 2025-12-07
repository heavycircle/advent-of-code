#!/usr/bin/env python3

from collections import deque

import aoclib

data = aoclib.get_data(day=13, year=2016)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()


def isopen(x, y):
    """Is (x,y) open or a wall?"""
    s = x * x + 3 * x + 2 * x * y + y + y * y
    return bin(s)[2:].count("1") % 2 == 0


def bfs(cur, dst):
    s = set()

    q.append(cur)
    while q:
        x, y = q.popleft()
        s.add((x, y))

        if (x, y) == dst:
            break

        for dx, dy in dirs:
            if x + dx < 0 or y + dy < 0:
                continue
            if (x + dx, y + dy) in s:
                continue
            if isopen(x + dx, y + dy):
                q.append((x + dx, y + dy))

    return len(s)


print("ONE:", bfs((1, 1), (31, 39)))
