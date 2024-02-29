import sys
import pytest
import math


def fibonacci(maximum):
    n1 = 1
    n2 = 1
    while n1 < maximum:
        yield n1
        n1, n2 = n2, n1 + n2

def special_fibonacci(maximum):
    n1 = 1
    n2 = 4
    while n1 < maximum:
        yield n1
        n1, n2 = n2, n1 + n2


def solutions(maximum):
    for n in range(maximum):
        if math.sqrt(5 * n ** 2 + 14 * n + 1).is_integer():
            yield n


def generate_solutions(count):
    maximum = 10 ** count
    fib = list(fibonacci(maximum))
    s_fib = list(special_fibonacci(maximum))
    found = []
    n = 0
    i = 0
    while i < len(s_fib[2::4]):
        found.append(n)
        n += s_fib[2::4][i]
        i += 1
    c = 2
    i = 0
    while i < len(s_fib[1::4]):
        c += fib[4 * i - 4 - 1] if i > 1 else 0
        found.append(s_fib[1::4][i] - c)
        i += 1
    return sorted(found)[:count + 1]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    print sum(generate_solutions(int(sys.argv[1])))
