import sys
import pytest
import math


def get_continued_fraction(p, full_cycle=False):
    root = math.sqrt(p)
    assert root != math.floor(root)
    cycles = []
    x = math.floor(root)
    d = x
    n = p - x ** 2
    cycles.append((x, n, d))
    while True:
        x = math.floor((root + d) / n)
        d -= n * x
        if (x, n, d) in cycles:
            if full_cycle:
                return [c[0] for c in cycles]
            cycle = cycles[cycles.index((x, n, d)):]
            return [c[0] for c in cycle]
        cycles.append((x, n, d))
        d, n = n, d
        new_d = -n
        n = p - n * n
        n /= d
        d = new_d


def test_get_continued_fraction():
    assert get_continued_fraction(13) == [1, 1, 1, 1, 6]
    assert get_continued_fraction(23) == [1, 3, 1, 8]
    assert get_continued_fraction(2) == [2]


def has_odd_fraction_length(p):
    root = math.sqrt(p)
    if root == math.floor(root):
        return False
    return len(get_continued_fraction(p)) % 2 == 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum([has_odd_fraction_length(i) for i in range(int(sys.argv[-1]) + 1)])
