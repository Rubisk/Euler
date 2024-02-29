import sys
import pytest
import math


def get_solutions(count):
    n = 1
    found = 0
    while found < count:
        for d in (1, -1):
            root = math.sqrt(5 * n ** 2 + d)
            if root.is_integer():
                m = root + 2 * n
                yield long(n ** 2 + m ** 2)
                found += 1
        n += 1


def test_get_solutions():
    assert 17 in list(get_solutions(2))
    assert 305 in list(get_solutions(6))


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print long(sum(get_solutions(int(sys.argv[1]))))
