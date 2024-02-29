import sys


def find_primes(n):
    i = 2
    while i < n:
        while n % i == 0:
            yield i
            n /= i
        i += 1
    if n != 1:
        yield n

if __name__ == '__main__':
    print max(find_primes(int(sys.argv[-1])))
