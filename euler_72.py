import sys
import pytest
import numpy as np


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
    print "Sieving Complete!"
    return sieve, primes


class PhiCalculator(object):

    def __init__(self, maximum, primes):
        self.phis = np.zeros(maximum)
        self.primes = primes
        for p in primes:
            self.phis[p] = p - 1
            self.phis[1] = 1

    def get_phi(self, n):
        phi = 1
        mutable_n = n + 0
        if self.phis[n] != 0:
            return self.phis[n]
        for p in self.primes:
            if mutable_n % p == 0:
                phi *= (p - 1)
                mutable_n /= p
                while mutable_n % p == 0:
                    phi *= p
                    mutable_n /= p
            if self.phis[mutable_n] != 0:
                self.phis[n] = self.phis[mutable_n] * phi
                break
        assert self.phis[n] != 0
        return self.phis[n]


def custom_combinations(primes, maximum_product, factors=None):
    if factors is None:
        factors = []
    product = np.prod(factors)
    if product > 1:
        yield factors
    minimum = min(factors) if len(factors) > 0 else 0
    for p in primes:
        if p >= minimum:
            if p * product >= maximum_product:
                break
            for c in custom_combinations(primes, maximum_product, factors + [p]):
                yield c


def get_number_of_fractions(max_denominator):
    _, primes = sieve_primes(max_denominator + 1)
    phi_calc = PhiCalculator(max_denominator + 1, primes)
    phi_sum = 0
    for n in range(2, max_denominator + 1):
        phi_sum += phi_calc.get_phi(n)
    return int(phi_sum)


def test_custom_combinations():
    combinations = custom_combinations([2, 3, 5, 7], 9)
    assert sorted([np.prod(p) for p in combinations]) == [2, 3, 4, 5, 6, 7, 8]


def test_get_number_of_fractions():
    assert get_number_of_fractions(8) == 21
    assert get_number_of_fractions(9) == 27
    assert get_number_of_fractions(10) == 31

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_number_of_fractions(int(sys.argv[-1]))
