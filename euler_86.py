"""
Yay for inefficiency. Misread the problem, decided to not redo all code
and just implement binary search. Still solves it in about 30 seconds :/
"""


import sys
import pytest
import math


def ggd(a, b):
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)


def brute_force_cuboids(maximum_length):
    print "Brute force:", maximum_length
    total = 0
    a = 1
    while a <= maximum_length:
        b = 1
        while b <= a:
            c = 1
            while c <= b:
                if math.sqrt((b + c) ** 2 + a ** 2).is_integer():
                    # print a, b, c
                    total += 1
                c += 1
            b += 1
        a += 1
    return total


def find_number_of_cuboids(maximum_length):
    print "LOOKING FOR:", maximum_length
    total = 0
    p = 1
    while p <= maximum_length:
        q = 1
        while q < p:
            if (p - q) % 2 == 0 or ggd(p, q) != 1:
                q += 1
                continue
            a = 2 * p * q
            b = p * p - q * q
            if not a > b:
                a, b = b, a
            if b > maximum_length:
                q += 1
                continue
            k = 1

            while k * b <= maximum_length:
                subtotal = 0
                subtotal += max((k * b - (k * a - k * b) + 2) / 2, 0)
                if not k * a > maximum_length:
                    subtotal += k * b / 2
                # print k * a, k * b, subtotal
                total += subtotal
                k += 1
            q += 1
        p += 1
    return total


def binary_search_number_of_cuboids(minimum):
    minimum_search = 0
    maximum_search = int(math.sqrt(minimum))
    while find_number_of_cuboids(maximum_search) < minimum:
        minimum_search = maximum_search
        maximum_search *= 2
    while minimum_search != maximum_search - 1:
        print minimum_search, maximum_search
        search = (minimum_search + maximum_search) / 2
        if find_number_of_cuboids(search) > minimum:
            maximum_search = search
        else:
            minimum_search = search
    return maximum_search


def test_find_number_of_cuboids():
    assert brute_force_cuboids(5) == 3
    assert find_number_of_cuboids(5) == 3
    assert find_number_of_cuboids(99) == 1975
    assert binary_search_number_of_cuboids(2000) == 100


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print binary_search_number_of_cuboids(int(sys.argv[-1]))
