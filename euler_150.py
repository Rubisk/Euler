import sys
import pytest
import math
import itertools as it

def get_table(size):
	table_size = int(size * (size + 1) / 2)
	table = [0 for _ in range(table_size)]
	t = 0
	for k in range(1, table_size + 1):
		t = (615949 * t + 797807) % (2 ** 20)
		table[k - 1] = t - (2 ** 19)
	return table


def min_triangle_sum(table):
	best = 0
	prev_row_sums = [table[0]]
	for y in range(1, size):
		print(y)
		row_start = int(y * (y + 1) / 2)
		row = table[row_start:row_start + y + 1]
		row_sums = [0 for _ in range((y + 1) ** 2)]
		for start in range(y + 1):
			row_total = 0
			for end in range(start, y + 1):
				row_total += row[end]
				if start != end:
					 triangle_sum = row_total + prev_row_sums[start * (y - 1) + (end - 1)]
				else:
					triangle_sum = row_total + 0
				row_sums[start * y + end] = triangle_sum
				if triangle_sum < best:
					best = triangle_sum
		prev_row_sums = row_sums
	return best


def test_min_triangle_sum():
	triangle = [ 1,
	             2,  -3,
	             4,   5,  6,
	            -7,  -8, -9, 6]
	assert min_triangle_sum(triangle) == -13


def test_get_table():
	table = get_table(3)
	assert table[0] == 273519
	assert table[1] == -153582
	assert table[2] == 450905

if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		size =int(sys.argv[-1])
		table = get_table(size)
		print(min_triangle_sum(table))