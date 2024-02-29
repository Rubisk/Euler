import sys
import pytest


def get_all_digit_sums(maximum_value):
    for a in range(1, maximum_value):
        total = 1
        for b in range(maximum_value):
            total *= a
            yield sum([int(i) for i in str(total)])

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print max(get_all_digit_sums(int(sys.argv[-1])))
