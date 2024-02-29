import pytest
import sys


shapes = [
	[(0, 0), (0, 1), (0, 2)],
	[(0, 0), (1, 0), (2, 0)],
	[(0, 0), (0, 1), (1, 0)], 
	[(0, 0), (1, 1), (0, 1)],
	[(0, 0), (1, 1), (1, 0)],
	[(0, 0), (1, 0), (1, -1)],
]


def hash_board(board, n, m):
	hash_key = 0
	for j in range(m):
		i = 0
		while i < n and board[i * m + j] == 1:
			i += 1
		hash_key += i * n ** j
	return hash_key


def count_triomono_fillings(n, m):
	assert m % 3 == 0
	smaller_counts = {}
	board = [0 for _ in range(n * m)]
	x = 0
	y = 0
	total_saved = 0

	def next_empty_tile(cboard):
		tx = 0
		while tx < n:
			ty = 0
			while ty < m:
				if cboard[tx * m + ty] == 0:
					return tx, ty
				ty += 1
			tx += 1
		return n, 0

	def count_board(cboard):
		if all(cboard):
			return 1
		x, y = next_empty_tile(cboard)
		count = 0
		if smaller_counts.get(hash_board(cboard, n, m)) is not None:
			return smaller_counts[hash_board(cboard, n, m)]
		for shape in shapes:
			good_shape = True
			for c in shape:
				if not (0 <= x + c[0] < n and 0 <= y + c[1] < m):
					good_shape = False
					break
				if cboard[(x + c[0]) * m + y + c[1]] == 1:
					good_shape = False
					break
			if not good_shape:
				continue
			for c in shape:
				cboard[(x + c[0]) * m + y + c[1]] = 1
			count += count_board(cboard)
			for c in shape:
				cboard[(x + c[0]) * m + y + c[1]] = 0
		smaller_counts[hash_board(cboard, n, m)] = count
		return count

	smaller_counts[n] = count_board(board)
	return smaller_counts


def test_count_triomono_fillings():
	assert count_triomono_fillings(2, 3)[2] == 3
	assert count_triomono_fillings(3, 3)[3] == 10
	assert count_triomono_fillings(2, 9)[2] == 41


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		args = map(int, sys.argv[1:])
		print(count_triomono_fillings(*args)[args[0]])
