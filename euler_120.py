import sys
import pytest


def get_r_max(a):
    if a % 2 == 0:
        return a * (a - 2)
    else:
        return a * (a - 1)


def test_get_r_max():
    assert get_r_max(7) == 42


def sum_r_max(minimum, maximum):
    return sum([get_r_max(a) for a in range(minimum, maximum)])


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum_r_max(int(sys.argv[-2]), int(sys.argv[-1]))
