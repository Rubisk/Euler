import sys
import pytest


def evaluate(polynomial, value):
    l = len(polynomial)
    return sum([value ** j * polynomial[l - j - 1] for j in range(l)])


def find_sum_of_incorrect_terms(polynomial):
    grade = len(polynomial) - 1
    matrix = [[0 for _ in range(grade)]
              for _ in range(grade)]
    matrix[0] = [evaluate(polynomial, i) for i in range(1, grade + 1)]
    for depth in range(1, grade):
        for t in range(grade - depth):
            matrix[depth][depth + t] = matrix[depth - 1][depth + t] - matrix[depth - 1][depth + t - 1]
    return sum([sum(row) for row in matrix])


def test_find_first_incorrect_term():
    assert find_sum_of_incorrect_terms([1, 0, 0, 0]) == 74

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        p = [int(x) for x in sys.argv[1:]]
        print find_sum_of_incorrect_terms(p)
