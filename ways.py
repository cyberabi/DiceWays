"""
  Figure out the number of ways each sum of some number of dice can be rolled.
  Optimized but suboptimal - do your own homework :-)
  Christopher Burke, 1/4/23
"""

import random

solved = []

def reset_solved(sides, dice):
    global solved
    solved = [[-1 for value in range(sides * dice_left + 1)] for dice_left in range(dice + 1)]

def ways(total, sides, dice, depth) -> int:
    #print(" " * depth, "die", depth, ":", total, "remain")
    # not a viable solution if the total exceeds max possible
    # not a viable solution if the total is less than the number of dice
    if total > sides * dice or total < dice or 0 >= total:
        return 0

    #print(f'Checking solved[D:{dice}][T:{total}]')
    known = (solved[dice])[total]
    if -1 != known:
        #print(" " * depth, "already solved", known)
        return known

    alternatives = 0

    if total <= sides and 1 == dice:
        # One solution for rolling the exact remaining total on this die
        alternatives += 1
        # Additional solutions for rolling less
        for roll in range(total - 1):
            alternatives += ways(total - (roll + 1), sides, dice - 1, depth + 1)
    else:
        usable_sides = min(sides, total)
        for roll in range(usable_sides):
            alternatives += ways(total - (roll + 1), sides, dice - 1, depth + 1)
    #print(" " * depth, "viable alternatives", alternatives)
    (solved[dice])[total] = alternatives
    return alternatives

if __name__ == '__main__':
    # Tests
    #for dice, sides in [(3, 6), (5, 20), (1, 100)]:
    for dice, sides in [(3,6), (5,20), (1,100), (-1,6), (3,-1), (20, 20)]:
        print(f'\n{dice}d{sides} Test:')
        reset_solved(sides, dice)
        for total in range(-2, limit if (limit := dice * sides + 3) > 0 else 21):
            print(total, ways(total, sides, dice, 1))
