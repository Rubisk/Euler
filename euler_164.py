import sys
import pytest
import numpy as np

length = 20
continuations = np.zeros([length - 2, 10, 10])

for l in range(length - 2):
    for i in range(10):
        for j in range(10):
            total = 0
            for k in range(10):
                if l == length and k == 0:
                    continue
                if k + i + j > 9:
                    continue
                if l != 0:
                    total += continuations[l - 1, j, k]
                else:
                    total += 1
            continuations[l, i, j] = total
    print(continuations[l])

result = 0
for i in range(1, 10):
    for j in range(10):
        result += continuations[length - 3, i, j]
print(result)