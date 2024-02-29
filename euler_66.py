import math
import sys
import pytest
from euler_64 import get_continued_fraction
from euler_65 import convert_to_one_fraction


def find_smallest_solution(D):
    if math.sqrt(D).is_integer():
        return 0, 0
    fraction = get_continued_fraction(D, True)
    continued = get_continued_fraction(D)
    i = 1
    while True:
        if i > len(fraction):
            fraction.extend(continued)
        n, d = convert_to_one_fraction(fraction[:i])
        if n * n - D * d * d == 1:
            return n, d
        i += 1
    assert False


def test_find_smallest_solution():
    assert find_smallest_solution(7) == (8, 3)
    assert find_smallest_solution(5) == (9, 4)
    assert find_smallest_solution(13) == (649, 180)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        solutions = [find_smallest_solution(x)[0] for x in range(1, int(sys.argv[-1]) + 1)]
        print solutions.index(max(solutions)) + 1
