import sys
import pytest
import itertools


def faculty(n):
    if n in (0, 1):
        return 1
    return n * faculty(n - 1)


def extended_combinations(it, n):
    for i in range(n):
        for c in itertools.combinations_with_replacement(it, i + 1):
            yield c


def get_digit_factorials():
    factorials = [faculty(n) for n in range(10)]
    max_digits = 0
    while len(str(factorials[9] * max_digits)) > max_digits:
        max_digits += 1
    for digits in extended_combinations(range(10), max_digits + 1):
        digits = [d for d in digits]
        number = sum([factorials[d] for d in digits])
        if len(str(number)) != len(digits) or len(str(number)) == 1:
            continue
        string = [x for x in str(number)]
        for d in digits:
            if str(d) in string:
                string.remove(str(d))
            else:
                break
        if len(string) == 0:
            yield number


def test_get_digit_factorials():
    assert 145 in [x for x in get_digit_factorials()]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(get_digit_factorials())