import pytest
import sys
import numpy as np
import math


def power(number, powers):
    return np.sum(number for _ in range(powers))


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


def test_is_prime():
    assert is_prime(97)
    assert not is_prime(17 * 17)


def get_prime(n):
    count = 1  # 2 excluded
    prime_trial = 1
    while count < n:
        prime_trial += 2
        if is_prime(prime_trial):
            count += 1
    return prime_trial


def test_get_prime():
    assert get_prime(6) == 13

if __name__ == '__main__':
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_prime(int(sys.argv[-1]))
