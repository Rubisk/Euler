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


def find_divisor_sums(maximum):
    _, primes = sieve_primes(maximum)
    divisor_sums = np.ones(maximum)

    for p in primes:
        n = 1
        while p ** n < maximum:
            if n > 1:
                divisor_sums[::p ** n] /= (p ** n - 1) / (p - 1)
            divisor_sums[::p ** n] *= (p ** (n + 1) - 1) / (p - 1)
            n += 1

    divisor_sums -= range(maximum)
    return divisor_sums


def find_longest_chain(numbers, maximum):
    numbers = [int(n) if (n != np.inf and n < maximum) else -1 for n in numbers]
    enum = list(enumerate(numbers))

    longest_chain = []
    for number, divisors in enum[1:]:
        if number is None:
            continue
        # print number, divisors

        chain = [number, divisors]
        while numbers[chain[-1]] != -1 and numbers[chain[-1]] not in chain:
            enum[chain[-1]] = (None, None)
            chain.append(numbers[chain[-1]])

        if numbers[chain[-1]] != -1:
            chain = chain[chain.index(numbers[chain[-1]]):]
            if len(chain) > 1 and chain[1] == chain[0]:
                chain = chain[1:]
            if len(chain) > len(longest_chain):
                longest_chain = chain

    return longest_chain


def test_find_divisor_sums():
    assert find_divisor_sums(40)[28] == 28
    assert find_divisor_sums(40)[12] == 16


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        m = int(sys.argv[-1])
        print min(find_longest_chain(find_divisor_sums(m), m))
