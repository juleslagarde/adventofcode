import sys


times     = [int(x) for x in sys.stdin.readline().split(" ")[1:] if x]
distances = [int(x) for x in sys.stdin.readline().split(" ")[1:] if x]

part2 = True
if part2:
    times = [int("".join(map(str, times)))]
    distances = [int("".join(map(str, distances)))]


prod0 = 1
for t, d in zip(times, distances):
    sum0 = 0
    for x in range(0, t+1):
        if x*(t-x) > d:
            sum0 += 1
    prod0 *= sum0
print("result:", prod0)


