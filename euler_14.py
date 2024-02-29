import numpy as np
import sys
import pytest


def find_longest_chain(maximum_start):
    starters = np.zeros(maximum_start, dtype='uint64')
    starters[2] = 1

    def find_chain_size(n):
        if n == 2:
            return 1
        if n % 2 == 0:
            next_number = n / 2
        else:
            next_number = n * 3 + 1
        if next_number >= maximum_start:
            size = find_chain_size(next_number) + 1
        elif starters[next_number] == 0:
            size = find_chain_size(next_number) + 1
        else:
            size = starters[next_number] + 1
        if n < maximum_start:
            starters[n] = size
        return size

    for start_number in range(1, maximum_start):
        if starters[start_number] != 0:
            continue
        find_chain_size(start_number)

    return np.where([starters == max(starters)])


def test_find_longest_chain():
    print find_longest_chain(10)
    assert False


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_longest_chain(int(sys.argv[-1]))
