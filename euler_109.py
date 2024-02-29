import itertools as it
import sys


doubles = [2 * i for i in range(1, 21)] + [50]
all_possibilities = doubles + [3 * i for i in range(1, 21)] + range(1, 21) + [25, 0]


def find_all_endings():
    for d in doubles:
        for c in it.combinations_with_replacement(all_possibilities, 2):
            yield [d] + list(c)


if __name__ == "__main__":
    print len([x for x in find_all_endings() if sum(x) < int(sys.argv[-1])])
