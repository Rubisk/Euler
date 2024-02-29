import sys
import pytest
import numpy as np


def faculty(n):
    if n in (0, 1):
        return 1
    return n * faculty(n - 1)


CHAIN_NUMBERS = [169, 363601, 1454, 871, 872, 45361, 45362]


def find_chains_with_length(maximum, length):
    factorials = [faculty(n) for n in range(10)]
    chain_lengths = np.zeros(maximum + 1)
    for n in range(3, int(maximum) + 1):
        m = n + 0
        chain = [n]
        while m not in chain[:-1] and (m > maximum or chain_lengths[m] == 0):
            m = sum([factorials[int(d)] for d in str(m)])
            chain.append(m)
        chain_lengths[n] = (chain_lengths[m] if m < maximum else 0) + len(chain) - 1
        if chain_lengths[n] == length:
            yield n


def test_find_chains_with_length():
    assert 145 in list(find_chains_with_length(150, 1))
    assert 69 in list(find_chains_with_length(100, 5))
    assert 145 not in find_chains_with_length(150, 5)

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print len(list(find_chains_with_length(*[int(x) for x in sys.argv[-2:]])))
