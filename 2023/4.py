import sys
import math
from collections import defaultdict

counts = defaultdict(lambda: 1)
lines = sys.stdin.readlines()

sum0 = 0
for i, line in enumerate(lines):
    print(line)
    wining_nbs, card_nbs = map(lambda x: set(int(y) for y in x.strip().split(" ") if len(y) > 0),  line.split(": ")[1].split(" | "))
    print(wining_nbs, card_nbs)
    matching_nbs = wining_nbs.intersection(card_nbs)
    print(matching_nbs)
    points = math.floor(math.pow(2, len(matching_nbs)-1))
    print(f"game {i+1}: '{points}' points")
    for j in range(i+1, i+1+len(matching_nbs)):
        print(f"{i},{j} = {counts[j]}+{counts[i]}")
        counts[j] = counts[j]+counts[i]
    sum0 += points

print(f"sum : {sum0}")
print("number of cards: "+sum(counts[i] for i in range(len(lines))))
