import sys
import pytest
import numpy as np
import itertools as it


def plus(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def get_all_possible_values(integers):
    if len(integers) == 1:
        yield integers[0]
        return
    for first in integers:
        leftovers = [x for x in integers if x != first]
        for operation in (plus, multiply, subtract, divide):
            for value in get_all_possible_values(leftovers):
                if value == 0 and operation == divide:
                    continue
                yield operation(first, value)
                if operation == plus:
                    yield operation(-first, value)


def find_all_possible_values(integers):
    integers = [float(x) for x in integers]
    for v in get_all_possible_values(integers):
        if v.is_integer() and v > 0:
            yield v


def test_find_all_possible_values():
    found = list(find_all_possible_values([1, 2, 3, 4]))
    print list([int(x) for x in np.unique(found)])
    assert len(np.unique(found)) == 31
    assert max(found) == 36


def find_number_of_consecutive_numbers(unique_founds):
    i = 1
    while i in unique_founds:
        i += 1
    return i - 1


def evaluate_number_set(integers):
    return find_number_of_consecutive_numbers(np.unique(list(find_all_possible_values(integers))))


def test_evaluate_number_set():
    assert evaluate_number_set([1, 2, 3, 4]) == 28


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        top = 0
        best = []
        for comb in it.combinations(range(1, 10), 4):
            if evaluate_number_set(comb) > top:
                best = comb
                top = evaluate_number_set(comb)
        print best
