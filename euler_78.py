import sys
import pytest


class SummationFinder(object):
    _cache = [1, 1]
    _divisor = 1
    _i_cache = [0]
    _j_cache = [0]

    def find_first_divisible_by(self, divisor):
        n = 2
        self._divisor = divisor
        while self.find_number_of_partitions(n) % divisor != 0:
            n += 1
        return n

    def find_number_of_partitions(self, n):
        if n < 0:
            return 0
        if len(self._cache) <= n:
            assert len(self._cache) == n
            self._cache.append(self._calculate_number_of_partitions(n))
        return self._cache[n]

    def _calculate_number_of_partitions(self, n):
        k = 1
        total = 0
        i, j = 1, 1
        while k <= n and (i <= n or j <= n):
            if k >= len(self._i_cache):
                self._i_cache.append(k * (3 * k - 1) / 2)
            if k >= len(self._j_cache):
                self._j_cache.append(k * (3 * k + 1) / 2)
            i = self._i_cache[k]
            j = self._j_cache[k]
            one = self.find_number_of_partitions(n - i)
            two = self.find_number_of_partitions(n - j)
            total += (-1) ** (k + 1) * (one + two)
            k += 1
        return total % self._divisor


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        try:
            finder = SummationFinder()
            print finder.find_first_divisible_by(int(sys.argv[-1]))
        except ValueError:
            print "Script invocation: [N]"
            print "[N]: Number to find summations for (integer)."
