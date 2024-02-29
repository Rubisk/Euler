import sys
import pytest


def get_diagonal_spiral_sum(n):
    assert n % 2 == 1
    total = 1
    s = 4
    increase = 20
    for i in range(n / 2):
        s += increase
        increase += 32
        total += s
    return total


def test_get_diagonal_spiral_sum():
    assert get_diagonal_spiral_sum(5) == 101


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_diagonal_spiral_sum(int(sys.argv[1]))
