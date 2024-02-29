import itertools as it
import sys
import pytest


def ggd(a, b):
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)


def get_triangles_at_corner(x, y, dimension):
    # assert 0 < x < dimension
    # assert 0 < y < dimension
    g = ggd(x, y)
    dx, dy = y / g, x / g
    max_x_left = x / dx
    max_x_right = (dimension - x) / dx
    max_y_left = (dimension - y) / dy
    max_y_right = y / dy
    return min(max_x_left, max_y_left) + min(max_x_right, max_y_right)


def find_right_triangles(dimension):
    total = 0
    for x, y in it.product(range(dimension + 1), repeat=2):
        if x == 0 and y == 0:
            total += dimension * dimension
            continue
        elif x == 0 or y == 0:
            total += dimension
        # elif x == dimension or y == dimension:
        #     continue
        else:
            total += get_triangles_at_corner(x, y, dimension)
    return total


def test_get_triangles_at_corner():
    assert get_triangles_at_corner(1, 1, 2) == 2
    assert get_triangles_at_corner(1, 2, 3) == 1
    assert get_triangles_at_corner(2, 2, 3) == 2
    assert get_triangles_at_corner(3, 3, 4) == 2
    assert get_triangles_at_corner(3, 1, 4) == 1
    assert get_triangles_at_corner(4, 2, 4) == 1


def test_find_right_triangles():
    assert find_right_triangles(2) == 14
    assert find_right_triangles(4) == 62


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_right_triangles(int(sys.argv[-1]))