import sys
import pytest


def get_next_expansion(numerator, denominator):
    n = numerator + denominator
    return n + denominator, n


def find_all_with_more_digits_in_denominator(number):
    n, d = 1, 1
    for _ in range(number):
        n, d = get_next_expansion(n, d)
        if len(str(n)) > len(str(d)):
            yield n, d

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print len([x for x in find_all_with_more_digits_in_denominator(int(sys.argv[-1]))])
