import sys
import pytest


def names_from_file(string):
    return [n.replace("\"", "").lower() for n in string.split(",")]


def names_to_numbers(names):
    def _get_value(character):
        return ord(character) - 96

    for i in range(len(names)):
        names[i] = tuple([_get_value(c) for c in names[i]])
    return names


def compare_strings(left, right):
    if left == right:
        return 0
    for i in range(min(len(left), len(right))):
        if left[i] > right[i]:
            return 1
        if left[i] < right[i]:
            return -1
    if len(left) > len(right):
        return 1
    return -1


def _merge(left, right):
    merged = []
    l = len(left)
    r = len(right)
    while len(left) + len(right) > 0:
        if len(left) == 0:
            merged.extend(right)
            break
        elif len(right) == 0:
            merged.extend(left)
            break
        else:
            c = compare_strings(left[0], right[0])
            if c == 1:
                merged.append(right[0])
                right = right[1:]
            elif c == -1:
                merged.append(left[0])
                left = left[1:]
            elif c == 0:
                print left[0], right[0]
                assert False
    assert len(merged) == l + r
    return merged


def sort_names(names):
    names = names_to_numbers(names)
    names = [(n,) for n in names]

    def _sort(names_):
        if len(names_) == 1:
            return names_

        new_names = []
        for index in range(0, len(names_) / 2):
            l, r = names_[2 * index], names_[2 * index + 1]
            new_names.append(_merge(l, r))
        if len(names_) % 2 == 1:
            new_names.append(names_[-1])
        return _sort(new_names)

    sorted_names = _sort(names)[0]
    assert len(sorted_names) == len(names)
    return sorted_names


def get_total(names):
    total = 0
    for i in range(1, len(names) + 1):
        total += i * sum(names[i - 1])
    return total


def evaluate_name_sum(string):
    return get_total(sort_names(names_from_file(string)))


def test_merge():
    assert _merge([(1,), (5,), (6,)], [(3,), (4,), (8,)]) == [(1,), (3,), (4,), (5,), (6,), (8,)]


def test_sort():
    assert sort_names(["d", "a", "b", "f", "g"]) == [(1,), (2,), (4,), (6,), (7,)]
    assert sort_names(["renae", "zelda", "elda", "ma"]) == \
        [(5, 12, 4, 1), (13, 1), (18, 5, 14, 1, 5), (26, 5, 12, 4, 1)]


def test_get_total():
    assert get_total([(18, 5, 14, 1, 5), (26, 5, 12,4, 1)]) == sum((18, 5, 14, 1, 5)) + 2 * sum((26, 5, 12,4, 1))


if __name__ == "__main__":
    test_merge()
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print evaluate_name_sum(open(sys.argv[1]).read())
