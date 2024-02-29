import sys
import pytest
import itertools
from copy import copy


def get_all_base_10_palindromes(digits):
    assert digits % 2 == 0
    symbols = "0123456789"
    palindromes = []
    for j in range(1, (digits + 1) / 2 + 1):
        print j
        for c in itertools.product(symbols, repeat=j):
            c = list(c)
            if c[0] == "0":
                continue
            uneven_c = copy(c)
            even_c = copy(c)
            even_c.extend([i for i in reversed(c)])
            uneven_c.extend([i for i in reversed(c)][1:])
            palindromes.append("".join(uneven_c))
            palindromes.append("".join(even_c))
    palindromes = [int(p) for p in palindromes]
    return palindromes


class BaseTwoConverter(object):
    _powers = [1]

    def _assert_enough_powers(self, n):
        while n > self._powers[-1]:
            self._powers.append(self._powers[-1] * 2)

    def convert_to_base_two(self, n):
        self._assert_enough_powers(n)
        bits = [0 for _ in range(len(self._powers))]
        m = -1
        i = 1
        while n > 0:
            if self._powers[-i] <= n:
                if m == -1:
                    m = i - 1
                n -= self._powers[-i]
                bits[-i] = 1
            i += 1
        return "".join([str(i) for i in bits[:-m]])


def is_palindromic(string):
    l = [c for c in string]
    for i in range(len(string) / 2):
        if l[i] != l[-(i + 1)]:
            return False
    return True


def get_all_base_two_and_ten_palindromics(base_10_digits):
    palindromes = get_all_base_10_palindromes(base_10_digits)
    converter = BaseTwoConverter()
    as_two = [converter.convert_to_base_two(n) for n in palindromes]
    for i in range(len(palindromes)):
        if is_palindromic(as_two[i]):
            yield palindromes[i]


def test_get_base_10_palindromes():
    assert 5225 in get_all_base_10_palindromes(4)
    assert 0110 not in get_all_base_10_palindromes(4)


def test_base_two_converter():
    converter = BaseTwoConverter()
    assert converter.convert_to_base_two(5) == "101"
    assert converter.convert_to_base_two(21) == "10101"


def test_is_palindromic():
    assert is_palindromic("100001")
    assert is_palindromic("12321")
    assert not is_palindromic("100101")


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(get_all_base_two_and_ten_palindromics(int(sys.argv[-1])))
