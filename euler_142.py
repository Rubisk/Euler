import itertools as it
import sys
import math


def pair_to_xyz(a, b, c, d):
	assert b - a == d - c
	x = (b - a) / 2
	y = b - x
	z = d - x
	return x, y, z


def search(m):
	squares = [n**2 for n in range(1, m)]
	differences = {}
	best = -1
	for (a, b) in it.combinations(squares, 2):
		if ((b - a) % 2) != 0:
			continue
		if differences.get(b - a) is None:
			differences[b - a] = [(a, b)]
			continue
		for (c, d) in differences[b - a]:
			(x, y, z) = pair_to_xyz(a, b, c, d)
			if math.sqrt(y - z).is_integer() and math.sqrt(y + z).is_integer():
				if (x == y or y == z or x == z):
					continue
				total = x + y + z
				if total < best or best == -1:
					best = total
		differences[b - a].append((a, b))
	return best


if __name__ == "__main__":
	print(search(int(sys.argv[1])))