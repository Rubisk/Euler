import sys
import pytest


alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_word_value(word):
    return sum([ord(c) - 96 for c in word.lower()])


def get_number_of_triangle_words(words):
    count = 0
    triangle_numbers = [1]
    for word in words:
        value = get_word_value(word)
        while value > triangle_numbers[-1]:
            n = len(triangle_numbers) + 1
            t = int(0.5 * n * (n + 1))
            triangle_numbers.append(t)
        if value in triangle_numbers:
            count += 1
    return count


def scan_file(filename):
    string = open(filename).read()
    words = string.split(",")
    for i in range(len(words)):
        words[i] = words[i].replace("\"", "")
    return get_number_of_triangle_words(words)


def test_get_word_value():
    assert get_word_value("SKY") == 55
    assert get_word_value("sky") == 55


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print scan_file(sys.argv[-1])
