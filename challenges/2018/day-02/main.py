#!/usr/bin/env python3

from aoclib import get_data


data = get_data(year=2018, day=2)


def one():
    two, three = 0, 0
    for ln in data.splitlines():
        m = {x: ln.count(x) for x in set(ln)}
        two += int(any(y == 2 for _, y in m.items()))
        three += int(any(y == 3 for _, y in m.items()))

    return two * three


def two():
    nd = sorted(data.splitlines())
    for r in nd:
        for s in nd:
            diff = 0
            for i, c in enumerate(r):
                if c != s[i]:
                    diff += 1
            if diff == 1:
                return s


print("ONE:", one())
print("TWO:", two())
