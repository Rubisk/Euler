import math
import sys
import pytest


def get_divisors(n):
    divisors = []
    x = 1
    root = math.sqrt(n)
    while x <= root:
        if n % x == 0:
            divisors.append(x)
            if n / x not in divisors:
                divisors.append(n / x)
        x += 1
    return divisors


def get_triangle_number(divisors):
    x = 1
    n = 0
    d = 0
    m_d = 0
    while d < divisors:
        n += x
        x += 1
        d = len(get_divisors(n))
        if d > m_d:
            m_d = d
        print m_d
    return n


def test_get_divisors():
    assert len(get_divisors(1)) == 1
    assert len(get_divisors(28)) == 6


def test_get_triangle_number():
    assert get_triangle_number(5) == 28


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_triangle_number(int(sys.argv[-1]))
