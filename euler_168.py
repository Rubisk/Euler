import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections



def find_all_rotating_numbers(codivisor, last_digit, max_digits):
    digits = [str(last_digit)]
    while len(digits) < max_digits:
        product = str(int("".join(digits)) * codivisor)
        next_digit = product[-len(digits) - 0]
        digits = [next_digit] + digits
        if int("".join(digits)) * codivisor == int(digits[-1] + "".join(digits[:-1])):
            if digits[0] == "0":
                continue
            if codivisor > 10:
                print(int("".join(digits)), codivisor)
            yield int("".join(digits))  

numbers = set()

for last_digit in range(1, 10):
    for codivisor in range(1, 100):
        for number in find_all_rotating_numbers(codivisor, last_digit, 100):
            numbers.add(number)

print(min(numbers))

print(sum(numbers))