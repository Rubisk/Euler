import sys
import pytest
import numpy as np


def ggd(a, b):
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)


def find_number_of_triples(limit):
    array = np.zeros(limit + 1)
    p = 1
    while p <= limit:
        # print "P", p
        # if n % (limit / 100) == 0:
        #     print n
        q = 1
        while q < p and 2 * p * (p + q) <= limit:
            # print q
            if (p - q) % 2 == 0 or ggd(p, q) != 1:
                q += 1
                continue
            length = 2 * p * (p + q)
            array[::length] += 1
            q += 1
        p += 1
    return len(np.where(array == 1)[0])


def test_find_number_of_triples():
    assert find_number_of_triples(150) == 16

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        try:
            print find_number_of_triples(int(sys.argv[-1]))
        except ValueError:
            print "Script invocation: [L]"
            print "[L]: Limit to search to (integer)."



