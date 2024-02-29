import sys
import pytest
import math


def find_biggest(index_numbers):
    tree = {}
    for base, exp in index_numbers:
        tree[exp * math.log(base)] = base, exp
    for i in reversed(sorted(tree.keys())):
        return tree[i]


def test_find_biggest():
    assert find_biggest([(632382, 518061), (519432, 525806)]) == (632382, 518061)


def find_largest_line_number(path):
    tuples = open(path).read().splitlines()
    tuples = [x.split(",") for x in tuples]
    tuples = [(int(x), int(y)) for x, y in tuples]
    return tuples.index(find_biggest(tuples)) + 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_largest_line_number(sys.argv[-1])
