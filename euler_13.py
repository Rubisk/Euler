import sys


def get_sum_of_first_digits(digits, string):
    lines = string.splitlines()
    return str(sum([int(x) for x in lines]))[:digits]


if __name__ == '__main__':
    print get_sum_of_first_digits(int(sys.argv[-2]),
                                  open(sys.argv[-1]).read())

