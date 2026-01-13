#!/usr/bin/env python3

import itertools as it
import sys

import z3


one, two = 0, 0
for ln in iter(sys.stdin.readline, ""):
    light, *wires, joltage = ln.split()

    light = light[1:-1]
    pattern = [set(map(int, x[1:-1].split(","))) for x in wires]
    joltage = list(map(int, joltage[1:-1].split(",")))

    one += next(
        i
        for i in it.count(0)
        for comb in it.combinations(pattern, i)
        if "".join(".#"[sum(i in p for p in comb) % 2] for i in range(len(light))) == light
    )

    # I can't say I knew how to do this part on my own. Definitely got help
    # and need to learn how to use z3 more.

    init = [z3.Int(f"p{i}") for i in range(len(pattern))]

    solve = z3.Optimize()
    solve.add(z3.And([p >= 0 for p in init]))
    solve.add(z3.And([sum(init[j] for j, b in enumerate(pattern) if i in b) == jolt for i, jolt in enumerate(joltage)]))
    solve.minimize(sum(init))
    assert solve.check() == z3.sat

    m = solve.model()
    two += sum(m[p].as_long() for p in init)

print(f"ONE: {one}")
print(f"TWO: {two}")
