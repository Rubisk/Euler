import numpy as np
import sys
import pytest


def find_all_mdrs(max_n):
	solutions = np.zeros(max_n + 1)
	for n in range(1, max_n + 1):
		n_drs = n % 9
		if n_drs == 0:
			n_drs = 9
		solutions[n] = max(solutions[n], n_drs)
		i = 2
		while i * n <= max_n and i <= n:
			solutions[i * n] = max(solutions[i * n], solutions[i] + solutions[n])
			i += 1
	return solutions


def test_find_all_mdrs():
	assert find_all_mdrs(25)[24] == 11


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		bound = int(sys.argv[-1])
		mdr_table = find_all_mdrs(bound)
		print(sum(mdr_table[2:bound]))
