import sys
import pytest
import copy
import itertools as it


def find_all_polygonal_numbers(polygonal, mimimum, maximum):
    n = 0
    polygonal -= 2
    difference = 1
    numbers = []
    while n < maximum:
        n += difference
        difference += polygonal
        if mimimum <= n < maximum:
            numbers.append(n)
    return numbers


def test_find_all_polygonal_numbers():
    assert find_all_polygonal_numbers(6, 3, 56) == [6, 15, 28, 45]


def merge(array_1, array_2):
    new_array = []
    for i in array_1:
        end = i[-1] % 100
        minimum = end * 100
        maximum = end * 100 + 100
        # print minimum, maximum
        for j in array_2:
            if minimum <= j < maximum:
                new = copy.copy(i)
                new.append(j)
                new_array.append(new)
    return new_array


def find_cyclic_set_of_4_digit_numbers():
    polygonals = []
    for i in range(3, 9):
        polygonals.append(find_all_polygonal_numbers(i, 1000, 10000))
    for p in it.permutations(polygonals):
        p = list(p)
        p[0] = [[n] for n in p[0]]
        while len(p) > 1:
            new = merge(p[0], p[1])
            p = p[1:]
            p[0] = new
        for possibility in p[0][1:]:
            if str(possibility[5])[2:] == str(possibility[0])[:2]:
                print sum(possibility)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        find_cyclic_set_of_4_digit_numbers()
