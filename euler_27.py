import sys
import pytest
from copy import copy


def generate_prime_table(maximum, prime_table=None):
    if prime_table is None:
        prime_table = []
        minimum = 2
    else:
        minimum = max(prime_table) + 1
    for n in range(minimum, maximum):
        prime = True
        for p in prime_table:
            if n % p == 0:
                prime = False
                break
        if prime:
            prime_table.append(n)
    return prime_table


def test_generate_prime_table():
    prime_table = generate_prime_table(12)
    assert prime_table == [2, 3, 5, 7, 11]
    assert generate_prime_table(15, prime_table) == [2, 3, 5, 7, 11, 13]


def get_value(a, b, n):
    return n * n + a * n + b


def find_best_coefficients(maximum):
    primes = generate_prime_table(maximum)
    prime_table = copy(primes)
    prime_max = maximum
    best = (0, 0, 0)
    for b in primes:
        for a in range(-b, maximum):
            n = 0
            while True:
                x = get_value(a, b, n)
                if x > prime_max:
                    prime_table = generate_prime_table(x + 1, prime_table)
                    prime_max = x + 1
                if x not in prime_table:
                    break
                n += 1
            if n > best[2]:
                best = (a, b, n)
    return best[0], best[1], best[2]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        c = find_best_coefficients(int(sys.argv[1]))
        print c[0] * c[1]