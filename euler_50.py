import sys
import pytest
import numpy as np


def get_primes_and_table(maximum):
    sieve = np.zeros(maximum)
    for i in range(2, maximum):
        if sieve[i] == 0:
            sieve[::i] = 1
            sieve[i] = 0
    primes = np.where(sieve == 0)[0][1:]
    return primes, sieve


def find_longest_consecutive_prime_sum(maximum):
    primes, sieve = get_primes_and_table(maximum)
    length = 2
    longest = (2, 5)
    while True:
        total = sum([primes[p] for p in range(length)])
        if total > maximum:
            break
        i = length - 1
        while total < maximum:
            if sieve[total] == 0:
                longest = (length, total)
            total -= primes[i - length + 1]
            total += primes[i + 1]
            i += 1
        length += 1
    return longest[1]


def test_find_longest_consecutive_prime_sum():
    assert find_longest_consecutive_prime_sum(100) == 41
    assert find_longest_consecutive_prime_sum(1000) == 953


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_longest_consecutive_prime_sum(int(sys.argv[-1]))
