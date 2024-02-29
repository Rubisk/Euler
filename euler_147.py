import sys
import pytest
from itertools import combinations_with_replacement, product
from euler_util import choose
import functools
import math


def in_cross_grid(n, m, x, y):
	if not 1 <= x < n + m - 1:
		return False
	if not (m - 0.5) - abs(m - 0.5 - x) > y:
		return False
	if not abs(n - 0.5 - x) - (n - 0.5) <= y:
		return False
	return True

def tiles_in_grid(n, m):
	for x in range(1, n + m - 1):
		for y in range(math.floor(abs(n - 0.5 - x) - (n - 0.5)), 
			           math.ceil((m - 0.5) - abs(m - 0.5 - x))):
			yield x, y


def new_tiles_on_m_increment(n, m):
	pos = [m - 1, m - 2]
	yield pos
	while pos[0] < n + m - 2:
		pos[0] += 1
		yield pos
		pos[1] -= 1
		yield pos

@functools.lru_cache(maxsize=None)
def get_cross_tiles(n, m):
	if n == 1 or m == 1:
		return (n - 1) + (m - 1)
	if n > m:
		return get_cross_tiles(m, n)
	elif m - n > 1:
		return get_cross_tiles(n, m - 1) + get_cross_tiles(n, n + 1) - get_cross_tiles(n, n)
	else:
		total = get_cross_tiles(n, m - 1)
		new_tiles_done = []
		for x, y in new_tiles_on_m_increment(n, m):
			for a, b in tiles_in_grid(n, m):
				if (a, b) in new_tiles_done or (a, y) in new_tiles_done or (x, b) in new_tiles_done:
					continue
				if not in_cross_grid(n, m, a, y):
					continue
				if not in_cross_grid(n, m, x, b):
					continue
				total += 1
			new_tiles_done.append((x, y))
		return total


def brute_force_cross_tiles(n, m):
	total = 0
	for ((x1, y1), (x2, y2)) in product(tiles_in_grid(n, m), repeat=2):
		if x1 > x2 or y1 > y2:
			continue
		if in_cross_grid(n, m, x1, y2) and in_cross_grid(n, m, x2, y1):
			total += 1
	return total


def get_total_tiles(n, m):
	upright = int(n * m * (n + 1) * (m + 1) / 4)
	return get_cross_tiles(n, m) + upright


def sum_total_tiles(n, m):
	total = 0
	for a in range(1, n + 1):
		for b in range(1, m + 1):
			total += get_total_tiles(a, b)
	return total

def test_get_cross_grid():
	for n, m in product(range(1, 10), repeat=2):
		assert brute_force_cross_tiles(n, m) == get_cross_tiles(n, m)

if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		x, y = int(sys.argv[-2]), int(sys.argv[-1])
		print(sum_total_tiles(x, y))