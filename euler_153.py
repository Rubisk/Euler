import sys
import pytest
import math
import itertools as it
import numpy as np
from fractions import gcd
from euler_util import sieve_primes
from functools32 import lru_cache


# @lru_cache(maxsize=None)
def sum_all_divisors(n, d):
	divisor_count = 0
	i = 1
	stop = n + 1
	n = int(n / d)
	while i < stop:
		divisor_count += int(n / i) * i
		start = int(n / i)
		end = int(n / (i + 1) + 1)
		if end == i:
			end += 1
		i_sum = start * (start + 1) / 2 - (end) * (end - 1) / 2
		divisor_count += i_sum * i
		stop = end
		i += 1
	return int(d * divisor_count)


def sum_for_a(n, a, g=1):
	total = 0
	i = 1
	stop = math.sqrt(max(0, n / g ** 2 - a ** 2))
	while i <= stop:
		d = g ** 2 *  (a ** 2 + i ** 2)
		total += sum_all_divisors(n, d) / d * a
		start = int(1 / g * math.sqrt(max(0, (n / i) - (a * g) ** 2)))
		root = max(0, n / (i + 1) - (a * g) ** 2)
		end = int(1 / g * math.sqrt(root) + 1)
		while end <= i:
			end += 1
		if end <= start:
			total_bs = start - end + 1
			d = g ** 2 * (start ** 2 + a ** 2)
			total += sum_all_divisors(n, d) / d * a * total_bs
			stop = end - 1
		i += 1
	return total


def test_sum_all_divisors():
	assert(sum_all_divisors(3, 1) == 8)
	assert(sum_all_divisors(4, 1) == 15)
	assert(sum_all_divisors(8, 2) == 30)
	assert(sum_all_divisors(1, 1) == 1)
	assert(sum_all_divisors(2, 1) == 4)
	assert(sum_all_divisors(5, 2) == 8)


def test_sum_for_a():
	def brute_for_a(n, a, g=1):
		total = 0
		b = 1
		while g ** 2 *  (a ** 2 + b ** 2) <= n:
			d = g ** 2 * (a ** 2 + b ** 2)
			total += sum_all_divisors(n, d) / d * a
			b += 1
		return total

	assert brute_for_a(5, 1, 2) == sum_for_a(5, 1, 2)
	assert brute_for_a(68, 1, 2) == sum_for_a(68, 1, 2)
	assert brute_for_a(26, 3) == sum_for_a(26, 3)
	assert brute_for_a(100, 5) == sum_for_a(100, 5)
	assert brute_for_a(2, 1) == sum_for_a(2, 1)
	assert brute_for_a(5, 1, 1) == sum_for_a(5, 1, 1)
	assert brute_for_a(10, 1, 1) == sum_for_a(10, 1, 1)
	assert brute_for_a(20, 1, 2) == sum_for_a(20, 1, 2)
	assert brute_for_a(20, 1, 3) == sum_for_a(20, 1, 3)
	for x, y in it.product(range(150), repeat=2):
		assert brute_for_a(x, y) == sum_for_a(x, y)
		assert brute_for_a(x, y, 2) == sum_for_a(x, y, 2)
		assert brute_for_a(x, y, 3) == sum_for_a(x, y, 3)
		assert brute_for_a(x, y, 4) == sum_for_a(x, y, 4)
		assert brute_for_a(x, y, 5) == sum_for_a(x, y, 5)
		assert brute_for_a(x, y, 6) == sum_for_a(x, y, 6)

def sum_gaussian_divisors(n):
	total = 0
	a = 1
	while a ** 2 + 1 <= n:
		print(a)
		b = 1
		while b ** 2 + a ** 2 <= n:
			if gcd(a, b) > 1:
				b += 1
				continue
			d = a ** 2 + b ** 2
			total += a * sum_all_divisors(n, d) / d
			b += 1
		a += 1
	# total = 0
	# max_g = int(1 +  math.sqrt(n))
	# print(max_g)
	# _, primes = sieve_primes(max_g)
	# mus = np.ones(max_g)
	# for p in primes:
	# 	mus[::p] *= -1
	# 	mus[::p ** 2] *= 0
	# for g in range(1, max_g):
	# 	print(g)
	# 	g_total = 0
	# 	for a in range(1, 1 + 2 * int(math.sqrt(n))):
	# 		print(a)
	# 		# print(a, g, sum_for_a(n, a, g))
	# 		g_total += g * sum_for_a(n, a, g)
	# 	# print(g_total)
	# 	total += mus[g] * g_total
	total *= 2
	total += sum_all_divisors(n, 1)
	return total


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		print(int(sum_gaussian_divisors(int(sys.argv[-1]))))