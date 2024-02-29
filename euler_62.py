import sys
import pytest


def find_smallest_cube_with_cube_permutations(permutations):
    n = 1
    n_accent = 0
    c = 1
    cube = 1
    permutation_dict = {}
    while True:
        cube += 1
        n_accent += 6
        n += n_accent
        c += n
        digits = "".join(sorted(str(c)))
        if permutation_dict.get(digits) is None:
            permutation_dict[digits] = []
        permutation_dict[digits].append(c)
        if len(permutation_dict[digits]) >= permutations:
            return min(permutation_dict[digits])


def test_find_smalles_cube_with_permutations():
    assert find_smallest_cube_with_cube_permutations(3) == 41063625

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_smallest_cube_with_cube_permutations(int(sys.argv[-1]))