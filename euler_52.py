import sys
import pytest


def get_smallest(times):
    n = (10 ** 16 - 1) / 17
    print n
    while True:
        digits = ["0"]
        digits.extend(sorted(str(n)))
        print digits
        i = 1
        while i < times:
            i += 1
            if sorted(str(n * i)) != digits:
                break
            if i == times:
                print n
        n += 1

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_smallest(int(sys.argv[-1]))