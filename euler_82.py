import sys
import pytest


def check_bounds(x, y, size):
    return 0 <= x < size and 0 <= y < size


def find_minimum_path_sum(string):
    matrix = [[int(i) for i in l.split(",")] for l in string.splitlines()]
    size = len(matrix)
    queue = [(i, size - 1) for i in range(size)]  # y, x
    minimum_matrix = [[0 for _ in range(size)] for __ in range(size)]
    for i in range(size):
        minimum_matrix[i][size - 1] = matrix[i][size - 1]

    while len(queue) > 0:
        new_queue = []
        for check in queue:
            x, y = check
            current = minimum_matrix[x][y]
            for dx, dy in ((1, 0), (-1, 0), (0, -1)):
                _x, _y = x + dx, y + dy
                if not check_bounds(_x, _y, size):
                    continue
                if minimum_matrix[_x][_y] == 0 or minimum_matrix[_x][_y] > current + matrix[_x][_y]:
                    minimum_matrix[_x][_y] = current + matrix[_x][_y]
                    new_queue.append((_x, _y))
        queue = new_queue
    return min([row[0] for row in minimum_matrix])


def test_find_minimum_path_sum():
    assert find_minimum_path_sum(open("euler_81_test.txt").read()) == 994


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_minimum_path_sum(open(sys.argv[-1]).read())