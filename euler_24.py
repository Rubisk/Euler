import sys
import pytest


def faculty(n):
    if n == 1:
        return n
    return n * faculty(n - 1)


def get_permutation(number, characters):
    if len(characters) == 1:
        assert number == 1 or number == 0
        return characters[0]
    characters = [c for c in characters]
    size = len(characters)
    f = faculty(size - 1)
    n = 1
    while n * f < number:
        n += 1
    first_char = characters[n - 1]
    characters.remove(first_char)
    return first_char + get_permutation(number - (n - 1) * f, characters)


def test_get_permutation():
    assert get_permutation(3, "012") == "102"
    assert get_permutation(24, "1234") == "4321"


if __name__ == "__main__":
    if '-test' in sys.argv:
        pytest.main(__file__)
    else:
        print get_permutation(int(sys.argv[1]), sys.argv[2])
