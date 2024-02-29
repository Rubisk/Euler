import sys
import pytest
import numpy as np
import copy


def generate_prime_table(maximum, extend=None):
    print "Generating prime table using sieve..."
    primes = extend if extend is not None else []
    table = np.zeros(maximum)
    for p in primes:
        table[::p] = 1
        table[p] = 0
    start = min(2, max(primes))
    for n in range(start, maximum):
        if table[n] == 0:
            primes.append(n)
            table[::n] = 1
            table[n] = 0
    print "Prime table generated. Found %d primes." % len(primes)
    return primes


class TruncatablePrimeFinder(object):

    def __init__(self):
        self._primes = [2, 3, 5, 7]
        self._truncatables = []
        self._maximum = 100

    def _is_truncatable(self, n, right=False):
        string = [c for c in str(n)]
        while len(string) > 1:
            string = string[:-1] if right else string[1:]
            if not int("".join(string)) in self._primes:
                return False
            # print n, string
        # print "TRUE", n, right, string
        return True

    def find_truncatables(self, n, start_targets=None):
        print self._primes
        if start_targets is None:
            start_targets = generate_prime_table(self._maximum, copy.copy(self._primes))
            start_targets = [x for x in start_targets if x not in self._primes]
        next_targets = start_targets
        while len(self._truncatables) < n:
            start_targets = copy.copy(next_targets)
            next_targets = []
            self._primes = generate_prime_table(self._maximum, self._primes)
            for p in start_targets:
                if p not in self._primes:
                    continue
                if self._is_truncatable(p):
                    next_targets.append(p)
                    if self._is_truncatable(p, right=True) and p not in self._truncatables:
                        self._truncatables.append(p)
            self._maximum *= 10
            start_targest = copy.copy(next_targets)
            next_targets = []
            for i in start_targest:
                for c in "123456789":
                    next_targets.append(int(c + str(i)))
        return self._truncatables


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        t = TruncatablePrimeFinder()
        print sum(t.find_truncatables(11))
