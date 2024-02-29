import sys
import pytest


def convert_to_one_fraction(expansion):
    expansion = [long(e) for e in expansion]
    if len(expansion) == 1:
        return expansion[0], 1
    if len(expansion) == 2:
        return expansion[0] * expansion[1] + 1, expansion[1]
    n = long(expansion[-1])
    d = 1L
    for a in reversed(expansion[1:-1]):
        d, n = n, d + a * n
    return d + expansion[0] * n, n


def test_convert_to_one_fraction():
    assert convert_to_one_fraction([2, 1, 2, 1, 1, 4]) == (87, 32)
    assert convert_to_one_fraction([2, 1, 2, 1, 1, 4, 1, 1, 6]) == (1264, 465)

    assert convert_to_one_fraction([1, 2, 2, 2]) == (17, 12)
    assert convert_to_one_fraction([1, 2, 2, 2, 2, 2, 2]) == (239, 169)


def get_convergents_of_e(n):
    yield 2
    i = 1
    while i < n:
        if (i - 2) % 3 == 0:
            yield (i + 2) / 3 * 2
        else:
            yield 1
        i += 1


def test_get_convergents_of_e():
    assert list(get_convergents_of_e(5)) == [2, 1, 2, 1, 1]
    assert list(get_convergents_of_e(1)) == [2]
    assert list(get_convergents_of_e(9)) == [2, 1, 2, 1, 1, 4, 1, 1, 6]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum([int(c) for c in str(convert_to_one_fraction(get_convergents_of_e(int(sys.argv[-1])))[0])])
