import sys
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


def find_sum_of_special_sets_in_file(path):
    sets = open(path).read().splitlines()
    total = 0
    for s in sets:
        s = [int(n) for n in s.split(",")]
        if is_special_sum_set(s):
            total += sum(s)
    return total


if __name__ == "__main__":
    print find_sum_of_special_sets_in_file(sys.argv[-1])
