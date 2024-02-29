import sys


def fibonacci(digits):
    f1 = 1
    f2 = 1
    i = 2
    while len(str(f2)) < digits:
        _t = f2
        f2 += f1
        f1 = _t
        i += 1
    return i


if __name__ == "__main__":
    print fibonacci(int(sys.argv[1]))
