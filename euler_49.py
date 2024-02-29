import sys
import pytest
import numpy as np
import itertools as it


def find_prime_permutations():
    sieve = np.zeros(10000)
    for s in range(2, 10000):
        if sieve[s] == 0:
            sieve[::s] = 1
            sieve[s] = 0
    primes = np.where(sieve == 0)[0]
    primes = [x for x in primes if x > 999]
    prime_digits = {}
    for p in primes:
        string = "".join(sorted(str(p)))
        if prime_digits.get(string) is None:
            prime_digits[string] = []
        prime_digits[string].append(p)
    for permutations in prime_digits.values():
        for perm in it.combinations(permutations, 3):
            perm = sorted(perm)
            if perm[2] - perm[1] == perm[1] - perm[0]:
                print perm


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        find_prime_permutations()