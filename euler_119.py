import sys
import pytest


def sum_digits(n):
    return sum([int(d) for d in str(n)])


def find_sequence_entry(index):
    i = 1
    found = []
    while len(found) - 1 <= index or 10 ** (i / 9) <= found[index + 1]:
        i += 1
        n = 2
        while i ** n <= 10 ** i:
            if sum_digits(i ** n) == i:
                found.append(i ** n)
                found = sorted(found)
            n += 1
    return found[index - 1]


def test_find_sequence_entry():
    assert find_sequence_entry(2) == 512
    assert find_sequence_entry(10) == 614656

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    print find_sequence_entry(int(sys.argv[-1]))
