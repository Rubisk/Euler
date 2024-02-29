from euler_util import choose, faculty
import pytest
import sys


def find_number_of_solutions(n, l):
	solutions = 0
	for i in range(2, l + 1):
		first_size = i - 1
		second_size = l + 1 - i
		solutions += choose(n, first_size) * choose(n - first_size, second_size)
		solutions -= choose(n, l)
	return solutions


def test_find_number_of_solutions():
	assert find_number_of_solutions(26, 3) == 10400

if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		for j in range(1, 27):
			print(find_number_of_solutions(26, j))
