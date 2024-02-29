import itertools as it
import copy
import numpy as np


squares = ((0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (1, 8))
square_values = (0, 1, 2, 3, 4, 5, 6, 8)


def faculty(n):
    if n < 0:
        print n
        return
    if n in (0, 1):
        return 1
    return n * faculty(n - 1)


def choose(n, m):
    return faculty(n) / faculty(m) / faculty(n - m)
#
#
# def brute_force_rate_possibility(cube1, cube2_):
#     found = []
#     total = 0
#     cube2 = copy.copy(cube2_)
#     for c2 in it.combinations_with_replacement(range(10), 6 - len(cube2)):
#         test_c2 = sorted(cube2 + list(c2))
#         if test_c2 not in found:
#             total += 1
#             found.append(test_c2)
#     index = 0
#     while 6 in cube2:
#         index = cube2.index(6)
#         cube2[index] = 9
#         for c2 in it.combinations_with_replacement(range(10), 6 - len(cube2)):
#             test_c2 = sorted(cube2 + list(c2))
#             if test_c2 not in found:
#                 total += 1
#                 found.append(test_c2)
#     print found
#     n = 6 - len(cube2_)
#     sixes = len([x for x in cube2_ if x == 6])
#     assert total == choose(9 + n, 9) + sixes * choose(8 + n, 8)
#     return total
#
#
# class PossibilityFinder(object):
#     def __init__(self):
#         self.found = []
#
#     def find_all_possibilities(self):
#         for i in range(7):
#             for cube in it.combinations(square_values, i):
#                 self.find_number_of_possibilities(cube, [], squares)
#
#     def find_number_of_possibilities(self, cube1, cube2, squares_left, max_cube2=9):
#         if len(squares_left) == 0:
#             self.found.append((sorted(cube1), sorted(cube2)))
#             return 0
#
#         left_test, right_test = squares_left[0]
#         if (left_test in cube1 and right_test in cube2) or (right_test in cube1 and left_test in cube2):
#             self.find_number_of_possibilities(cube1, cube2, squares_left[1:], max_cube2)
#             return
#
#         if left_test in cube1 and right_test in cube1:
#             for d in left_test, right_test:
#                 self.find_number_of_possibilities(cube1, cube2 + [d], squares_left[1:], d)
#             return
#
#         for l, r in ((left_test, right_test), (right_test, left_test)):
#             if l in cube1 and r not in cube1:
#                 self.find_number_of_possibilities(cube1, cube2 + [r], squares_left[1:], max_cube2)
#                 return
#
#     @staticmethod
#
#     def rate_all_possibilities(self):
#         print self.found
#         assert len(self.found) > 0
#         total = 0
#         for f in self.found:
#             total += PossibilityFinder.rate_possibility(*f)
#         return total
#
#     def clear_double_possibilities(self):
#         assert len(self.found) > 0
#         for i1, i2 in it.combinations(range(len(self.found)), 2):
#             if i1 != i2 and self.is_same_possibility(self.found[i1], self.found[i2]):
#                 print self.found[i1], self.found[i2]
#                 self.found[i2] = ([], [])
#         while ([], []) in self.found:
#             self.found.remove(([], []))
#
#     @staticmethod
#     def is_same_possibility((cube1_left, cube1_right), (cube2_left, cube2_right)):
#         if cube1_left == [] or cube2_left == []:
#             return False
#         return len([x for x in cube2_left if x not in cube1_left]) <= 6 - len(cube1_left) and \
#             len([x for x in cube2_right if x not in cube1_right]) <= 6 - len(cube1_right)
#
#
# if __name__ == "__main__":
#     p = PossibilityFinder()
#     p.find_all_possibilities()
#     p.clear_double_possibilities()
#     print p.rate_all_possibilities()


def find_possibilities_for_cubes(cube1, cube2=None, squares_left=squares, max_cube2=9):
    if cube2 is None:
        cube2 = []

    if len(squares_left) == 0:
        yield sorted(cube2)
        return

    left_test, right_test = squares_left[0]
    if (left_test in cube1 and right_test in cube2) or (right_test in cube1 and left_test in cube2):
        for f in find_possibilities_for_cubes(cube1, cube2, squares_left[1:], max_cube2):
            yield f
        return

    if left_test in cube1 and right_test in cube1:
        for d in left_test, right_test:
            for f in find_possibilities_for_cubes(cube1, cube2 + [d], squares_left[1:], d):
                yield f
        return

    for l, r in ((left_test, right_test), (right_test, left_test)):
        if l in cube1 and r not in cube1:
            for f in find_possibilities_for_cubes(cube1, cube2 + [r], squares_left[1:], max_cube2):
                yield f


def is_same_possibility(cube1, cube2):
    assert not(9 in cube1 or 9 in cube2)
    assert (len([x for x in cube2 if x not in cube1]) <= 6 - len(cube1)) == \
           (len([x for x in cube1 if x not in cube2]) <= 6 - len(cube2))
    if cube1 == [] or cube2 == []:
        return False
    return len([x for x in cube2 if x not in cube1]) <= 6 - len(cube1)


def rate_possibility(c):
    n = 6 - len(c)
    sixes = len([x for x in c if x == 6])
    total = choose(9 + n, 9) + sixes * choose(8 + n, 8)
    return total


def find_number_of_possibilities_for_cube(cube):
    total = 0
    found = []
    while 9 in cube:
        cube[cube.index(9)] = 6
    for p in find_possibilities_for_cubes(cube):
        if all([not is_same_possibility(f, p) for f in found]):
            found.append(p)
            total += rate_possibility(p)
        else:
            for f in found:
                if is_same_possibility(f, p):
                    print f, p
    # print cube, found, total
    return total


def find_number_of_possibilities():
    found = 0
    for cube_1 in it.combinations_with_replacement(range(10), 6):
        found += find_number_of_possibilities_for_cube(list(cube_1))
    return found


def is_match(cube1, cube2):
    for cube in (cube1, cube2):
        while 9 in cube:
            cube[cube.index(9)] = 6
    for s in squares:
        if not (s[0] in cube1 and s[1] in cube2) and not (s[0] in cube2 and s[1] in cube1):
            return False
    return True


def brute_force_number_of_possibilities():
    total = 0
    for cube_1 in it.combinations(range(10), 6):
        for cube_2 in it.combinations(range(10), 6):
            if is_match(list(cube_1), list(cube_2)):
                print cube_1, cube_2
                total += 1
    return total

if __name__ == "__main__":
    print brute_force_number_of_possibilities()