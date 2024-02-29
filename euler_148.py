import sys
import pytest
from euler_util import choose
import math

def max_power_7(n):
	i = 0
	while n % 7**(i + 1) == 0:
		i += 1
	return i

def seven_power_of_faculty(n):
	total = 0
	i = 7
	while i <= n:
		total += int(n / i)
		i *= 7
	return total

def divisible_by_seven(n, k):
	return seven_power_of_faculty(n) > (seven_power_of_faculty(k) + seven_power_of_faculty(n - k))

def sum_row_brute(n):
	total = 0
	string = ""
	for k in range(n + 1):
		total += 0 if divisible_by_seven(n, k) else 1
		string += str(1 if divisible_by_seven(n, k) else 0)
	print(string)
	return total

def sum_row(n):
	n += 1
	seven_power = 7
	while 7 * seven_power <= n:
		seven_power *= 7
	blocks = int(n / seven_power)
	while seven_power > 1:
		seven_power /= 7
		mod = n % (seven_power * 7)
		if mod == 0:
			mod = seven_power * 7
		new_block_multiplier = math.ceil(mod / seven_power)
		blocks = blocks * new_block_multiplier
		if mod >= seven_power and mod != seven_power * 7:
			blocks += int(mod / seven_power)
	return blocks

		
	# total = 0
	# k = n + 0
	# while k % 7 != 0:
	# 	total += 0 if divisible_by_seven(n, k) else 1
	# 	k -= 1
	# if k == 0:
	# 	return total
	# div_total = 0
	# for i in range(7):
	# 	if not divisible_by_seven(n - 1, i):
	# 		div_total += 1
	# print("d", n, div_total, k, sum_row(k / 7))
	# return total + sum_row(k / 7) * div_total

def sum_rows(n):
	if n == 0:
		return 0
	total = 0
	start_n = n + 0
	while n % 7 != 0:
		total += sum_row(n - 1)
		n -= 1
	total += 28 * sum_rows(int(n / 7))
	return total

def sum_rows_brute(n):
	total = 0
	for x in range(n + 1):
		total += sum_row_brute(x)
	return total

def test_sum_row():
	for x in range(400):
		assert sum_row(x) == sum_row_brute(x)

if __name__ == "__main__" :
	if "-test" in sys.argv:
		pytest.main([__file__])
	else:
		print(sum_rows(int(sys.argv[-1])))