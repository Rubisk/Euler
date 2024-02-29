import sys
import pytest

numbers = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}

numbers_iter = [
    ("M", 1000),
    ("D", 500),
    ("C", 100),
    ("L", 50),
    ("X", 10),
    ("V", 5),
    ("I", 1),
]


def roman_to_decimal(string):
    total = 0
    string = list(string)
    for letter, value in numbers_iter:
        if len(string) > 1 and numbers[string[1]] > numbers[string[0]]:
            total -= numbers[string[0]]
            string = string[1:]
            total += numbers[string[0]]
            string = string[1:]
        while len(string) > 0 and string[0] == letter:
            total += value
            string = string[1:]
        if len(string) == 0:
            break
    return total


def decimal_to_roman(number):
    string = ""
    for letter, value in numbers_iter:
        while number >= value:
            number -= value
            string += letter
        if number > value / 2:
            for letters, power, preletter in ((("V", "X"),   1, "I"),
                                              (("L", "C"),  10, "X"),
                                              (("D", "M"), 100, "C")):
                if letter in letters:
                    if number / power in (4, 9):
                        number -= (numbers[letter] - power)
                        string += preletter
                        string += letter
    return string


def test_roman_to_decimal():
    assert roman_to_decimal("MCMI") == 1901
    assert roman_to_decimal("MDMI") == 1501
    assert roman_to_decimal("VVVI") == 16
    assert roman_to_decimal("XVI") == 16
    assert roman_to_decimal("MMMMCCCXIV") == 4314


def test_decimal_to_roman():
    assert decimal_to_roman(2196) == "MMCXCVI"
    assert decimal_to_roman(49) == "XLIX"
    assert decimal_to_roman(1606) == "MDCVI"


def find_number_of_characters_saved(string):
    strings = string.splitlines()
    total = 0
    for n in strings:
        old = len(n)
        new = len(decimal_to_roman(roman_to_decimal(n)))
        if not old - new >= 0:
            print n, decimal_to_roman(roman_to_decimal(n))
        total += (old - new)
    return total


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_number_of_characters_saved(open(sys.argv[-1]).read())
