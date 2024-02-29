import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math


def odd_numbers_in_interval(lower, upper):
    if lower > upper:
        return 0
    lower = math.ceil(lower)
    upper = math.floor(upper)
    if lower % 2 == 1:
        lower -= 1
    if upper % 2 == 1:
        upper += 1
    return int((upper - lower) / 2)



def even_numbers_in_interval(lower, upper):
    if lower > upper:
        return 0
    lower = math.ceil(lower)
    upper = math.floor(upper)
    if lower % 2 == 0:
        lower -= 1
    if upper % 2 == 0:
        upper += 1
    return int((upper - lower) / 2)



def count_laminae(upper_bound):
    total = 0
    for a in range(1, int(upper_bound / 2) + 2):
        lower = 1 if a ** 2 < upper_bound else max(math.ceil(math.sqrt(a ** 2 - upper_bound)), 1)
        if a % 2 == 0:
            total += even_numbers_in_interval(lower, a - 1)
        else:
            total += odd_numbers_in_interval(lower, a - 1)
    return total

print(count_laminae(1000000))