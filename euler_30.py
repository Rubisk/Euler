from itertools import combinations_with_replacement
import sys
import pytest


def extended_combinations_with_replacement(gen, n):
    for i in range(2, n + 1):
        for c in combinations_with_replacement(gen, i):
            # print c
            yield c


def powers(a, b):
    if b == 1:
        return a
    else:
        return a * powers(a, b - 1)


def find_all_digit_sum_numbers(power):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digit_powers = [(powers(n, power), n) for n in digits]
    m = 1
    while int("".join(["9" for _ in range(m)])) < m * powers(9, power):
        m += 1
    for c in extended_combinations_with_replacement(digit_powers, m):
        digits = [str(d[1]) for d in c]
        digit_sum = sum([d[0] for d in c])
        if len(digits) != len(str(digit_sum)):
            continue
        good = True
        for d in str(digit_sum):
            if d not in digits:
                good = False
                break
            digits.remove(d)
        if good:
            yield digit_sum


def test_find_all_digit_sum_numbers():
    assert [x for x in find_all_digit_sum_numbers(4)] == [8208, 1634, 9474]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(find_all_digit_sum_numbers(int(sys.argv[-1])))
