import sys
import pytest


def get_digits_sum(n):
    string = str(n)
    return sum([int(d) for d in string if d in "0123456789"])


def calculate_digits(n):
    x = 1
    y = 1
    z = 1
    for _ in range(10):
        x *= n
    for _ in range(10):
        y *= x
    for _ in range(10):
        z *= y

    return get_digits_sum(z)


def test_get_digits_sum():
    assert get_digits_sum(12345) == 15
    assert get_digits_sum(1000000000000L) == 1


def test_calculate_digits():
    assert calculate_digits(1) == 1


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print calculate_digits(int(sys.argv[-1]))
