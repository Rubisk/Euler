import sys
import pytest
import itertools as it
from fraction import Fraction


def ggd(a, b):
    if 0 in (a, b):
        return 1
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)


def product(iterable):
    p = 1
    for element in iterable:
        p *= element
    return p


def get_win_chance(turns):
    total_chance = 0
    for i in range(turns / 2 + 1, turns + 1):
        for c in it.combinations(range(2, turns + 2), i):
            chance = product([Fraction(1, n) if n in c else Fraction((n - 1), n) for n in range(2, turns + 2)])
            total_chance += chance
    return total_chance


def win_chance_to_pounds(chance):
    return chance.denominator / chance.numerator


def test_win_chance():
    assert get_win_chance(4) == Fraction(11, 120)
    assert win_chance_to_pounds(get_win_chance(4)) == 10


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print win_chance_to_pounds(get_win_chance(int(sys.argv[-1])))
