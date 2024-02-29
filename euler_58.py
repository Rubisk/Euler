import sys
import pytest
import math


def get_diagonals(n):
    n = (2 * n + 1)
    square = n * n
    inner_square = (n - 2) * (n - 2)
    for i in reversed(range(4)):
        yield square - ((square - inner_square) / 4.0 * i)


def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 6
    while j < math.sqrt(n) + 6:
        if n % (j - 1) == 0 or n % (j + 1) == 0:
            return False
        j += 6
    return True


def test_get_diagonals():
    assert [x for x in get_diagonals(1)] == [3, 5, 7, 9]
    assert [x for x in get_diagonals(2)] == [13, 17, 21, 25]


def test_is_prime():
    assert is_prime(17)
    assert is_prime(137)
    assert not is_prime(49)
    assert not is_prime(25)
    assert is_prime(43)
    assert is_prime(53)


def find_first_below_ratio(ratio):
    primes_len = [3, 5, 7]
    diagonals = 5.0
    n = 1
    while len(primes) / diagonals > ratio:
        print len(primes) / diagonals
        diagonals += 4
        n += 1
        possible_primes = get_diagonals(n)
        for p in possible_primes:
            if is_prime(p):
                primes.append(p)
    return int(diagonals / 4) * 2 + 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_first_below_ratio(float(sys.argv[-1]))