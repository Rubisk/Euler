import sys
import pytest
import itertools as it


def find_anagrams_words(path):
    words = open(path).read().replace("\"", "").split(",")
    palindrome_dict = {}
    for w in words:
        key = "".join(sorted(w))
        if palindrome_dict.get(key) is None:
            palindrome_dict[key] = []
        palindrome_dict[key].append(w)
    for key in palindrome_dict.keys():
        if len(palindrome_dict[key]) > 1:
            yield palindrome_dict[key]


def encode(word_or_number):
    passed = []
    code = ""
    for c in str(word_or_number):
        if c not in passed:
            passed.append(c)
        i = passed.index(c)
        code += str(i)
    return code


def find_squares(maximum):
    s = 1
    n = 1
    squares = []
    while s <= maximum:
        squares.append(s)
        s += 2 * n + 1
        n += 1
    return squares


def test_encode():
    assert encode(1961) == "0120"
    assert encode("hello") == "01223"


def find_all_anagramic_squares(path):
    anagrams = list(find_anagrams_words(path))
    max_len = max([max([len(l) for l in s]) for s in anagrams])
    squares = find_squares(10 ** max_len)
    encoded_squares = {encode(s): [] for s in squares}
    for s in squares:
        encoded_squares[encode(s)].append(s)
    for group in anagrams:
        for left, right in it.combinations(group, 2):
            if encoded_squares.get(encode(left)) is not None and encoded_squares.get(encode(right)) is not None:
                for left_s in encoded_squares[encode(left)]:
                    d = {left[i]: str(left_s)[i] for i in range(len(left))}
                    right_s = int("".join([d[c] for c in right]))
                    if right_s in encoded_squares.get(encode(right)) and left_s > right_s:
                        print left, right, left_s, right_s


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        find_all_anagramic_squares(sys.argv[-1])
