import sys
import pytest
import numpy as np


TEST_SIZE = 1000


def get_digit(number, digit):
    return int(str(number)[digit - 1])


def get_digit_champernowne(n):
    i = 1
    d = 1
    while i * 9 * d < n:
        n -= i * 9 * d
        i *= 10
        d += 1
    return get_digit((n - 1) / d + i, n % d)


def test_get_digit_champernowne():
    i = 1
    string = ""
    while len(string) < TEST_SIZE:
        string += str(i)
        i += 1
    for j in range(len(string)):
        assert int(string[j]) == get_digit_champernowne(j + 1)


def test_get_digit():
    assert get_digit(25, 2) == 5
    assert get_digit(123456, 4) == 4


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print np.prod([get_digit_champernowne(int(x)) for x in sys.argv[1:]])
