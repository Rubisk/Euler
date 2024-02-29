import sys
import pytest


def is_pandigital_1_through_9(n):
    if len(n) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True


def find_biggest_pandigitial():
    i = 5
    n = 1
    while i > 1:
        string = "".join([str(n * j) for j in range(1, i + 1)])
        while len(string) > 9:
            i -= 1
            string = "".join([str(n * j) for j in range(1, i + 1)])
        if is_pandigital_1_through_9(string):
            yield int(string)
        n += 1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print max(find_biggest_pandigitial())
