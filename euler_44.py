import sys
import pytest
import itertools as it
import math


def abs(n):
    return n if n >= 0 else -n


def is_pentagon(n):
    m = (math.sqrt(24 * n + 1) + 1.0) / 6.0
    return m == int(m)


def find_all():
    pentagons = [n * (3 * n - 1) / 2 for n in range(1, 3000)]
    differences = [(a, b, abs(a - b)) for (a, b) in it.combinations(pentagons, 2) if is_pentagon(abs(a - b))]
    return [d for d in differences if is_pentagon(d[0] + d[1])]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_all()