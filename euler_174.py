import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math

upper_bound = 1000000 
divisor_table = [1 for x in range(1, 10000001)]


for i in range(2, upper_bound + 1):
    j = 1
    while j * i - 1 <= upper_bound:
        divisor_table[j * i - 1] += 1
        j += 1
    if i % 1000 == 0:
        print(i)


def type(t):
    if t % 4 != 0:
        return 0
    t = int(t / 4)
    divisor_count = divisor_table[t - 1]
    if divisor_count % 2 == 1:
        divisor_count -= 1
    return divisor_count / 2

total = 0
for t in range(1, 1000000 + 1):
    if 1 <= type(t) <= 10:
        total += 1
print(total)
