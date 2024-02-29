import sys
import pytest
import math
import fractions


def get_pell_number_pairs():
    n1 = 1
    n2 = 2
    while True:
        yield n1, n2
        n1, n2 = n2, n1 + 2 * n2

def get_solution_count(maximum):
    total = 0
    for m, n in get_pell_number_pairs():
        perimeter = 2 * n ** 2 + 2 * n * m
        if perimeter > maximum:
            break
        total += maximum / perimeter
    return total

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print(get_solution_count(int(sys.argv[1])))
