import sys
import math
import fractions
import pytest


def gcd(a, b, *args):
	if len(args) > 0:
		return gcd(gcd(a, b), args[0], *args[1:])
	return fractions.gcd(a, b)

def find_pairs(max_a):
	m = 1
	while 3 * (m ** 2) - 2 * m - 1 <= 12 * max_a:
		n = 1
		while 0 < 3 * (m ** 2) - n ** 2 - 2 * n * m <= 12 * max_a:
			if gcd(n, m) == 1:
				a = 4 * n * m
				b = (3 * (m ** 2) - n ** 2 - 2 * n * m)
				d = gcd(a, b)
				if d > 12:
					print(d)
					assert False
				# if (a / d + b / d) <= max_a:
				yield a / d, b / d
			n += 1
		m += 1



def find_solutions(max_a):
	possible_cs = {}
	total = 0
	for (a, b) in find_pairs(max_a):
		k = 1
		# possible_cs.add(a)
		# possible_cs.add(b)
		while k * a <= max_a:
			if possible_cs.get(k * a) is None:
				possible_cs[k * a] = set()
			possible_cs[k * a].add(k * b)
			k += 1
	for (a, b) in find_pairs(max_a):
		k = 1
		while k * (a + b) <= max_a:
			if k * a > max_a:
				continue
			for c in possible_cs[a * k]:
				if not math.sqrt((k * a)**2 + c**2 + (k * a) * c).is_integer():
					continue
				if not math.sqrt((k * b)**2 + c**2 + (k * b) * c).is_integer():
					continue
				yield k * a, k * b, c
			k += 1

	return 0


def get_unique_solutions(max_sum):
	unique_solutions = set()
	for p, q, r in find_solutions(max_sum):
		p, q, r = sorted(map(int, [p, q, r]))
		a = math.sqrt(p**2 + q**2 + p * q)
		b = math.sqrt(p**2 + r**2 + p * r)
		c = math.sqrt(q**2 + r**2 + q * r)
		if not c - b < a <= b <= c:
			print(a, b, c)
		if not math.acos((a **2 + b ** 2 - c**2) / (2 * a * b)) / math.pi < (2 / 3):
			print(a, b, c)
		if not math.acos((a **2 + c ** 2 - b**2) / (2 * a * c)) / math.pi < (2 / 3):
			print(a, b, c)
		if not math.acos((b **2 + c ** 2 - a**2) / (2 * b * c)) / math.pi < (2 / 3):
			print(a, b, c)
		s = 1
		t = p + q + r
		while t * s <= max_sum:
			unique_solutions.add(tuple(sorted([s * p, s * q, s * r])))
			s += 1
	return unique_solutions


def test_find_pairs():
	M = 5000
	pairs = list(find_pairs(M))
	for a in range(1, M):
		for b in range(1, a):
			if a + b > M:
				continue
			if math.sqrt(a ** 2 + b ** 2 + a * b).is_integer():
				d = gcd(a, b)
				assert (a / d, b / d) in pairs


def test_find_solutions():
	M = 12000
	unique_solutions = get_unique_solutions(M)
	possible_cs = set()
	for a in range(1, M):
		for b in range(1, a):
			if math.sqrt(a ** 2 + b ** 2 + a * b).is_integer():
				for c in possible_cs:
					if not math.sqrt(a**2 + c**2 + a * c).is_integer():
						continue
					if not math.sqrt(b**2 + c**2 + b * c).is_integer():
						continue
					if a + b + c <= M:
						assert tuple(sorted([a, b, c])) in unique_solutions

				possible_cs.add(a)
				possible_cs.add(b)

if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		print(sum(set([a + b + c for a, b, c in get_unique_solutions(int(sys.argv[-1]))])))