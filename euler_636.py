import pytest
import sys
import itertools as it
import numpy as np


limit = 26

two_ways = [int(n / 2) + 1 for n in range(limit + 1)]
three_ways = np.zeros(limit + 1, dtype=np.uint64)
four_ways = np.zeros(limit + 1, dtype=np.uint64)

three_ways[0] = 1
four_ways[0] = 1

cached_sums = {}


def find_sums(pattern):
    if pattern in cached_sums.keys():
        return cached_sums[pattern]
    pattern_sums = np.zeros(limit + 1, dtype=np.uint64)
    pattern_sums[0] = 1

    last = pattern[-1]
    if len(pattern) > 1:
        short_patterns = find_sums(pattern[:-1])
        for n in range(1, limit + 1):
            total = 0
            i = 0
            while i * last <= n:
                total += short_patterns[n - (i * last)]
                i += 1
            pattern_sums[n] = total
    else:
        for n in range(1, limit + 1):
            pattern_sums[n] = 1 if n % last == 0 else 0
    cached_sums[pattern] = pattern_sums
    return pattern_sums


def count_sums(pattern, equal_indices):
    new_pattern = [0] if len(equal_indices) > 0 else []
    for (i, x) in enumerate(pattern):
        if i in equal_indices:
            new_pattern[0] += x
        else:
            new_pattern.append(x)
    print(new_pattern, equal_indices)
    return find_sums(tuple(new_pattern))


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
prime_counts = np.zeros(len(primes), dtype=np.uint64)

def highest_power(p):
    highest_power = 0
    i = p + 0
    while limit >= i:
        highest_power += int(limit / i)
        i *= p
    return highest_power


for (i, p) in enumerate(primes):
    prime_counts[i] = highest_power(p)


sums = np.zeros(limit + 1, dtype=np.uint64)
for (a, b, c, d) in it.product(range(40), repeat=4):
    if a == b and a + 2 * b + 3 * c + 4 * d <= limit:
        sums[a + 2 * b + 3 * c + 4 * d] += 1

four_ways = find_sums((1, 2, 3, 4))

result = 0
for size in range(5):
    if size == 1:
        continue
    sign = 1 if size == 0 else (-1) ** (size - 1)
    for equal_indices in it.combinations((0, 1, 2, 3), size):
        sub_result = 1
        ways = count_sums((1, 2, 3, 4), equal_indices)
        for x in prime_counts:
            sub_result *= ways[x]
        result += sub_result * sign
print(result)


# result = 1
# for x in prime_counts:
#     print(x)
#     result *= four_ways[x]
# print(result)