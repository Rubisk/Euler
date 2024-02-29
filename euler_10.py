import pytest
import sys
import numpy as np


def power(number, powers):
    return np.sum(number for _ in range(powers))


def get_all_primes(maximum):
    prime_array = np.zeros(maximum + 1)
    current_prime = 2
    while current_prime < maximum:
        yield current_prime
        prime_array[::current_prime] = 1
        while prime_array[current_prime] == 1 and current_prime < maximum:
            current_prime += 1


def test_get_all_primes():
    assert len([x for x in get_all_primes(14)]) == 6


def test_get_prime_sum():
    assert get_prime_sum(10) == 17


def get_prime_sum(maximum):
    return sum(get_all_primes(maximum))


if __name__ == '__main__':
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_prime_sum(int(sys.argv[-1]))
