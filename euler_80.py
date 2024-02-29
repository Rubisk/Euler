import sys
import pytest
import math


def get_continued_fraction(p, length=100):
    root = math.sqrt(p)
    assert not root.is_integer()
    cycles = []
    x = math.floor(root)
    d = x
    n = p - x ** 2
    cycles.append((x, n, d))
    while True:
        x = math.floor((root + d) / n)
        d -= n * x
        if (x, n, d) in cycles:
            while len(cycles) < length:
                cycles.extend(cycles[cycles.index((x, n, d)):])
            return [int(c[0]) for c in cycles[:length]]
        cycles.append((x, n, d))
        d, n = n, d
        new_d = -n
        n = p - n * n
        n /= d
        d = new_d


def convert_to_one_fraction(expansion):
    expansion = [e for e in expansion]
    if len(expansion) == 1:
        return expansion[0], 1
    if len(expansion) == 2:
        return expansion[0] * expansion[1] + 1, expansion[1]
    n = expansion[-1]
    d = 1
    for a in reversed(expansion[1:-1]):
        d, n = n, d + a * n
    return d + expansion[0] * n, n


def find_sum_of_expansion(root, digits):
    if math.sqrt(root).is_integer():
        return 0
    n, d = list(convert_to_one_fraction(get_continued_fraction(root, digits * 2)))
    decimals = []
    for i in range(digits):
        decimals.append(int(n / d))
        n *= 10
        n %= (10 * d)
    return sum(decimals)


def test_get_continued_fraction():
    assert get_continued_fraction(2, 10) == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]


def test_convert_to_one_fraction():
    print convert_to_one_fraction(get_continued_fraction(2, 20))


def test_find_sum_of_expansion():
    assert find_sum_of_expansion(2, 100) == 475


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    try:
        print sum([find_sum_of_expansion(i, int(sys.argv[-1])) for i in range(1, int(sys.argv[-2]) + 1)])
    except ValueError:
        print "Script invocation: [D] [N]"
        print "[D]: Number of digits to count for each root (integer)."
        print "[N]: Highest root to evaluate (integer)."
