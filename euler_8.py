import sys
import pytest
import numpy as np


def get_highest(digits, string):
    numbers = [int(x) for x in string if x in "0123456789"]
    current_digits = np.array(numbers[:digits])

    sum_max = sum(current_digits)

    for i in range(len(numbers) - digits):
        current_digits[i % digits] = numbers[i + digits]
        if np.prod(current_digits, dtype='uint64') > sum_max:
            sum_max = np.prod(current_digits, dtype='uint64')

    return sum_max


def test_get_highest():
    assert get_highest(4, open("euler_8.txt").read()) == 5832


if __name__ == '__main__':
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_highest(int(sys.argv[-1]),
                          open(sys.argv[-2]).read())
