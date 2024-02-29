import sys
import pytest
import numpy as np


def get_all_numbers():
    sieve = np.zeros(1000000)
    for p in range(2, len(sieve)):
        if sieve[p] == 0:
            sieve[::p] += 1
    p = 2
    while p < len(sieve):
        if sieve[p] == 4 and sieve[p + 1] == 4 and sieve[p + 2] == 4 and sieve[p + 3] == 4:
            print p
            break
        p += 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        get_all_numbers()