"""
About prime factor objects:
For example, 12 would be given like:
[(2, 2), (3, 2)]
As
12 = 2 ^ 2 * 3 ^ 2
   = (2 * 2) * (3 * 3)
"""

# Using pytest for testing, just run pytest -m test
# to run all unit tests.
import pytest
import sys

from itertools import combinations
import numpy as np


def get_primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            x = 0
            while n % d == 0:
                x += 1
                n //= d
            primfac.append((d, x))
        d += 1
    if n > 1:
        primfac.append((n, 1))
    return primfac


def get_sum(max_value=1000000):
    total = 0
    # primes = []
    # prime_counter = []
    for x in range(100000, max_value):
        if x == 100000 + 1000:
            exit()
        if x == 1:
            total += 1
            continue
        primes = get_primes(x)
        if len(primes) >= 2:
            total += get_highest_idempotent(primes)
        else:
            total = 1
        # total += get_highest_slow(x)


def zero_pairs(prime_factors):
    """
    Let n be the product of the prime_factors.
    Returns all zero divisors for
    Z modulo n
    """
    prime_set = partitions(prime_factors)
    for prime_duo in prime_set:
        yield prime_duo


def partitions(target_set):
    """
    Generates all partitions of set
    with 2 elements.
    """
    for i in range(1, (len(target_set)) / 2 + 1):
        sets = combinations(target_set, i)
        for s in sets:
            yield (s, [p for p in target_set if p not in s])


def get_highest_idempotent(prime_factors):
    """
    Returns the highest idempotent element in
    Z modulo(product of prime_factors)
    """
    number = get_number(prime_factors)

    def get_top_idempotent(left, right):
        right_int = get_number(right)
        left_int = get_number(left)

        def find_difference_of_one():
            left_sum = left_int
            right_sum = right_int

            while left_sum - right_sum not in (-1, 1):
                if left_sum < right_sum:
                    left_sum += left_int
                else:
                    right_sum += right_int
            return left_sum, right_sum

        left_sum_, right_sum_ = find_difference_of_one()

        yield max(number - left_sum_, number - right_sum_)

    return np.max([get_top_idempotent(*p) for p in zero_pairs(prime_factors)])


def get_number(prime_factors):
    """
    Returns the number corresponding to the prime factors.
    """
    return np.prod([np.prod([p[0] for _ in range(p[1])]) for p in prime_factors])


def test_zero_pairs():
    test_tuples = [(2, 2), (3, 2), (5, 1), (7, 1)]
    x = 0
    for z in zero_pairs(test_tuples):
        assert get_number(test_tuples) == get_number(z[0]) * get_number(z[1])
        x += 1
    assert x == 10

    test_tuples = [(2, 5), (3, 1)]
    x = 0
    for z in zero_pairs(test_tuples):
        assert get_number(z[0]) * get_number(z[1]) == 32 * 3
        x += 1
    assert x == 2


def get_highest_slow(modulo):
    for a in range(1, modulo):
        current_test = modulo - a
        if (current_test * current_test) % modulo == current_test:
            return current_test
    return 1


def test_get_highest_idempotent():
    test_tuples = [(2, 2), (3, 2), (5, 1), (7, 1)]
    assert get_highest_idempotent(test_tuples) == get_highest_slow(get_number(test_tuples))


if __name__ == "__main__":
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_sum()
