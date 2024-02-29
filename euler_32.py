import sys
import pytest
import itertools
import numpy


def extended_permutations(it, n):
    for i in range(n):
        for c in itertools.permutations(it, i + 1):
            yield c


def is_pandigital(n):
    n = str(n)
    for d in range(len(n)):
        if not str(int(d) + 1) in n:
            return False
    return True


def test_pandigital():
    assert is_pandigital(2314)
    assert not is_pandigital(11234)


def get_all_pandigitals(string, digits):
    for x in extended_permutations(string, digits):
        yield int("".join(x))


def get_all_pandigital_pairs():
    pandigitals = []
    string = "123456789"
    for d in get_all_pandigitals(string, 4):
        digits = len(str(d))
        digits_other = 5 - digits
        second_string = [s for s in "123456789" if s not in str(d)]
        for d_other in get_all_pandigitals(second_string, digits_other):
            product = d_other * d
            together = str(d_other) + str(d) + str(product)
            if is_pandigital(together) and len(together) == 9 and product not in pandigitals:
                pandigitals.append(product)
    return pandigitals


def test_get_all_pandigitals():
    assert 2314 in [x for x in get_all_pandigitals("123456789", 4)]


def test_get_all_pandigital_pairs():
    assert 7254 in get_all_pandigital_pairs()


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(get_all_pandigital_pairs())
