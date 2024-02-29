import sys
import pytest
import math
import numpy as np


class Fraction(object):
    _n = 1
    _d = 1

    def __init__(self, n):
        self._n = n
        self._d = 1

    def __div__(self, other):
        self._d *= other

    def __mul__(self, other):
        self._n *= other

    def __cmp__(self, other):
        return cmp(self._n, self._d * other)


def sieve_primes(maximum, primes=None):
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


def prime_counts_to_product(counts, primes):
    it = [primes[i] ** counts[i] for i in range(len(counts))]
    product = 1
    for i in it:
        product *= i
    return product


def find_optimal_primes(required_divisors, max_power, max_value, primes=None):
    i = 0
    best, minimum = [], max_value
    while (i <= max_power or max_power == -1) and primes[0] ** i <= max_value:
        if i == 0:
            opt = []
        else:
            opt = find_optimal_primes(required_divisors / (2.0 * i + 1), i, max_value / (primes[0] ** i), primes[1:])
        product = prime_counts_to_product([i] + opt, primes)
        if product <= minimum and np.prod([2 * n + 1 for n in [i] + opt]) >= required_divisors:
            best = [i] + opt
            minimum = product
        i += 1
    return best


def find_first_above(bound):
    prime_bound = int(math.log(bound * 2 - 1) / math.log(3)) + 1
    i = 1
    _, primes = sieve_primes(prime_bound * i)
    while len(primes) < prime_bound:
        i += 1
        _, primes = sieve_primes(prime_bound * i, primes)
    best = find_optimal_primes(bound * 2 - 1, -1,
                               prime_counts_to_product([1 for _ in range(prime_bound)], primes), primes)
    return prime_counts_to_product(best, primes), best


def test_find_first_above():
    assert find_first_above(100) == 1260


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_first_above(int(sys.argv[-1]))
