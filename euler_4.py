import numpy as np


def powers(number, power):
    return np.prod([number for _ in range(power)])


def is_palindrome(number, digits):
    for d in range((digits - 1) / 2 + 1):
        left_power = powers(10, digits - d - 1)
        right_power = powers(10, d)
        left_digit = number / left_power % 10
        right_digit = number / right_power % 10
        if left_digit != right_digit:
            return False
    return True


def test_is_palindrome():
    assert is_palindrome(900009, 6)
    assert not is_palindrome(990009, 6)


def find_biggest_palindrome(maximum):
    r = range(int(np.sqrt(np.sqrt(maximum))), int(np.sqrt(maximum)))
    for x in range(maximum):
        if is_palindrome(maximum - x, len(str(maximum - x))):
            target = maximum - x
            for number in r:
                if target % number == 0:
                    if target / number < np.sqrt(maximum):
                        return target

if __name__ == '__main__':
    print find_biggest_palindrome(999999)
