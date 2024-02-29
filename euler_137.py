import sys
import pytest
import math


def get_rationals(target):
    solution_count = 0
    n = 1L
    while True:
        if math.sqrt(5 * n ** 2 + 4).is_integer():
            solution_count += 1
            if solution_count == target:
                m = (math.sqrt(5 * n ** 2 + 4) + n) / 2
                return long(m * n)
        n += 1


def test_get_rationals():
    assert get_rationals(10) == 74049690


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_rationals(int(sys.argv[1]))
