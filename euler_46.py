import sys
import pytest
import math


class GoldbachInvalidator(object):
    _prime_cache = {}
    _square_cache = []

    def is_prime(self, n):
        if self._prime_cache.get(n) is None:
            self._prime_cache[n] = self._is_prime(n)
        return self._prime_cache[n][0]

    @staticmethod
    def _is_prime(n):
        if n < 2:
            return False, False
        if n in (2, 3):
            return True, False
        if n % 2 == 0 or n % 3 == 0:
            return False, True
        root = math.sqrt(n)
        j = 6
        while j - 1 <= root:
            if n % (j - 1) == 0:
                return False, True
            if n % (j + 1) == 0:
                return False, True
            j += 6
        return True, False

    def is_composite(self, n):
        if self._prime_cache.get(n) is None:
            self._prime_cache[n] = self._is_prime(n)
        return self._prime_cache[n][1]

    def get_square(self, n):
        while len(self._square_cache) < n:
            m = len(self._square_cache) + 1
            self._square_cache.append(m * m)
        return self._square_cache[n - 1]


def get_smalles_invalid_goldbach():
    invalidator = GoldbachInvalidator()
    n = 5
    while True:
        if invalidator.is_composite(n):
            square = 1
            s = 1
            check = True
            while n - 2 * square > 0:
                square = invalidator.get_square(s)
                if invalidator.is_prime(n - 2 * square):
                    check = False
                    break
                s += 1
            if check:
                return n
        n += 2


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_smalles_invalid_goldbach()