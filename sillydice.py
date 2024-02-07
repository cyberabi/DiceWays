"""
  Fair polyhedral D&D dice using only a D6
  Christopher Burke 1/3/24
"""
import random
from collections import Counter


# Returns integer 1 to 6
# All other dice are built on d6()
def d6() -> int:
    return random.randrange(6) + 1


"""
  Utilities
"""

# Returns integer 0 to 1; used for d8(), d10(), d12()
def d2() -> int:
    return int((d6() - 1) / 3)


# Returns integer 1 to 5; used for d10() and d20()
def d5() -> int:
    return roll if (6 > (roll := d6())) else d5()


# Returns sum of rolling a given die n times
def nDx( dicecount : int, dicefunc):
    return sum([dicefunc() for roll in range(dicecount)])


"""
  Simulated polyhedrals
"""

# Returns integer 1 to 4
def d4() -> int:
    return d2() * 2 + d2() + 1


# Returns integer 1 to 8
def d8() -> int:
    return d2() * 4 + d4()


# Returns integer 0 to 9 (special case)
def d10() -> int:
    return d2() * 5 + d5() - 1


# Returns integer 1 to 12
def d12() -> int:
    return d2() * 6 + d6()


# Returns integer 1 to 20
def d20() -> int:
    return (d4() - 1) * 5 + d5()


# Returns integer 0 to 99 (special case)
def d100() -> int:
    return d10() * 10 + d10()


if __name__ == '__main__':
    """
      Test cases to show uniform distribution
    """

    # Single dice, histogram for 1,000,000 rolls
    print('\nSingle dice:')
    for f in [d4, d6, d8, d10, d12, d20, d100]:
        print( '\n', f.__name__, sorted(Counter([f() for roll in range(1000000)]).items()) )

    # Multiple dice, histogram for 1,000,000 rolls
    print('\nGroups of dice:')
    for n, f in [(2, d6), (3, d6), (2, d8)]:
        print( '\n', n, f.__name__, sorted(Counter([nDx(n, f) for roll in range(1000000)]).items()) )
