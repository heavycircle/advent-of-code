#!/usr/bin/env python3

import aoclib

def one():
    return sum(eval(s) for s in data.splitlines())

def two():
    s = 0
    lst = []
    while True:
        for ln in data.splitlines():
            s += eval(ln)
            if s in lst:
                return s
            lst.append(s)

data = aoclib.get_data(year=2018, day=1)

print(f"ONE: {one()}")
print(f"TWO: {two()}")
