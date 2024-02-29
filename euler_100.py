import math
import sys
import pytest


def find_first_with_min_balls(minimum):
    sequence = [1, 3]
    while math.ceil(math.sqrt(sequence[-1] * (sequence[-1] - 1) * 2)) < minimum:
        sequence.append(6 * sequence[-1] - sequence[-2] - 2)
    return sequence[-1]


def test_find_first_with_min_balls():
    assert find_first_with_min_balls(80) == 120


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_first_with_min_balls(int(sys.argv[-1]))
