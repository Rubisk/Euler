import numpy as np
import math
import pytest

def faculty(n):
    assert type(n) == int and n >= 0
    if n == 0:
        return 1
    return n * faculty(n - 1)


def choose(n, k):
    return faculty(n) / faculty(k) / faculty(n - k)


def sieve_primes(maximum, primes=None):
    print("Sieving up to %i" % maximum)
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
        if i % 1000000 == 0:
            print(i)
        if sieve[i] == 0:
            sieve[::i] = 1
            sieve[i] = 0
            primes.append(i)
    print("Sieving Complete!")
    return sieve, primes

def is_prime_slow(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def is_prime(n, sieved_primes=[]):
    # TODO change this out with aks
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    for prime in sieved_primes:
        if n <= prime:
            return True
        if n % prime == 0:
            return False
    root = int(math.sqrt(n))
    divisor = max([5] + sieved_primes)
    divisor = divisor - (divisor % 6) - 1
    while divisor <= root + 6:
        if n % divisor == 0:
            return False
        if n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def all_prime(numbers_to_test, sieved_primes=[]):
    if any([x <= 1 for x in numbers_to_test]):
        return False
    for prime in sieved_primes:
        to_remove = []
        for n in numbers_to_test:
            if n < prime * prime:
                to_remove.append(n)
            elif n % prime == 0:
                return False
        for n in to_remove:
            numbers_to_test.remove(n)
        if len(numbers_to_test) == 0:
            return True

    start = 2 if sieved_primes == [] else max(sieved_primes)
    end = max(map(lambda x: int(math.sqrt(x) + 1), numbers_to_test))
    for divisor in range(start, end + 1):
        to_remove = []
        for n in numbers_to_test:
            if n < divisor * divisor:
                to_remove.append(n)
            elif n % divisor == 0:
                return False
        for n in to_remove:
            numbers_to_test.remove(n)
        if len(numbers_to_test) == 0:
            return True


def test_is_prime_with_sieve():
    _, sieved_primes = sieve_primes(1000000)
    primes = []
    for n in range(100000000, 101000000):
        if is_prime(n):
            primes.append(n, sieved_primes)


def test_all_prime_with_sieve():
    _, sieved_primes = sieve_primes(1000000)
    assert all_prime([2, 3, 5, 7, 11, 13, 17, 19], sieved_primes)
    assert all_prime([2, 3, 13, 17, 19], sieved_primes)
    assert not all_prime([2, 4, 13, 17, 19], sieved_primes)
    assert not all_prime([2, 3, 5, 7, 11, 13, 17, 19, 100], sieved_primes)
    assert not all_prime([1, 4], sieved_primes)


def test_is_prime_without_sieve():
    primes = []
    for n in range(100000000, 101000000):
        if is_prime(n):
            primes.append(n)


def test_all_prime_without_sieve():
    assert all_prime([2, 3, 5, 7, 11, 13, 17, 19])
    assert all_prime([2, 3, 13, 17, 19])
    assert not all_prime([2, 4, 13, 17, 19])
    assert not all_prime([2, 3, 5, 7, 11, 13, 17, 19, 100])
    assert not all_prime([1, 4])

def slow_factor(n):
    factors = []
    for i in range(2, int(n ** 0.5 + 1)):
        while (n % i) == 0:
            n /= i
            factors.append(i)
    if n != 1:
        factors.append(int(n))
    return factors