import sys
import pytest
import numpy as np

def get_solutions(maximum):
    solution_table = np.zeros(maximum + 1)
    a = 2
    while a < maximum:
        if a % 100000 == 0:
            print a
        solution_table[(- a ** 2 % (4 * a)):3 * a ** 2:4 * a] += 1
        a += 1
    solution_table[0] = 0
    return solution_table


def test_get_solutions():
    assert min(np.where(get_solutions(10000) == 10)[0]) == 1155

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print len(np.where(get_solutions(int(sys.argv[1])) == int(sys.argv[2]))[0])
