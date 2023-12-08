import sys
from collections import defaultdict
import math

valid_game = {"red": 12, "green": 13, "blue": 14}
sum = 0
sumPower = 0
for i, line in enumerate(sys.stdin):
    game = defaultdict(lambda: 0)
    sets = line.split(": ")[1].split(";")
    for set in sets:
        for n, color in (x.strip().split(" ") for x in set.split(",")):
            game[color] = max(game[color], int(n))
    sumPower += math.prod(game.values())
    for color, n in game.items():
        if n > valid_game[color]:
            break
    else:
        sum += i+1  # game id == line number
print(f"sum : {sum}")
print(f"sumPower : {sumPower}")
