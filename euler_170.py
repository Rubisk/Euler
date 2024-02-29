import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections
from functools import wraps
import math

def compatible(str1, str2):
    for x in str1:
        if x in str2:
            return False
    return True

def no_double_digits(number_string):
    for (x, y) in it.combinations(number_string, 2):
        if x == y:
            return False
    return True


def generate_uniques(multiplier):
    multiplier_str = str(multiplier)
    results = [[] for length in range(11)]

    results[0] = [""]

    digits = "0123456789"

    starts = [""]

    for length in range(1, 11):
        next_starts = []
        for start in starts:
            for d in digits:
                if d in start or d in str(multiplier):
                    continue
                product = str(multiplier * int(d + start))

                if no_double_digits(product[-length:]):
                    next_starts.append(d + start)
                if not no_double_digits(product):
                    continue
                else:
                    results[length].append(d + start)
        starts = next_starts


    output = [[[] for __ in range(10)] for _ in range(11)]
    for length in range(1, 11):
        for x in results[length]:
            if x[0] != "0" and str(int(x) * multiplier)[0] != "0":
                pair = (multiplier * int(x), int(x))
                output[len(str(pair[0]))][int(str(pair[0])[0])].append(pair)
        for d in range(10):
            output[length][d] = sorted(output[length][d], key=lambda x: x[0])
            output[length][d] = [(str(x), str(y)) for (x, y) in output[length][d]]
    output[0] = [("0", "0")]

    return output

def find_best(multiplier, output_head="", input_head="", uniques=[], depth=0):
    if len(output_head) == 10:
        if len(input_head) == 10 - len(str(multiplier)) and depth > 1:
            return output_head, input_head
        else:
            return "0", ""
    if not uniques:
        uniques = generate_uniques(multiplier)
    best_input_head = ""
    best_output_head = "0"

    for d in range(10)[::-1]:
        if str(d) in output_head:
            continue
        if best_output_head != "0":
            continue

        for length in range(1, 11 - len(output_head)):
            for pair_output, pair_input in uniques[length][d]:
                if compatible(pair_output, output_head):
                    if compatible(pair_input, input_head):
                        new_output, new_input = find_best(multiplier, output_head + pair_output, input_head + pair_input, uniques, depth + 1)
                        if int(new_output) > int(best_output_head):
                            best_output_head = new_output
                            best_input_head = new_input
                            break
    return best_output_head, best_input_head

best = 0
for x in range(2, 100):
    best = max(best, int(find_best(x)[0]))
print(best)