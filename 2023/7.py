import sys
from collections import Counter
import math
from pprint import pprint

cards  = "23456789TJQKA"
cards2 = "J23456789TQKA"

card_to_strength = {v: i for i, v in enumerate(cards)}
card2_to_strength = {v: i for i, v in enumerate(cards2)}
strengthBase = len(card_to_strength)


# calculate a score that will be used to order the cards
# each type of combinaison maps to a [0,1[ range.
# here is the list or ranges:
#   Five of a kind => [6,7[
#   Four of a kind => [5,6[
#   Full house => [4,5[
#   Three of a kind => [3,4[
#   Two pair => [2,3[
#   One pair => [1,2[
#   High card => [0,1[
def score(hand, card_strength, part2):
    # this function basicly append digit in base 'strengthBase', that way the first card has more value than the others
    # exemple: if strengthBase == 10, then a hand with the following strengths 1,7,2,3,4 would output a partial_score of 17234
    def partial_score(hand):
        s = 0
        for card in hand:
            s *= strengthBase
            s += card_strength[card]
        return s
    #def partial_score(cards): # I first thought that the best card was the next thing to compare (and not only the first)
    #    s = 0
    #    for card in cards:
    #        s *= strengthBase
    #        s += card_strength[card[0]]
    #    return s
    counter = Counter(hand)
    count = dict(counter.items())
    if part2 and "J" in count:
        J = counter.pop("J")
        if J != 5:  # if there is only J in hands keep them
            count[counter.most_common(1)[0][0]] += J
            del count["J"]
    assert sum(v for k,v in count.items())==5, f"not five cards ??? {hand} {counter.most_common(1)[0][0]} {count}"
    cards = ((c, i) for c, i in count.items())
    cards = sorted(cards, key=lambda x: x[1]*strengthBase+card_strength[x[0]], reverse=True)
    shift = 0
    match cards:
        case [_]:
            shift = 6  # Five of a kind
        case [(_, 4), (_, 1)]:
            shift = 5  # Four of a kind
        case [(_, 3), (_, 2)]:
            shift = 4  # Full house
        case [(_, 3), _, _]:
            shift = 3  # Three of a kind
        case [(_, 2), (_, 2), _]:
            shift = 2  # Two pair
        case [(_, 2), _, _, _]:
            shift = 1  # One pair
        case [_, _, _, _, _]:
            shift = 0  # High card
        case _:
            print("cards not matching:", cards)
            sys.exit(1)
    return shift + (partial_score(hand)/math.pow(strengthBase, 5))

hands = [line.split(" ") for line in sys.stdin]
hands1 = sorted([(score(hand, card_to_strength, False), hand, int(mult)) for hand, mult in hands], key=lambda x: x[0])
hands2 = sorted([(score(hand, card2_to_strength, True), hand, int(mult)) for hand, mult in hands], key=lambda x: x[0])
pprint(hands)
print("part1", sum((i+1)*mult for i,(_, _, mult) in enumerate(hands1)))
print("part2", sum((i+1)*mult for i,(_, _, mult) in enumerate(hands2)))
