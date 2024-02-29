import sys
import pytest
import math
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


def find_biggest_pandigital_prime():
    for n in reversed(range(1, 10)):
        if sum(range(1, n)) % 3 == 0:
            continue
        for p in it.permutations("".join(str(x) for x in reversed(range(1, n)))):
            if is_prime(int("".join(p))):
                return "".join(p)


def test_is_prime():
    assert is_prime(137)
    assert is_prime(97)
    assert is_prime(2)
    assert is_prime(104729)
    assert not is_prime(51)
    assert not is_prime(49)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_biggest_pandigital_prime()