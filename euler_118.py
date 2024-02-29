import sys
import pytest
import itertools as it
import math
import copy


def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        root = int(math.sqrt(n))
        divisor = 5
        while divisor <= root + 6:
            if n % divisor == 0:
                return False
            if n % (divisor + 2) == 0:
                return False
            divisor += 6
        return True


def find_prime_sets(digits, maximum=987654321, primes=None):
    if len(digits) == 0:
        yield []
        return
    if len(digits) == 1:
        if digits[0] in (2, 3, 5, 7) and digits[0] < maximum:
            yield [digits[0]]
        return
    if primes is None:
        primes = {}
    for i in range(1, len(digits) + 1):
        if maximum == 987654321:
            print i
        for perm in it.permutations(digits, i):
            if sum(perm) % 3 != 0 or perm == (3,):
                number = sum([perm[len(perm) - i - 1] * 10 ** i for i in range(len(perm))])
                if number > maximum:
                    continue
                if primes.get(number) is None:
                    primes[number] = is_prime(number)
                if primes[number]:
                    leftovers = copy.copy(digits)
                    for p in perm:
                        leftovers.remove(p)
                    for s in find_prime_sets(leftovers, number, primes):
                        yield s + [number]


if __name__ == "__main__":
    total = 0
    for s in find_prime_sets(range(1, 10)):
        total += 1
    print total