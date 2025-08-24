#!/usr/bin/env python3

from itertools import combinations

from aoclib import get_data

data = get_data(year=2020, day=1)
lst = list(map(int, data.splitlines()))

one = list(a * b for a, b in combinations(lst, 2) if a + b == 2020)[0]
print("ONE:", one)

two = list(a * b * c for a, b, c in combinations(lst, 3) if a + b + c == 2020)[0]
print("TWO:", two)
