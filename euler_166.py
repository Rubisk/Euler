import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy

size = 4

total = 0
for goal in range(40):
    print(goal)
    rows = []
    for row in it.product(range(10), repeat=4):
        if sum(row) == goal:
            rows.append(row)

    double_score_table = {}
    for (row1, row2) in it.product(rows, repeat=2):
        scores = [row1[i] + row2[i] for i in range(4)]
        scores.append(row1[0] + row2[1])
        scores.append(row1[3] + row2[2])
        scores = tuple(scores)
        double_score_table[scores] = double_score_table.get(scores, 0) + 1

    for score, count in double_score_table.items():
        coscore = [goal - i for i in score]
        coscore[4], coscore[5] = coscore[5], coscore[4]
        coscore = tuple(coscore)
        total += count * double_score_table.get(coscore, 0)

    print(total)

print(total)
