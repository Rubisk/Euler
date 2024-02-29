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


def find_all_phis(maximum):
    _, primes = sieve_primes(maximum / 2)
    best = (-1, 1000)
    for p1 in reversed(primes):
        for p2 in primes:
            if p2 == p1:
                continue
            if p2 * p1 > maximum:
                break
            n, phi = p2*p1, (p2 - 1) * (p1 - 1)
            if sorted(str(phi)) == sorted(str(n)):
                if n / float(phi) < best[1]:
                    best = n, n / float(phi)
    return best

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_all_phis(10000000)
