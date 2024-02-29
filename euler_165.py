import sys
import pytest
import numpy as np
from fractions import Fraction


def intersect(first, second):
        # if min(first[0], first[2]) > max(second[0], second[2]):
        #     return False
        # if min(second[0], second[2]) > max(first[0], first[2]):
        #     return False
        # if min(first[1], first[3]) > max(second[1], second[3]):
        #     return False
        # if min(second[1], second[3]) > max(first[1], first[3]):
        #     return False
        a0, b0, a1, b1 = map(int, first)
        c0, d0, c1, d1 = map(int, second)
        m1 = a0 - a1
        m2 = c1 - c0
        m3 = b0 - b1
        m4 = d1 - d0

        # Check if lines are parallel (det 0)
        det = m1 * m4 - m2 * m3
        if det == 0:
            return False

        # Find inverse
        i1 = m4 / det
        i2 = -m2 / det
        i3 = -m3 / det
        i4 = m1 / det

        t = Fraction(m4 * (c1 - a1) - m2 * (d1 - b1), det)
        if not 0 < t < 1:
            return False
        s = Fraction(-m3 * (c1 - a1) + m1 * (d1 - b1), det)
        if not 0 < s < 1:
            return False

        # t_exact = Fraction(m4 * (c1 - a1) - m2 * (d1 - b1), det)
        point_x = t * a0 + (1 - t) * a1
        point_y = t * b0 + (1 - t) * b1
        return point_x, point_y

l1 = (27, 44, 12, 32)
l2 = (46, 53, 17, 62)
l3 = (46, 70, 22, 40)

np.seterr(all='warn')
s = np.zeros(20001, dtype=np.int64)
t = np.zeros(20001, dtype=np.int64)

s[0] = 290797
for n in range(20000):
    s[n + 1] = (s[n] * s[n]) % 50515093
    t[n + 1] = s[n + 1] % 500
print(s[5000])

segments = []
for i in range(5000):
    segments.append(tuple(t[4 * i + j + 1] for j in range(4)))

total = set()
total_list = []

count = 0
for first in segments:
    count += 1
    for second in segments:
        point = intersect(first, second)
        if point:
            total.add(point)
            total_list.append(point)

    if count % 50 == 0:
        print("%s percent done." % (count / 50))
print(len(total))
