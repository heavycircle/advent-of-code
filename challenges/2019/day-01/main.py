#!/usr/bin/env python3

from aoclib import get_data


data = get_data(year=2019, day=1)


def fuel(f, inf):
    nf = f // 3 - 2
    if nf <= 0:
        return 0
    if not inf:
        return nf
    return nf + fuel(nf, inf)


one = sum(fuel(int(x), False) for x in data.splitlines())
print("ONE:", one)

two = sum(fuel(int(x), True) for x in data.splitlines())
print("TWO:", two)
