import sys
import pytest


def goes_above_origin((x1, y1), (x2, y2)):
    r = (y1 - y2) / (x1 - x2)
    h = y1 - x1 * r
    return h > 0


def contains_origin(triangle):
    triangle = sorted(triangle)
    if triangle[0][0] > 0 or triangle[2][0] < 0:
        return False
    line_1 = (triangle[0], triangle[2])
    line_2 = (triangle[0] if triangle[1][0] > 0 else triangle[2], triangle[1])
    return sum([goes_above_origin(l[0], l[1]) for l in (line_1, line_2)]) == 1


def test_goes_above_origin():
    assert not goes_above_origin((-10, -5), (20, 3))
    assert goes_above_origin((1, 1), (-3, 2))


def test_contains_origin():
    assert contains_origin(((-2, -2), (3, 0), (0, 3)))
    assert not contains_origin(((-2, 1), (0, 5), (3, 7)))
    assert not contains_origin(((-2, -2), (3, 0), (1, 0)))
    assert contains_origin(((-340, 495), (-153, -910), (835, -947)))
    assert not contains_origin(((-175, 41), (-421, -714), (574, -645)))
    assert not contains_origin(((-1, -1), (0, -1), (1, 0)))


def evaluate_file(path):
    string = open(path).read()
    triangles = [line.split(",") for line in string.splitlines()]
    triangles = [[(float(t[i * 2]), float(t[i * 2 + 1])) for i in range(3)] for t in triangles]
    return sum([contains_origin(t) for t in triangles])

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print evaluate_file(sys.argv[-1])
