import sys
import pytest


def find_first_above(n, maximum):
    k = 0
    n_above_k = 1
    while n_above_k < maximum:
        if k > (n + 1) / 2:
            return -1
        n_above_k *= (n - k)
        k += 1
        n_above_k /= k
    return k


def find_number_above(n, maximum):
    k = find_first_above(n, maximum)
    n += 1
    if k == -1:
        return 0
    return n - 2 * k


def test_find_first_above():
    assert find_first_above(5, 10) == 2
    assert find_first_above(5, 6) == 2
    assert find_first_above(23, 1E6) == 10


def test_find_all_above():
    assert find_number_above(3, 3) == 2
    assert find_number_above(4, 4) == 3
    assert find_number_above(4, 6) == 1
    assert find_number_above(5, 6) == 2
    assert find_number_above(23, 1E6) == 4
    assert find_number_above(22, 1E6) == 0


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum([find_number_above(m, int(sys.argv[-2]))
                   for m in range(int(sys.argv[-1]) + 1)])
