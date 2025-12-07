#!/usr/bin/env python3

import sys

lst = list(map(int, iter(sys.stdin.readline, "")))

one = sum(1 for a, b in zip(lst, lst[1:]) if b > a)
print("ONE:", one)

win = [sum(w) for w in zip(lst, lst[1:], lst[2:])]
two = sum(1 for a, b in zip(win, win[1:]) if b > a)
print("TWO:", two)
