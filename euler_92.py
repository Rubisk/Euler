import numpy as np
import sys


def find_number_of_starting_numbers_ending_at_89(maximum):
    squares = [x * x for x in range(10)]
    values = np.zeros(10 * maximum + 1)
    values[1] = 1
    values[89] = 89
    for v in reversed(range(1, maximum)):
        if v % (maximum / 100) == 0:
            print v / (maximum / 100)
        chain = v
        passed = []
        while chain >= 10 * maximum or values[chain] == 0:
            passed.append(chain)
            chain = sum([squares[int(x)] for x in str(chain)])
        for p in passed:
            values[p] = values[chain]
        values[v] = values[chain]
    return len(np.where(values == 89)[0])


if __name__ == "__main__":
    print find_number_of_starting_numbers_ending_at_89(int(sys.argv[-1]))
