import pytest
import sys
import math

def all_odd_digits(n):
	if (n == 0):
		return False
	while n > 0:
		if n % 2 == 0:
			return False
		n = int(n / 10)
	return True


def add_reverse(n):
	m = n + 0
	digits = []
	while m >= 1:
		digits.append(m % 10)
		m = int(m / 10)
	ten_power = 1
	for d in digits[::-1]:
		n += d * ten_power
		ten_power *= 10
	return n


def is_reversible(n):
	if (n % 10) == 0:
		return False
	return all_odd_digits(add_reverse(n))


def get_all_unique_endings(digits):
	if digits == 1:
		yield 1
		yield 9
		return
	ten_power = 10 ** (digits - 1)
	for ending in get_all_unique_endings(digits - 1):
		yield ending + 0 * ten_power
		yield ending + 9 * ten_power


def get_all_valid_n(digits):
	end_digits = int(digits / 2)
	for ending in get_all_unique_endings(end_digits):
		end_zeros = []
		for i in range(end_digits):
			if (i < len(str(ending)) and str(ending)[-i - 1] == "9"):
				end_zeros.append(i)
		for start in range(10**(digits - end_digits - 1), 10**(digits - end_digits)):
			good = True
			for i in end_zeros:
				if (str(start)[i] == "0"):
					good = False
			if good:
				yield start * 10**end_digits + ending

def get_number_of_cosolutions(n):
	string = str(n)
	cosolutions = 1
	for i in range(int(len(string) / 2)):
		two_sum = int(string[i]) + int(string[-i - 1])
		total = min(19 - two_sum, two_sum + 1)
		if i == 0:
			if two_sum <= 9:
				total -= 2
		cosolutions *= total
	return cosolutions

def test_is_reversible():
	assert(add_reverse(36) == 99)
	assert(is_reversible(36))
	assert(is_reversible(63))
	assert(not is_reversible(998))
	assert(not is_reversible(500))
	assert(not is_reversible(501))
	assert(not is_reversible(3))
	assert(is_reversible(904))


def test_find_all_valid_n():
	digits = 4
	valid_n = [add_reverse(n) for n in get_all_valid_n(4)]
	print(valid_n)
	for n in range(10 ** (digits - 1), 10 ** digits):
		if is_reversible(n):
			assert add_reverse(n) in valid_n


if __name__ == "__main__":
	if "-test" in sys.argv:
		pytest.main([__file__])
	max_digits = int(sys.argv[1])
	total = 0
	for digits in range(2, max_digits + 1):
		for n in get_all_valid_n(digits):
			if is_reversible(n):
				total += get_number_of_cosolutions(n)
	print(total)