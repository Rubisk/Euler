import sys
import pytest
import itertools
import numpy

def get_all_fractions(digits):
    for x in range(10 ** digits):
        for y in range(10 ** digits):
            return x, y


def get_all_curious_fractions():
    for x in range(1, 10):
        for p, q in itertools.combinations(range(10), 2):
            p = float(p)
            q = float(q)
            x = float(x)
            for p_q in ((x * 10 + p) / (q + x * 10),
                        (x * 10 + p) / (q * 10 + x),
                        (x + p * 10) / (q + x * 10),
                        (x + p * 10) / (q * 10 + x)):
                if p / q == p_q:
                    yield p_q


def test_get_all_curious_fractions():
    fractions = [f for f in get_all_curious_fractions()]
    assert 49.0/98.0 in fractions
    assert len(fractions) == 4


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print numpy.prod([x for x in get_all_curious_fractions()])