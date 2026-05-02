#!/usr/bin/env python3

import re
import sys


data = [tuple(map(int, ln.split("-"))) for ln in sys.stdin.readline().strip().split(",")]

one, two = 0, 0
for a, b in data:
    for i in range(a, b + 1):
        s = str(i)
        if re.match(r"^(\d+)\1$", s):
            one += i
        if re.match(r"^(\d+)\1+$", s):
            two += i


print("ONE", one)
print("TWO", two)
