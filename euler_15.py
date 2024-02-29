import pytest
import numpy as np
import sys


def get_number_of_paths(n):
    above = 1
    for x in range(n + 1, n * 2 + 1):
        above *= x
    below = 1
    for x in range(1, n + 1):
        below *= x
    return above/below


def test_get_number_of_paths():
    assert get_number_of_paths(2) == 6
    assert get_number_of_paths(3) == 20


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_number_of_paths(int(sys.argv[-1]))
