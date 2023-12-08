import sys
from pprint import pprint
from collections import deque
from math import gcd
from functools import reduce


steps = sys.stdin.readline().strip()

_ = sys.stdin.readline()

map0 = dict()
for line in sys.stdin:
    k, v = line.split(" = ")
    map0[k] = {k: v for k, v in zip("LR", v.strip()[1:-1].split(", "))}


######################## part1
i = 0
current = 'AAA'
target = 'ZZZ'
while current != target:
    current = map0[current][steps[i % len(steps)]]
    i += 1
print("part1:", i)


######################## part2
startNodes = [x for x in map0.keys() if x[-1] == "A"]
counts = []
for start in startNodes:
    current = start
    i = 0
    while current[-1] != "Z":
        current = map0[current][steps[i % len(steps)]]
        i += 1
    counts.append(i)


def lcm(a, b):  # least common multiple
    return a * b // gcd(a, b)
print("part2:", reduce(lcm, counts))
