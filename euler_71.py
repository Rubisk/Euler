import sys


def compare((n1, d1), (n2, d2)):
    return n1 * d2 < n2 * d1


def get_fraction_left_of(n, d, maximum_d):
    search_n = 0
    search_d = 1
    found = (0, 1)
    while search_d < maximum_d:
        search_d += 1
        while compare((search_n + 1, search_d), (n, d)):
            search_n += 1
        if not compare((search_n, search_d), found):
            found = (search_n, search_d)
    return found


if __name__ == "__main__":
    print get_fraction_left_of(*[int(i) for i in sys.argv[-3:]])
