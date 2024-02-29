import sys
import pytest
import numpy as np
import bisect


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
    return primes


def get_one_solutions(m):
    candidates = [1] + sieve_primes(m)
    last_4 = bisect.bisect_left(candidates, m / 4) - 1
    last_16 = bisect.bisect_left(candidates, m / 16) - 1
    return len([x for x in candidates if x % 4 == 3]) + len(candidates[:last_4]) + len(candidates[:last_16])

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_one_solutions(int(sys.argv[1]))
