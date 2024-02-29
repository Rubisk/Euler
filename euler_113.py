import sys
import pytest


def faculty(n):
    if n in (0, 1):
        return 1
    return n * faculty(n - 1)


def choose(n, k):
    return faculty(n) / faculty(k) / faculty(n - k)


def get_number_of_not_bouncy_numbers(digits):
    return 2 * choose(9 + digits, digits) + sum([choose(9 + j, j) for j in range(1, digits)]) - digits * 10 - 1


def test_get_number_of_not_bouncy_numbers():
    assert get_number_of_not_bouncy_numbers(6) == 12951
    assert get_number_of_not_bouncy_numbers(10) == 277032


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_number_of_not_bouncy_numbers(int(sys.argv[-1]))
