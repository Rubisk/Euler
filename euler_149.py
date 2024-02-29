import sys
import pytest
import math
from functools import lru_cache

def update_sum_end_point(end_point, number_list, best_sums):
	if (end_point == 0):
		best_sums[end_point] = number_list[0]
	elif number_list[end_point] > number_list[end_point] + best_sums[end_point - 1]:
		best_sums[end_point] = number_list[end_point]
	else:
		best_sums[end_point] = best_sums[end_point - 1] + number_list[end_point]
	return best_sums

def get_maximum_sum(number_list):
	max_sum = 0
	best_sums = [0 for _ in number_list]
	for end_point in range(len(number_list)):
		best_sums = update_sum_end_point(end_point, number_list, best_sums)
		max_sum = max(max_sum, best_sums[end_point])
	return max_sum


def test_get_maximum_sum():
	assert get_maximum_sum([-2, 5, 3, 2]) == 10
	assert get_maximum_sum([9, -6, 5, 1]) == 9
	assert get_maximum_sum([3, 2, 7, 3]) == 15
	assert get_maximum_sum([-1, 8, -4, 8]) == 12
	assert get_maximum_sum([-1, 8, 4, -6]) == 12
	assert get_maximum_sum([-1, -3, -2, -6]) == 0
	assert get_maximum_sum([5, -3, 1, -2, 5]) == 6


def get_table(size):
	table = [0 for _ in range(size * size)]
	def s_(k):
		if 1 <= k <= 55:
			return (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000 - 500000
		else:
			return (table[k - 25]+ table[k - 56] + 1000000) % 1000000 - 500000


	print("GENERATING TABLE")
	for k in range(size * size):
		table[k] = s_(k + 1)
	print("DONE")
	return table


def test_s():
	table = get_table(20)
	assert table[9] == -393027
	assert table[99] == 86613


def find_optimal_sum(table):
	size = int(math.sqrt(len(table)))
	optimal = 0
	for n in range(size):
		print(n)

		row = table[n * size:(n + 1) * size]
		optimal = max(optimal, get_maximum_sum(row))
		column = table[n + 1:size ** 2 + n + 1:size]
		optimal = max(optimal, get_maximum_sum(column))

		diagonal_1 = table[n:n * size + 1:size - 1]
		optimal = max(optimal, get_maximum_sum(diagonal_1))
		diagonal_2 = table[n:(size - n + 1) * size:size + 1]
		optimal = max(optimal, get_maximum_sum(diagonal_2))
		diagonal_3 = table[size * size - (n + 1):size ** 2 - size * (n + 1):-(size - 1)]
		optimal = max(optimal, get_maximum_sum(diagonal_3))
		if n > 0:
			diagonal_4 = table[size * size - (n + 1):size * n - 1:-(size + 1)]
		else:
			diagonal_4 = table[size * size - (n + 1)::-(size + 1)]
		optimal = max(optimal, get_maximum_sum(diagonal_4))
	return optimal


def test_find_optimal_sum():
	table = [-2,  5,  3,  2,
			  9, -6,  5,  1,
			  3,  2,  7,  3,
			 -1,  8, -4,  8]
	assert find_optimal_sum(table) == 16

	table2 = [11, 16, -8,  -9,  10,   7,
	           3,  8,  0,  -9,  -8,  -6,
	          -4, -3, -2,  -8, -10, -20,
	           8,  6, 10, -20,   7,   3,
	           1,  2,  7,   8,   6,  10,
	          -4,  2, -3,   2,  -8,   7]
	assert find_optimal_sum(table2) == 34


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		print(find_optimal_sum(get_table(int(sys.argv[-1]))))