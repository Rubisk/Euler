import math
import numpy as np
import sys
import pytest


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


def find_prime_sums(maximum):
    found = {}
    total = 0
    root = int(math.sqrt(maximum))
    _, primes = sieve_primes(root)
    fourth_root = math.sqrt(root)
    m = 0
    while primes[m] < fourth_root:
        second_maximum = maximum - primes[m] ** 4
        second_root = second_maximum ** (1 / 3.0)
        i = 0
        while primes[i] < second_root:
            third_maximum = second_maximum - primes[i] ** 3
            third_root = math.sqrt(third_maximum)
            j = 0
            while j < len(primes) and primes[j] < third_root:
                n = maximum - (third_maximum - primes[j] ** 2)
                if found.get(n) is None:
                    found[n] = 1
                    total += 1
                # if not found[n]:
                #     found[n] = True
                j += 1
            i += 1
        m += 1
    return total


def test_find_prime_sums():
    assert find_prime_sums(50) == 4

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_prime_sums(int(sys.argv[-1]))
