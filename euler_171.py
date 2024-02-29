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


def find_combinations(number_count, numbers, higher_sum=0):
    if numbers == [2, 1, 0]:
        for square in squares:
            x = square - higher_sum
            if 0 <= x <= 4 * number_count:
                for i in range(number_count + 1):
                    if 0 <= square - (higher_sum + 4 * i) <= number_count - i:
                        a = i
                        b = square - (higher_sum + 4 * i)
                        c = number_count - a - b
                        assert a + b + c == number_count
                        assert 4 * a + b + higher_sum == square
                        yield [a, b, c]
        return
    

    for x in range(number_count + 1):
        for combination in find_combinations(number_count - x, numbers[1:], higher_sum + x * (numbers[0] ** 2)):
            yield [x] + combination


def count_digits(combination, digit, spot, mult, n):
    if sum(combination) != spot + 1:
        a1 = combination[9 - digit]
        mult = a1 * mult / n
        if combination[9] - (1 if digit == 0 else 0) > 0:
            a2 = combination[9] - (1 if digit == 0 else 0)
            mult -= a2 * mult / (n - 1)
        return int(mult)
    else:
        if digit == 0:
            return 0
        return int(mult / n * (combination[9 - digit]))


def sum_numbers(digits):
    total = 0
    combinations = list(find_combinations(digits, list(range(10)[::-1])))
    print("Found {0} combinations.".format(len(combinations)))
    progress = 0
    for combination in combinations:
        progress +=1 
        old_total = total + 0
        mult = multinomial(combination)
        n = sum(combination)
        for d in range(1, 10):
            if combination[9 - d] == 0:
                continue
            for i in range(sum(combination)):
                count = count_digits(combination, d, i, mult, n)
                total += count * (d * 10 ** i)
        if progress % 1000 == 0:
            print("Evaluated {0} combinations.".format(progress))
    return total


total = 0
for n in range(1, 21):
    print("Looking for numbers with {0} digits".format(n))
    total += sum_numbers(n)
    print(total)