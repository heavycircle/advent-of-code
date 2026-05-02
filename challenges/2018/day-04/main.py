#!/usr/bin/env python3

from collections import Counter, defaultdict
from datetime import datetime

from aoclib import get_data


data = get_data(year=2018, day=4)

guards = defaultdict(Counter)

# Just make the LSP happy
start = datetime(2018, 1, 1)
g = 0

for t, m in [ln.split("] ") for ln in sorted(data.splitlines()) if ln]:
    t = datetime.strptime(t, "[%Y-%m-%d %H:%M")
    if "#" in m:
        g = int(m.split("#")[1].split()[0])
    if "falls" in m:
        start = t
    if "wakes" in m:
        minutes = int((t - start).total_seconds() // 60)
        guards[g].update(Counter((start.minute + i) % 60 for i in range(minutes)))


def one():
    _, id = max((sum(c.values()), id) for id, c in guards.items())
    return id * guards[id].most_common()[0][0]


def two():
    (_, minute), id = max((c.most_common()[0][::-1], id) for id, c in guards.items())
    return id * minute


print("ONE:", one())
print("TWO:", two())
