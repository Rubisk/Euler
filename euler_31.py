import sys
import pytest


def _get_possibilities(total, coins):
    if len(coins) == 1:
        return 1
    possibilities = 0
    coin = coins[0]
    n = 0
    while n * coin <= total:
        possibilities += get_possibilities(total - n * coin, coins[1:])
        n += 1
    return possibilities


def get_possibilities(total, coins):
    coins = sorted(coins, reverse=True)
    return _get_possibilities(total, coins)


def test_get_possibilities():
    assert get_possibilities(5, [1]) == 1
    assert get_possibilities(4, [1, 2]) == 3
    assert get_possibilities(10, [1, 2, 5, 10]) == 11


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_possibilities(int(sys.argv[1]), [int(x) for x in sys.argv[2:]])
