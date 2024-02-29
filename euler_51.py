import sys
import pytest
import numpy as np
import itertools as it


def extended_combinations(iterable):
    for n in range(1, len(iterable) + 1):
        for c in it.combinations(iterable, n):
            yield c


def get_primes_and_table(maximum):
    sieve = np.zeros(maximum)
    for i in range(2, maximum):
        if sieve[i] == 0:
            sieve[::i] = 1
            sieve[i] = 0
    primes = np.where(sieve == 0)[0][1:]
    return primes, sieve


def find_first_family(size):
    prime_size = 2
    while True:
        primes, sieve = get_primes_and_table(10 ** prime_size)
        iterprimes = [p for p in primes if p > 10 ** (prime_size - 1)]
        for p in iterprimes:
            to_remove = [p]
            string = str(p)
            for n in "0123456789":
                indices = [i for i, x in enumerate(string) if x == n]
                if prime_size - 1 in indices:
                    indices.remove(prime_size - 1)
                for c in extended_combinations(indices):
                    family = [p]
                    chars = [x for x in "0123456789"]
                    chars.remove(n)
                    if 0 in indices and n != "0":
                        chars.remove("0")
                    for char in chars:
                        new_prime = [s for s in string]
                        for index in c:
                            new_prime[index] = char
                        new_prime = int("".join(new_prime))
                        if sieve[new_prime] == 0:
                            family.append(new_prime)
                    if len(family) >= size:
                        return sorted(family)[0]
                    to_remove.extend(family)
        prime_size += 1


def test_find_first_family():
    assert find_first_family(6) == 13
    assert find_first_family(7) == 56003


if __name__ == "__main__":
    test_find_first_family()
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_first_family(int(sys.argv[-1]))
