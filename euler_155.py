from fractions import Fraction
import itertools as it
import sys


def d(n):
	i = 0
	values = []
	while i <= n:
		print(i)
		values.append(set([]))
		for j in range(0, 1 + int((i + 1) / 2)):
			if j == 0:
				values[i].add(i)
			else:
				left_options = values[j]
				right_options = values[i - j]
				for left, right in it.product(left_options, right_options):
					values[i].add(left + right)
					if left != 0 and right != 0:
						values[i].add(Fraction(1, Fraction(1, left) + Fraction(1, right)))
		i += 1
	unique_values = set()
	for value_set in values:
		unique_values |= value_set
	return len(unique_values) - 1

if __name__ == "__main__":
	print(d(int(sys.argv[-1])))