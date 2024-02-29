import sys
import pytest


def ggd(a, b):
    if b > a:
        b, a = a, b
    if a % b == 0:
        return b
    return ggd(a % b, b)


def find_all_almost_equilateral_triangles(maximum):
    x_array = [1, 4]
    y_array = [2, 7]

    def get_y(n):
        while n >= len(y_array):
            y_array.append(4 * y_array[-1] - y_array[-2])
        return y_array[n]

    def get_x(n):
        while n >= len(x_array):
            x_array.append(4 * x_array[-1] - x_array[-2])
        return x_array[n]

    index = 0
    total = 0
    keep_going = True
    while keep_going:
        keep_going = False
        for l in (4 * get_y(index) ** 2,
                  2 * (get_x(index) + get_x(index + 1)) ** 2):
            if l <= maximum:
                total += l
                keep_going = True
        index += 1
    return total


def test_find_all_almost_equilateral_trinagles():
    assert find_all_almost_equilateral_triangles(16) == 16
    assert find_all_almost_equilateral_triangles(54) == 66


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_all_almost_equilateral_triangles(int(sys.argv[-1]))
