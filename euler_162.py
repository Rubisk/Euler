import sys
import pytest


def to_hex_string(n):
	hex_chars = "0123456789ABCDEF"
	string = ""
	while n > 0:
		string = hex_chars[n % 16] + string
		n = n // 16
	return string


def count_containing_0_1_a(digits):
	count = 15 * 16 ** (digits - 1)

	count -= 14 * 15 ** (digits - 1)  # numbers without a 1
	count -= 14 * 15 ** (digits - 1)  # numbers without a A
	count -= 15 * 15 ** (digits - 1)  # numbers without a 0

	count += 14 * 14 ** (digits - 1)  # numbers without a 0, 1
	count += 14 * 14 ** (digits - 1)  # numbers without a 0, A
	count += 13 * 14 ** (digits - 1)  # numbers without a 1, A

	count -= 13 * 13 ** (digits - 1)  # numbers without a 0, 1, A

	if digits > 1:
		count += count_containing_0_1_a(digits - 1)

	return count


def test_to_hex_string():
	assert to_hex_string(1) == "1"
	assert to_hex_string(15) == "F"
	assert to_hex_string(16) == "10"
	assert to_hex_string(256) == "100"
	assert to_hex_string(175) == "AF"


def test_count_containing_0_1_a():
	count = 0
	for n in range(16 ** 5):
		s = to_hex_string(n)
		if "0" in s and "1" in s and "A" in s:
			count += 1
	assert count == count_containing_0_1_a(5)


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main([__file__])
    else:
    	print(count_containing_0_1_a(int(sys.argv[-1])))
    	print(to_hex_string(count_containing_0_1_a(int(sys.argv[-1]))))