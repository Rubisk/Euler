import sys
import pytest
import numpy as np
from fractions import Fraction
import itertools as it
import copy
import collections


def generate_ulam_up_to_limit(head, limit):
    sequence = head
    array = np.zeros(limit + 2)
    for x in head:
        array[x] = 1

    for x, y in it.combinations(head, 2):
        array[x + y] = 1

    n = max(head)
    while n < limit:
        n += 1
        if array[n] == 1:
            for x in sequence:
                if x + n < limit:
                    array[x + n] += 1
            sequence.append(n)
    return sequence



def generate_ulam_fast(head, size):
    if len(head) < min(100, size):
        head = generate_ulam_up_to_limit(head, 100)
    sequence = head
    evens = []

    for x in head:
        if x % 2 == 0:
            evens.append(x)
        if len(evens) >= 2:
            break

    result = [0 for _ in range(size)]
    index = 0
    for x in head:
        result[index] = x
        index += 1

    n = result[index - 1]

    buffer_size = int(max(evens) / 2) + 1
    assert n % 2 == 1
    while index < size:
        n += 2
        tail = result[max(index-buffer_size, 0):index]
        if (n - evens[0] in tail) ^ (n - evens[1] in tail):
            result[index] = n
            index += 1
            if index % 10000 == 0:
                print(index, len(tail))
    return result


def bruteforce_sequence(head, length):
    sequence = head
    n = max(sequence)
    while len(sequence) < length:
        n += 1
        count = 0
        for x in sequence:
            if n - x in sequence:
                count += 1
        if count == 2:
            sequence.append(n)
    return sequence


def find_period_and_start(sequence):
    n = 1
    period = 0
    while n < len(sequence) / 3:
        score = 0
        for i in range(1, n + 1):
            j = 0
            while len(sequence) -i - j * n >= 0 and sequence[-i - j * n] == sequence[-i]:
                j += 1
            score += (j / len(sequence))
        # print(n, score)
        if score > 0.8:
            period = n
            break
        n += 1
    if period == 0:
        raise Exception("No repetition")

    start = 0
    while any([sequence[start + i] != sequence[start + i + period] for i in range(period)]):
        start += 1
    return period, start


def find_period_and_start_fast(sequence):

    repeating_sequence = sequence[int(len(sequence) / 3):]
    counter = collections.Counter(repeating_sequence)
    best_score = len(sequence)
    best = 0

    for (number, count) in counter.items():
        if count < best_score:
            best = number
            best_score = count
    
    appearances = [i for (i, x) in enumerate(repeating_sequence) if x == best]

    periods = [x - y for (x, y) in it.product(appearances, repeat=2) if x > y]
    # assert not any([p % min(periods) != 0 for p in periods])

    period = min(periods)
    # for period in periods:
    #     good_period = True
    #     for i in range(1, period + 1):
    #         if sequence[-i] != sequence[-i - period]:
    #             good_period = False
    #             break
    #     if not good_period:
    #         continue
    start = 0
    while any([sequence[start + i] != sequence[start + i + period] for i in range(period)]):
        start += 1
    return period, start
    # return (-1, -1)


def sum_repeating_increment_sequence(head, repeating_increments, period, terms):
    print("START")
    assert period == len(repeating_increments)
    total = sum(head)
    start_n = max(head)
    terms -= len(head)

    full_sums = int(terms / period)
    # increment_sum = sum(sum(repeating_increments[:i + 1]) for i in range(period))
    fast_increment_sum = [0 for _ in range(period)]
    fast_increment_sum[0] = repeating_increments[0]
    for i in range(1, period):
        fast_increment_sum[i] = fast_increment_sum[i - 1] + repeating_increments[i]
    increment_sum = sum(fast_increment_sum)
    big_increment = sum(repeating_increments)

    half_period = int(period / 2)
    total += full_sums * (period * start_n + increment_sum) + full_sums * (full_sums - 1) * big_increment * half_period

    leftovers = terms % period
    last_n_start = start_n + full_sums * big_increment

    total += sum([last_n_start + fast_increment_sum[i] for i in range(leftovers)])

    return total


answer = 0

for n in range(2, 11):
    limit = 2 ** (2 * n) * 5
    prev_sequence = [2, 2 * n + 1]
    print(n, limit)
    print("GENERATING")
    sequence = generate_ulam_fast(prev_sequence, limit)
    print("SEARCHING")
    diff_sequence = [sequence[x] - sequence[x - 1] for x in range(len(sequence))]
    period, start = find_period_and_start_fast(diff_sequence)

    answer += sum_repeating_increment_sequence(sequence[:start], diff_sequence[start:start + period], period, 10**11) - sum_repeating_increment_sequence(sequence[:start], diff_sequence[start:start + period], period, 10**11 - 1)

print(answer)