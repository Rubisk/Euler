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
            return rv
    return wrapper

# 
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

def count_sums_new(length_array):
    if len(length_array) == 0:
        return 1
    count = 0
    count += (length_array[0] + 1) * count_sums_new(length_array[1:])
    new_length_array = length_array[1:]

    if len(new_length_array) > 0:
        new_length_array[0] -= 1
        count += count_sums_new(new_length_array)
    return count

@memoize
def count_sums_again(bin_exp):
    bin_exp = list(bin_exp)
    if len(bin_exp) <= 1:
        return 1
    count = 0
    count += (bin_exp[0] * bin_exp[1] + 1) * count_sums_again(tuple(bin_exp[2:]))
    if len(bin_exp) > 3:
        count += bin_exp[0] * count_sums_again(tuple([1, bin_exp[3] - 1] + bin_exp[4:]))
    return count


def short_bin_exp(n):
    lengths = [len(t) for t in str(bin(n))[2:].split("1")][1:]

    exp = []
    c = 1
    for x in lengths:
        if x == 0:
            c += 1
        else:
            exp.append(c)
            exp.append(x)
            c = 1
    # if lengths[-1] > 0:
    #     exp.append(0)
    return exp


# for (a, b, c, d) in it.product(range(1, 10), repeat=4):
#     string = "".join(["1" for _ in range(a)] + ["0" for _ in range(b)])
#     string += "".join(["1" for _ in range(c)] + ["0" for _ in range(d)])
#     n = int(string, 2)
#     print(a, b, c, d, string, count_sums(n), a * b * c * d + a * b + c * d + 1,  count_sums(n) - (a * b * c * d + a * (b + d) + c * d + 1))

results = set()

m = 0
for x in it.product(range(16), repeat=6):
    if x[-1] == 0:
        continue
    if count_sums_again(x) > m:
        m = count_sums_again(x)
        print(x, m)
