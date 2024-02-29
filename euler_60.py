import sys
import pytest
import numpy as np
import math
import itertools as it


def sieve_primes(maximum, primes=None):
    print "Sieving up to %i" % maximum
    sieve = np.zeros(maximum)
    sieve[1] = 1
    if primes is None:
        primes = [2]
        sieve[::2] = 1
        sieve[2] = 0
    else:
        for p in primes:
            sieve[::p] = 1
            sieve[p] = 0
    for i in range(primes[-1] + 1, maximum):
        if sieve[i] == 0:
            sieve[::i] = 1
            sieve[i] = 0
            primes.append(i)
    return sieve, primes


def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 6
    while j < math.sqrt(n) + 6:
        if n % (j - 1) == 0 or n % (j + 1) == 0:
            return False
        j += 6
    return True


def form_pair(left, right, sieve, primes):
    l = int(str(left) + str(right))
    r = int(str(right) + str(left))
    m = max(l, r, max(primes)) + 1
    if m > len(sieve):
        m /= 10000
        m += 1
        m *= 10000
        sieve, primes = sieve_primes(m, primes)
    return sieve, primes, sieve[l] == 0 and sieve[r] == 0


def test_sieve_primes():
    sieve, primes = sieve_primes(10)
    assert primes == [2, 3, 5, 7]
    _, primes = sieve_primes(20, primes)
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19]


def forms_clique(pairs, clique):
    for c in clique:
        for d in clique:
            if d == c:
                continue
            if c not in pairs[d]:
                return False
    return True


def find_clique_of_size(pairs, minimum, size):
    for key in pairs.keys():
        if key <= minimum:
            continue
        for clique in it.combinations(pairs[key], size - 1):
            if forms_clique(pairs, clique):
                clique = sorted([key] + [c for c in clique])
                return clique


def find_set_of_prime_pairs(number):
    pairs = {}
    n = 1
    checked_primes = []
    primes = None
    power = 0
    while True:
        print 1000 * n
        sieve, primes = sieve_primes(1000 * n, primes)
        for p in primes:
            if p <= power:
                continue
            for key in checked_primes:
                sieve, primes, pair = form_pair(p, key, sieve, primes)
                if pair:
                    if pairs.get(key) is None:
                        pairs[key] = []
                    pairs[key].append(p)
                    if pairs.get(p) is None:
                        pairs[p] = []
                    pairs[p].append(key)
            checked_primes.append(p)
        c = find_clique_of_size(pairs, power, number)
        if c is not None:
            return c
        power = 1000 * n
        n += 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_set_of_prime_pairs(int(sys.argv[-1]))