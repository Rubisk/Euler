import sys
import pytest
import numpy as np


def get_product(digits, grid, x, y, dx, dy):
    numbers = [grid[x+dx*r][y+dy*r] for r in range(digits)]
    return np.prod(numbers), numbers


def get_highest_grid_product(digits, string):
    lines = string.splitlines()
    grid = np.array([[int(x) for x in line.split()] for line in lines])
    width, height = len(grid), grid[0].size

    max_product = 0
    x = digits - 1
    while x < width:
        y = digits - 1
        while y < width:
            for d in ((-1, 0), (-1, -1), (0, -1)):  # (x, y)
                product, numbers = get_product(digits, grid, x, y, *d)
                if max_product < product:
                    max_product = product
            if y < width - digits:
                product, numbers = get_product(digits, grid, x, y, -1, 1)
                if max_product < product:
                    max_product = product
            y += 1
        x += 1
    return max_product


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_highest_grid_product(int(sys.argv[-2]),
                                       open(sys.argv[-1]).read())
