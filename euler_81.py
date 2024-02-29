import sys
import pytest


def find_minimum_path_sum(string):
    matrix = [[int(i) for i in l.split(",")] for l in string.splitlines()]
    for i in reversed(range(len(matrix))):
        for j in reversed(range(len(matrix))):
            if i + 1 == len(matrix) and j + 1 == len(matrix):
                continue
            left, down = 0, 0
            if j + 1 < len(matrix):
                left = matrix[i][j] + matrix[i][j + 1]
            if i + 1 < len(matrix):
                down = matrix[i][j] + matrix[i + 1][j]
            matrix[i][j] = left if i + 1 >= len(matrix) else (down if j + 1 >= len(matrix) else min(left, down))
    return matrix[0][0]


def test_find_minimum_path_sum():
    assert find_minimum_path_sum(open("euler_81_test.txt", "r").read()) == 2427


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_minimum_path_sum(open(sys.argv[-1]).read())
