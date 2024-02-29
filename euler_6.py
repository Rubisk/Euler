import pytest
import sys


def get_difference(n):
    difference = get_square_of_sum(n) - get_sum_of_squares(n)
    return difference if difference >= 0 else -difference


def get_square_of_sum(n):
    s = n * (n + 1) / 2
    return s * s


def get_sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def test_get_sum_of_squares():
    assert get_sum_of_squares(1) == 1
    assert get_sum_of_squares(10) == 385


def test_get_square_of_sum():
    assert get_square_of_sum(1) == 1
    assert get_square_of_sum(10) == 3025


if __name__ == "__main__":
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_difference(int(sys.argv[-1]))
