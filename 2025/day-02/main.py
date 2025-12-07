#!/usr/bin/env python3

from re import match

import aoclib

data = aoclib.get_data(year=2025, day=2)


one, two = 0, 0
for s in data.split(","):
    a, b = list(map(int, s.split("-")))

    for i in range(a, b + 1):
        s = str(i)
        if match(r"^(\d+)\1$", s):
            one += i
        if match(r"^(\d+)\1+$", s):
            two += i


print("ONE", one)
print("TWO", two)
