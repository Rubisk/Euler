import sys
import numpy as np
from euler_util import sieve_primes, is_prime, all_prime
import math
import pytest


square_additions = [1, 3, 7, 9, 13, 27]


def efficient_legendre(m, n):
	start_m = m + 0
	for i in range(1, int((n - 1) / 2)):
		m = m * start_m
		m = m % n
	if m == n - 1:
		m == -1
	return m
	# m = m % n
	# legendre = 1
	# while m % 2 == 0:
	# 	m /= 2
	# 	legendre *= (-1) ** ((n **2 - 1) / 8)
	# if (m == 1):
	# 	return legendre
	# return efficient_legendre(n, m)


def test_efficient_legendre():
	assert efficient_legendre(10, 13) == 1
	assert efficient_legendre(1001, 9907) == -1
	assert efficient_legendre(10, 13) == 1


def find_square_roots(n, p):
	if n == 0:
		yield 0
		return
	if efficient_legendre(n, p) != 1:
		return
	if p % 4 == 3:
		yield n ** ((p + 1) / 4) % p
		yield -n ** ((p + 1) / 4)  % p
		return
	q = p - 1
	s = 0
	while q % 2 == 0:
		s += 1
		q /= 2
	assert s > 1
	z = 2
	while efficient_legendre(z, p) != -1:
		z += 1

	r = n ** ((q + 1) / 2) % p
	t = n ** q % p 
	m = s
	while t % p != 1:
		i = 1
		while t ** (2 ** i) % p != 1:
			i += 1
		assert i < M
		b = c ** (2 ** (M - i - 1)) % p
		r = r * b % p
		t = t * b * b % p
		c = b * b % p
		m = i
	yield r
	yield -r


def find_all_n(maximum):
	_, small_primes = sieve_primes(150)
	mod_table = {}
	for prime in small_primes:
		possible_solutions = []

		prime_mod_zeroes = []
		for n in range(prime):
			square_n = (n % prime) ** 2
			if any([(square_n + s) % prime == 0 and (square_n + s) > prime for s in square_additions]):
				prime_mod_zeroes.append(n)
		mod_table[prime] = prime_mod_zeroes

	print("Mod tables calculated")
	print(np.prod([(prime - len(zeroes)) / prime for prime, zeroes in mod_table.items()]))

	_, small_primes = sieve_primes(maximum)
	del _
	for n in range(3, maximum):
		legit = True
		for prime, zeroes in mod_table.items():
			if n % prime in zeroes:
				legit = False
				break
		if not legit:
			continue
		square_n = n * n
		if all_prime([square_n + s for s in square_additions], small_primes):
			print(n)
			yield n

def test_find_all_n():
	pass
	# assert sum(find_all_n(1000000)) == 1242490


def test_find_square_roots():
	assert list(find_square_roots(4, 7)) == [2, 5]
	assert list(find_square_roots(10, 13)) == [6, 7]

if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	print(sum(find_all_n(int(sys.argv[-1]))))