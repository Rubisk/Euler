import sys
import pytest


def is_bouncy(n):
    digits = [int(d) for d in str(n)]
    if len(digits) <= 2:
        return False
    increasing = all([digits[i] <= digits[i + 1] for i in range(len(digits) - 1)])
    decreasing = all([digits[i] >= digits[i + 1] for i in range(len(digits) - 1)])
    return not (increasing or decreasing)


def test_is_bouncy():
    assert is_bouncy(155349)
    assert not is_bouncy(134468)
    assert not is_bouncy(66420)


def find_least_with_percentage(percentage):
    bouncy_count = 0.0
    not_bouncy_count = 0.0
    i = 1
    while not_bouncy_count == 0 or bouncy_count / (bouncy_count + not_bouncy_count) * 100 != percentage:
        if is_bouncy(i):
            bouncy_count += 1
        else:
            not_bouncy_count += 1
        i += 1
    return i - 1


def test_find_least_with_percentage():
    assert find_least_with_percentage(90) == 21780


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_least_with_percentage(int(sys.argv[-1]))
