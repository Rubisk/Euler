import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a

    return gcd(b, a % b)


def bruteforce_square_count(target):
    count = 0
    for a in range(1, 5 * target ** 2 + 2):
        if math.sqrt(target ** 2 + a ** 2).is_integer():
            count += 1
    return count


def square_count_with_factor(target):
    factors = slow_factor(target)
    product = 1
    for (factor, exp) in factors.items():
        if factor != 2:
            product *= 2 * exp + 1

    return ((2 * factors.get(2, 1) - 1) * product - 1) / 2



def find_odd_products(target):
    assert target % 2 == 1
    if target == 1:
        yield []
        return
    for x in range(2, target + 1):
        if target % x == 0:
            for y in find_odd_products(int(target / x)):
                yield [x] + y


a = list(find_odd_products(95095))[0][::-1]
print(a)
t = 2 ** ((a[0] + 1) / 2)
for (x, y) in zip(a[1:], [3, 5, 7, 11]):
    t *= y ** ((x - 1) / 2)
print(t)