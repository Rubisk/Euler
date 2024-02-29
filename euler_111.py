import math
import sys
import pytest
import itertools as it


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    root = math.sqrt(n)
    j = 6
    while j < root:
        if n % (j - 1) == 0 or n % (j + 1) == 0:
            return False
        j += 6
    return True


def find_all_sums(digits):
    total = 0
    for d in range(10):
        found = False
        base = sum([d * 10 ** i for i in range(digits)])
        i = 0
        while not found:
            i += 1
            for spot_comb in it.combinations(range(digits), i):
                for replace_comb in it.product(range(10), repeat=i):
                    n = base + sum([(r - d) * 10 ** s for s, r in zip(spot_comb, replace_comb)])
                    if is_prime(n) and n > 10 ** (digits - 1):
                        found = True
                        total += n
    return total

def test_find_all_sums():
    assert find_all_sums(4) == 273700


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_all_sums(int(sys.argv[-1]))
