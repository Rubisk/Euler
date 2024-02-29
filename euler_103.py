import sys
import pytest
import itertools as it


def is_special_sum_set(sum_set):
    sum_set = sorted(sum_set)
    n = len(sum_set)
    for i in range(2, (n + 1) / 2 + 1):
        if not sum(sum_set[:i]) > sum(sum_set[-(i - 1):]):
            return False
    for i in range(1, n / 2 + 1):
        found = []
        for c in it.combinations(sum_set, i):
            s = sum(c)
            if s in found:
                return False
            found.append(s)
    return True


def test_is_special_sum_set():
    assert is_special_sum_set([11, 17, 20, 22, 23, 24])
    assert is_special_sum_set([11, 18, 19, 20, 22, 25])
    assert not is_special_sum_set([11, 15, 16, 20, 22, 25])
    assert is_special_sum_set([11, 18, 19, 20, 22, 25])


def partition_in_pieces(integer, pieces, min_piece=1, max_piece=-1):
    if pieces == 1:
        yield [integer]
        return
    max_piece = integer - pieces if max_piece == -1 else min(integer - pieces, max_piece)
    for n in range(min_piece, max_piece):
        for p in partition_in_pieces(integer - n, pieces - 1, min_piece=n + 1, max_piece=max_piece):
            yield [n] + p


def find_possible_sum_sets(maximum, n):
    print maximum, n
    m = 0
    for p in partition_in_pieces(maximum, n, 19, 54):
        # print p
        assert sum(p) == maximum
        if is_special_sum_set(p):
            yield p
        # m += 1
        # if m % 10000 == 0:
        #     print p


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print is_special_sum_set([22, 33, 40, 41, 42, 44, 47])
        for x in find_possible_sum_sets(int(sys.argv[-1]), int(sys.argv[-2])):
            print "++++++++++++++"
            print x
            print "++++++++++++++"
