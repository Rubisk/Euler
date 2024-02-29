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


class SmallestSumFinder(object):

    _cache = {}
    _primes = None

    def find_smallest_with_sums(self, target_sum):
        _, self._primes = sieve_primes(target_sum * 2, self._primes)
        n = 1
        while self.get_number_of_sums(n) < target_sum:
            n += 1
        return n

    def get_number_of_sums(self, n, max_prime=-1):
        if n == 0:
            return 1
        elif n == 1:
            return 0
        else:
            if self._cache.get(n) is None:
                self._cache[n] = {}
            if self._cache[n].get(max_prime) is None:
                self._cache[n][max_prime] = self._calculate_number_of_sums(n, max_prime)
        return self._cache[n][max_prime]

    def _calculate_number_of_sums(self, n, max_prime=-1):
        p = -1
        total = 0
        if max_prime == -1:
            max_prime = n
        while p + 1 < len(self._primes) and self._primes[p + 1] <= min(max_prime, n):
            p += 1
            total += self.get_number_of_sums(n - self._primes[p], self._primes[p])
        return total


def test_find_smallest_with_prime_sums():
    f = SmallestSumFinder()
    assert f.find_smallest_with_sums(5) == 10


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        try:
            finder = SmallestSumFinder()
            print finder.find_smallest_with_sums(int(sys.argv[-1]))
        except ValueError:
            print "Script invocation: [N]"
            print "[N]: Lower limit for number of prime summations (integer)."
