import sys
import pytest
import numpy as np
from copy import copy


def generate_prime_table(maximum):
    print "Generating prime table using sieve..."
    primes = []
    table = np.zeros(maximum)
    for n in range(2, maximum):
        if table[n] == 0:
            primes.append(n)
            table[::n] = 1
            table[n] = 0
    print "Prime table generated. Found %d primes." % len(primes)
    return table, primes


def circulate(n):
    if len(n) == 1:
        return n
    n = [x for x in str(n)]
    n, end = n[1:], n[0]
    n.append(end)
    return "".join(n)


def get_all_circulations(n):
    circulations = []
    for _ in range(len(str(n))):
        n = circulate(str(n))
        if n not in circulations:
            circulations.append(n)
    return [int(n) for n in circulations]


def get_all_circular_primes(maximum):
    table, primes = generate_prime_table(maximum)
    circulars = []
    for p in primes:
        if p in circulars:
            continue
        circular = True
        circulations = get_all_circulations(p)
        for c in circulations:
            if table[c] == 1:
                circular = False
                break
        if circular:
            for c in circulations:
                if c not in circulars:
                    circulars.append(c)
    return circulars


def test_get_all_circulations():
    assert [x for x in get_all_circulations(197)] == [971, 719, 197]


def test_get_all_circular_primes():
    assert len(get_all_circular_primes(100)) == 13
    assert 197 in get_all_circular_primes(1000)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        size = len(get_all_circular_primes(int(sys.argv[-1])))
        print "Found %i circular primes." % size
