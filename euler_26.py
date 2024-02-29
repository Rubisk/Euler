import sys
import pytest


def get_recurring_cycle(n):
    modulos = []
    leftover = 10
    while leftover not in modulos:
        modulos.append(leftover)
        leftover %= n
        leftover *= 10
    return len(modulos) - modulos.index(leftover)


def test_get_recurring_cycle():
    assert get_recurring_cycle(2) == 1
    assert get_recurring_cycle(6) == 1
    assert get_recurring_cycle(7) == 6
    assert get_recurring_cycle(11) == 2


def find_biggest_recurring_cycle(maximum):
    b = (1, 1)
    for i in range(1, maximum):
        c = get_recurring_cycle(i)
        if c > b[1]:
            b = i, c
    return b[0]

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_biggest_recurring_cycle(int(sys.argv[-1]))