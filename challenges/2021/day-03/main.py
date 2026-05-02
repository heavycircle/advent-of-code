#!/usr/bin/env python3

from collections import Counter

import aoclib


data = aoclib.get_data(year=2021, day=3).splitlines()
data = [z.strip() for z in data]


def most_common(data, prefer: int):
    """Get the most common values at each index, preferring 'prefer' in ties"""
    tpose = ["".join(c) for c in zip(*data)]

    res = []
    for col in tpose:
        c = Counter(col)
        zeros = c.get("0", 0)
        ones = c.get("1", 0)
        if prefer == 1:
            res.append("1" if ones >= zeros else "0")
        else:
            res.append("0" if ones >= zeros else "1")
    return "".join(res)


def filter_most(data, i=0):
    """Filter the most common (oxygen)"""
    if len(data) == 1:
        return data

    gamma = most_common(data, 1)
    mc = [ln for ln in data if ln[i] == gamma[i]]
    return filter_most(mc, i + 1)


def filter_least(data, i=0):
    """Filter the least common (carbon)"""
    if len(data) == 1:
        return data

    epsilon = most_common(data, 0)
    lc = [ln for ln in data if ln[i] == epsilon[i]]
    return filter_least(lc, i + 1)


gamma = most_common(data, 1)
epsilon = most_common(data, 0)
print(f"ONE: {int(gamma, 2) * int(epsilon, 2)}")

oxygen = filter_most(data, 0)
carbon = filter_least(data, 0)
print(f"TWO: {int(oxygen[0], 2) * int(carbon[0], 2)}")
