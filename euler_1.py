import sys

def calculate_sum(max):
	threes = (max - 1) / 3
	fives = (max - 1) / 5
	fifteens = (max - 1) / 15
	
	threes = 3 * (threes * (threes + 1)) / 2
	fives = 5 * (fives * (fives + 1)) / 2
	fifteens = 15 * (fifteens * (fifteens + 1)) / 2
	return threes + fives - fifteens

	
if __name__ == '__main__':
    print calculate_sum(int(sys.argv[-1]))