import itertools as it
import random
import sys
import math
import random


def highest_power(p, n):
	highest_power = 0
	i = p + 0
	while n >= i:
		highest_power += int(n / i)
		i *= p
	return highest_power


def power_choose(n, k, p):
	return highest_power(p, n) - highest_power(p, k) - highest_power(p, n - k)

def search_row(n, max_5_power, max_2_power):
	total = 0
	for a in range(n + 1):
		b = n - a
		if highest_power(a, 2) + highest_power(b, 2) <= max_2_power:
			if highest_power(a, 5) + highest_power(b, 5) <= max_5_power:
				total += 1
	return total


def is_multiple(n, a, b, c, prime_powers):
	assert a + b + c == n
	for prime, power in prime_powers.items():
		if not highest_power(prime, n) - highest_power(prime, a) - highest_power(prime, b) - highest_power(prime, c) >= power:
			return False
	return True


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		total = 0
		count = 0
		streak = 0
		best = 200000
		while True:
			x = random.randint(1, 200000)
			row = ""
			a = 200000 - x 
			for b in range(200000 - a + 1):
				 c = 200000 - b - a
				 if highest_power(5, 200000) - highest_power(5, a) - highest_power(5, b) - highest_power(5, c) >= 12:
				 	row += "1"
				 else:
				 	row += "0"
			print(row)
