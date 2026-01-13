#!/usr/bin/env python3

import functools as ft
import sys


# networkx was super tempting today until it died on part 2.
# The graph has 596 nodes and 1696 edges. We need a caching
# solution to get this done.

G = {k[:-1]: v for k, *v in map(str.split, iter(sys.stdin.readline, ""))}


@ft.cache
def count(node, dac=False, fft=False):
    match node:
        case "out":
            return dac and fft
        case "dac":
            dac = True
        case "fft":
            fft = True

    return sum(count(n, dac, fft) for n in G[node])


print(f"ONE: {count('you', True, True)}")
print(f"TWO: {count('svr', False, False)}")
