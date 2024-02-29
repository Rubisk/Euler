import math
import sys
import pytest


def is_triangular(n):
    return math.sqrt(8 * n + 1).is_integer()


def is_pentagonal(n):
    root = math.sqrt(24 * n + 1)
    return root.is_integer()


def is_triangular_pentagonal_hexagonal(n):
    for test in (is_triangular, is_pentagonal):
        if not test(n):
            print test
            return False
    return True


def find_triangular_pentagonal(number):
    n = 1
    c = 0
    while c < number:
        n += 1
        h = n * (2 * n - 1)
        if is_pentagonal(h):
            c += 1
            yield h


def test_tests():
    assert is_triangular_pentagonal_hexagonal(40755)

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print [x for x in find_triangular_pentagonal(int(sys.argv[-1]))]