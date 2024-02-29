import sys
import pytest
import itertools as it
import math
from fractions import gcd
from euler_util import faculty, is_prime


def get_powers_to_bound(n, p):
	i = 1
	total = 0
	while p ** i <= n:
		total += int(n / (p ** i))
		i += 1
	return total


def get_ten_power_divisors(ten_power):
	i = 0
	while 2 ** i <= 10 ** ten_power:
		j = 0
		while 2 ** i * 5 ** j <= 10 ** ten_power:
			yield 2 ** i * 5 ** j
			j += 1
		i += 1

def mod_power(n, i, m):
	result = 1
	multiplier = n
	while i >= 1:
		if i % 2 == 1:
			result *= multiplier
			i -= 1
		multiplier *= multiplier
		multiplier %= m
		i = int(i / 2)
		result %= m
	return result


def invertibles_faculty(n, digits):
	f = 1
	highest_ten_power = math.ceil(math.log(n) / math.log(10))
	groups = n / (10 ** digits)
	for i in range(1, int(10 ** digits + 1)):
		if gcd(i, 10) > 1:
			continue
		for ten_divisor in get_ten_power_divisors(highest_ten_power):
			smallest_group = math.ceil(i * ten_divisor / (10.0 ** digits))
			if smallest_group > groups:
				continue
			f *= mod_power(i, int(1 + (groups - smallest_group) / ten_divisor), 10 ** digits)
		f %= 10 ** digits
	return f


def find_solution(n, digits):
	product = invertibles_faculty(n, digits)
	five_powers = get_powers_to_bound(n, 5)
	two_powers = get_powers_to_bound(n, 2)
	product *= mod_power(2, two_powers - five_powers, 10 ** digits)
	return product % 10 ** digits


def test_mod_power():
	assert mod_power(3, 2, 5) == 4
	assert mod_power(3, 3, 5) == 2
	assert mod_power(3, 4, 5) == 1
	assert mod_power(9, 2, 10) == 1

def test_find_solution():
	assert find_solution(10, 1) == 8
	assert find_solution(20, 1) == 4
	assert find_solution(20, 1) == 4


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main([__file__])
    else:
    	print(find_solution(*map(int, sys.argv[1:])))