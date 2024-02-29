import sys
import pytest
import itertools as it


def find_all_sets(nodes):
    outer = range(nodes + 1, nodes * 2 + 1)
    inner = range(1, nodes + 1)
    for outer_perm in it.permutations(outer[1:]):
        outer_perm = [outer[0]] + list(outer_perm)
        for inner_perm in it.permutations(inner):
            totals = [outer_perm[i] + inner_perm[i] + inner_perm[i - 1] for i in range(nodes)]
            correct = all([totals[i] == totals[0] for i in range(1, nodes)])
            if correct:
                to_yield = [(outer_perm[i], inner_perm[i], inner_perm[i - 1]) for i in reversed(range(nodes))]
                while to_yield[0][0] != nodes + 1:
                    to_yield.append(to_yield[0])
                    to_yield = to_yield[1:]
                yield to_yield


def set_to_string(set):
    string = []
    for s in set:
        string.extend([str(i) for i in s])
    return "".join(string)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print max([int(set_to_string(x)) for x in find_all_sets(int(sys.argv[-1]))])
