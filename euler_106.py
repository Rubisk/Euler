import itertools as it
import sys
import pytest


def brute_force_search(n):
    total = 0
    for i in range(4, n + 1):
        if i % 2 == 1:
            continue
        numbers = list(range(n))
        for full_comb in it.combinations(numbers, i):
            for half in it.combinations(full_comb, i / 2):
                other_half = sorted([x for x in full_comb if x not in half])
                half, other_half = half, other_half if half[0] < other_half[0] else (other_half, half)
                if not all([a < b for a, b in zip(half, other_half)]):
                    total += 1
    return total


def test_brute_force_search():
    assert brute_force_search(4) == 1
    assert brute_force_search(7) == 70


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print brute_force_search(int(sys.argv[-1]))
