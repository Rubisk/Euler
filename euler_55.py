import sys
import pytest
import numpy as np


def powers(number, power):
    return np.prod([number for _ in range(power)])


def reverse_and_add(i):
    return i + int("".join([s for s in reversed(str(i))]))


def is_palindrome(number):
    string = str(number)
    return all([string[i] == string[-(i + 1)] for i in range(len(string) / 2)])


def find_lychrel_numbers(maximum, iterations):
    for i in range(1, maximum + 1):
        lychrel = True
        m = i
        for j in range(iterations + 1):
            m = reverse_and_add(m)
            if is_palindrome(m):
                lychrel = False
                break
        if lychrel:
            yield i


def test_reverse_and_add():
    assert reverse_and_add(47) == 47 + 74
    assert reverse_and_add(123) == 123 + 321
    assert reverse_and_add(1230) == 1230 + 321


def test_is_palindrome():
    assert is_palindrome(100001)
    assert is_palindrome(121)
    assert not is_palindrome(123)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print len([x for x in find_lychrel_numbers(int(sys.argv[-2]), int(sys.argv[-1]))])