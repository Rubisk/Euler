import numpy as np
import sys
import pytest
from euler_12 import get_divisors


def find_ami(n):
    d = get_divisors(n)
    if n in d:
        d.remove(n)
    return sum(d)


def get_amicable_numbers(maximum):
    numbers = np.zeros(maximum)
    n = 3
    amicable_numbers = []
    while n < maximum:
        ami = numbers[n] = find_ami(n)
        if ami in amicable_numbers:
            n += 1
            continue
        if ami < maximum:
            if numbers[ami] == 0:
                numbers[ami] = find_ami(ami)
            if numbers[ami] == n and n != ami:
                amicable_numbers.extend([n, ami])
        n += 1
    return amicable_numbers


def test_get_amicable_numbers():
    assert 284 in get_amicable_numbers(300)
    assert 220 in get_amicable_numbers(300)
    assert 1 not in get_amicable_numbers(100)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(get_amicable_numbers(int(sys.argv[-1])))