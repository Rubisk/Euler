import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math


def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            rv = function(*args)
            memo[args] = rv
            if len(memo) % 1000 == 0:
                print(len(memo))
            return rv
    return wrapper

@memoize
def count_sums(n, max_2_power=-1):
    if max_2_power == 0:
        return 1 if n in (0, 1, 2) else 0
    if max_2_power == -1:
        max_2_power = int(math.log(n) / math.log(2))
    if 2 ** max_2_power * 4 <= n:
        return 0
    total = 0
    if n < 4 * 2 ** (max_2_power - 1):
        total += count_sums(n, max_2_power - 1) 
    if n - 2 ** max_2_power >= 0:
        total += count_sums(n - 2 ** max_2_power, max_2_power - 1) 
    if n - 2 * 2 ** max_2_power >= 0:
        total += count_sums(n - 2 * 2 ** max_2_power, max_2_power - 1) 
    return total


print(count_sums(10 ** 25))