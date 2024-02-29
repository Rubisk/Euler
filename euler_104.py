import sys
import pytest


def fibonacci(f0, f1):
    return f0 + f1


def is_pandigital(string):
    return all([str(i) in string for i in range(1, 10)])


def find_head_pandigitals(f, s1, s2):
    sequence_tail = [(s1, 1), (s2, 1)]
    i = 2
    while True:
        power = sequence_tail[1][1] - sequence_tail[0][1]
        assert power >= 0
        s_next = f(sequence_tail[0][0], sequence_tail[1][0] * 10 ** power)
        s_next_power = max(len(str(s_next)) - 15 + sequence_tail[1][1], 1) - power
        sequence_tail.append((int(str(s_next)[:15]), s_next_power))
        sequence_tail = sequence_tail[1:]
        i += 1
        if is_pandigital(str(sequence_tail[1][0])[:9]):
            yield i


def find_tail_pandigitals(f, s1, s2):
    sequence_tail = [s1, s2]
    i = 2
    while True:
        s_next = f(sequence_tail[0], sequence_tail[1]) % 10 ** 9
        sequence_tail.append(s_next)
        sequence_tail = sequence_tail[1:]
        i += 1
        if is_pandigital(str(sequence_tail[1])[:9]):
            yield i


def test_find_head_pandigitals():
    for s in find_head_pandigitals(fibonacci, 1, 1):
        assert s == 2749
        return


def test_find_tail_pandigitals():
    for s in find_tail_pandigitals(fibonacci, 1, 1):
        assert s == 541
        return

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        head_gen = find_head_pandigitals(fibonacci, 1, 1)
        tail_gen = find_tail_pandigitals(fibonacci, 1, 1)
        tail = 1
        head = 0
        while True:
            while head < tail:
                head = head_gen.next()
            if head == tail:
                print head
            while tail < head:
                tail = tail_gen.next()
            if head == tail:
                print head
                break
