from sys import stdin
from itertools import groupby
from pprint import pprint

steps_names = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]


class MyInt(int):
    def __init__(self, x):
        super().__init__()

    def __str__(self):
        return f"{self:_}"

    def __repr__(self):
        return f"{self:_}"


seeds = [MyInt(x) for x in stdin.readline().split(":")[1].strip().split(' ')]
print("seeds:", seeds)


maps = []
_ = stdin.readline()  # skip line

lines = (x.strip() for x in stdin.readlines())  # read remaining lines

grouped_lines = (group for key, group in groupby(lines, lambda x: x != "") if key)
for lines in grouped_lines:
    next(lines)  # skip header line (eg. "seed-to-soil map:")
    maps.append([tuple(map(MyInt, line.split(" "))) for line in lines])

pprint(maps)

part2 = True
if part2:
    seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
    print("seed_ranges:", seed_ranges)

    def split_range(r, n):
        start, end = r
        if start < n < end:
            return ((start, n), (n, end))
        return None

    def does_overlaps(a, b):
        return max(a[0], b[0]) < min(a[1], b[1])

    def apply_map(map0, state):
        newstate = []
        q = list(state)
        while len(q) > 0 and (state_part := q.pop(0)):
            (sstart, sstop) = state_part
            for (rdest, rstart, rrange) in map0:
                rstop = rstart+rrange
                if does_overlaps((rstart, rstart+rrange), (sstart, sstop)):
                    break
            else:
                continue
            print(rdest, rstart, rrange, ":", state_part, "=>", end=" ")
            diff = rdest-rstart
            assert sstart < sstop, "hum"
            mid = state_part
            left = right = None
            if (pair := split_range(mid, rstart)) is not None:
                left, mid = pair
            if (pair := split_range(mid, rstop)) is not None:
                mid, right = pair
            if does_overlaps(state_part, (rstart, rstop)):
                newstate.append((MyInt(mid[0]+diff), MyInt(mid[1]+diff)))
                q += [x for x in (left, right) if x is not None]
            print(left, newstate[-1:], right)
        return newstate if len(newstate) > 0 else None

    seed_to_loc = dict()
    for i, map0 in enumerate(maps):
        for seed_range in seed_ranges:  # [:1]:
            state = seed_to_loc.get(seed_range, [seed_range])
            print(f"{i}: ", steps_names[i]+"-to-"+steps_names[i+1], " len:", len(state))
            if (newstate := apply_map(map0, state)) is not None:
                print("applied:", newstate)
                state = newstate
            else:
                print("None applied")
            seed_to_loc[seed_range] = state

    print(seed_to_loc)
    print(f"min: {min(sorted(a, key=lambda b:b[0])[0] for a in seed_to_loc.values())}")

if not part2:
    def apply_range(range0, state):
        (d, s, r) = range0
        diff = d-s
        return state+diff if s <= state < (s+r) else None

    seed_to_loc = dict()
    for seed in seeds:
        state = seed
        for i, map0 in enumerate(maps):
            for range0 in map0:
                if (newstate := apply_range(range0, state)) is not None:
                    state = newstate
                    break  # only one range per map
        seed_to_loc[seed] = state

    print(seed_to_loc)
    print(f"min: {min(seed_to_loc.values())}")

           #if sstart < rstart < sstop:  # range start in state
           #    newstate.append((sstart, rstart))
           #    if rstop < sstop:  # range completely inside the state
           #        newstate.append((rstart+diff, rstop+diff))
           #        newstate.append((rstop, sstop))
           #    else:  # range ends outside the state
           #        newstate.append((rstart+diff, sstop+diff))
           #elif rstart < sstart:  # range start before state
           #    if sstart < rstop <= sstop:  # range ends inside the state
           #        newstate.append((sstart+diff, rstop+diff))
           #        newstate.append((rstop, sstop))
           #    elif sstop <= rstop:  # state completely inside the range
           #        newstate.append((sstart+diff, sstop+diff))
           #    else:  # range completely before the state
           #        pass
           #else:  # range start after the state
           #    pass
