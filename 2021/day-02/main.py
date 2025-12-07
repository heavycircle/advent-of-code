#!/usr/bin/env python3

import aoclib

data = aoclib.get_data(year=2021, day=2)

x, y = 0, 0
for ln in data.splitlines():
    k, v = ln.split(" ")
    if k == "forward":
        x += int(v)
    elif k == "up":
        y -= int(v)
    elif k == "down":
        y += int(v)
    else:
        print("bad")

print(f"ONE: {x * y}")

x, y, aim = 0, 0, 0
for ln in data.splitlines():
    k, v = ln.split(" ")
    if k == "forward":
        x += int(v)
        y += aim * int(v)
    elif k == "up":
        aim -= int(v)
    elif k == "down":
        aim += int(v)
    else:
        print("bad")

print(f"TWO: {x * y}")
