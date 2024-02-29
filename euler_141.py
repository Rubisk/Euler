import sys
import pytest
import math
import numpy as np


def brute_force(maximum):
    a = 1
    while a ** 4 <= maximum:
        b = a
        while a * (b ** 3 + 1) <= maximum:
            k = 1
            while k * a * (k * b ** 3 + a) <= maximum:
                if math.sqrt(k * a * (k * b ** 3 + a)).is_integer():
                    yield k * a * (k * b ** 3 + a)
                k += 1
            b += 1
        a += 1

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(np.unique(list(brute_force(int(sys.argv[1])))))
