import numpy as np
import sys
import pytest
from euler_21 import find_ami
from itertools import combinations


def is_abundant(n):
    if n < find_ami(n):
        return True
    return False


def generate_abundant_table(maximum):
    return [1 if is_abundant(n) else 0 for n in range(maximum)]


def custom_combinations(maximum, input_values):
    for i in input_values:
        print i
        j = 0
        while i + input_values[j] < maximum:
            yield i, j
            j += 1


def generate_sum(maximum, abundants):
    total = 0
    for n in range(maximum):
        i = 0
        abundant_sum = False
        while i < n:
            while i < n and abundants[i] != 1:
                i += 1
            if abundants[n - i] == 1:
                abundant_sum = True
                break
            i += 1
        if not abundant_sum:
            print n
            total += n
    return total


def get_sum_of_non_abundants(maximum):
    abundants = generate_abundant_table(maximum)
    return generate_sum(maximum, abundants)


def test_generate_abundant_table():
    for i in range(12):
        assert not is_abundant(i)
    assert is_abundant(12)
    assert (generate_abundant_table(11) == np.zeros(11)).all()
    assert sum(generate_abundant_table(13)) == 1


def test_generate_sum_table():
    assert get_sum_of_non_abundants(6) == 15
    assert get_sum_of_non_abundants(25) == 276


if __name__ == "__main__":
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_sum_of_non_abundants(int(sys.argv[1]))
