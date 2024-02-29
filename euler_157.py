import itertools as it
import sys
import math
from fractions import Fraction, gcd


def divisors(n):
	i = 1
	while i ** 2 <= n:
		if n % i == 0:
			yield i
			if int(n / i) != i:
				yield int(n / i)
		i += 1


def find_solutions(n):
	solutions = set()
	for a, b in it.product(divisors(10 ** n), repeat=2):
		if gcd(a, b) > 1:
			continue
		if a > b:
			continue
		p = 10 ** n / a + 10 ** n / b
		for d in divisors(p):
			solutions.add((a * d, b * d))
	return len(solutions)


if __name__ == "__main__":
	max_n = int(sys.argv[-1])
	print(sum([find_solutions(n) for n in range(1, max_n + 1)]))
