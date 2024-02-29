import sys
import pytest
import time


class SummationFinder(object):
    _cache = {}

    def find_number_of_summations(self, n, max_value=-1):
        if self._cache.get(n) is None:
            self._cache[n] = {}
        if self._cache[n].get(max_value) is None:
            self._cache[n][max_value] = self._compute_number_of_summations(n, max_value)
        return self._cache[n][max_value]

    def _compute_number_of_summations(self, n, max_value=-1):
        if n in (1, 0) or max_value == 1:
            return 1
        total = 0
        max_value = n if max_value == -1 else min(max_value + 1, n + 1)
        for i in range(1, max_value):
            total += self.find_number_of_summations(n - i, i)
        return total


def test_find_number_of_summations():
    f = SummationFinder()
    assert f.find_number_of_summations(5) == 6
    assert f.find_number_of_summations(6) == 10
    t = time.time()
    f.find_number_of_summations(100)
    assert time.time() - t < 0.1


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        try:
            finder = SummationFinder()
            print finder.find_number_of_summations(int(sys.argv[-1]))
        except ValueError:
            print "Script invocation: [N]"
            print "[N]: Number to find summations for (integer)."
