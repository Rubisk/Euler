import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math

test = 0
squares = [n ** 2 for n in range(1, int(math.sqrt(30 * 9 ** 2)))]


def faculty(n):
    if n == 0:
        return 1
    return n * faculty(n - 1)

faculties = [faculty(n) for n in range(21)]


def multinomial(sequence):
    n = sum(sequence)

    denom = 1
    for x in sequence:
        denom *= faculties[x]
    result = int(faculties[n] / denom)
    assert result * denom == faculties[n]

    return result


def find_combinations(max_appearance, numbers, length):
    if max_appearance * len(numbers) < length:
        return

    elif len(numbers) == 1:
        assert numbers == [0]
        assert length <= max_appearance
        yield [length]
        return
    

    for x in range(max_appearance + 1):
        if x > length:
            continue
        for combination in find_combinations(max_appearance, numbers[1:], length - x):
            yield [x] + combination


def count_numbers(combination):
    mult = multinomial(combination)
    if combination[9] > 0:
        a2 = combination[9]
        mult -= a2 * mult / sum(combination)
    return int(mult)



total = 0
for combination in find_combinations(3, list(range(10))[::-1], 18):
    total += count_numbers(combination)
print(total)
