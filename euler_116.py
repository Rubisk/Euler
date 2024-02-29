import sys
import pytest


class CombinationCounter(object):
    _possible_combinations = None
    _block_sizes = None

    def count(self, length, block_sizes=None):
        self._possible_combinations = [-1 for _ in range(length + 1)]
        if block_sizes is None:
            block_sizes = []
        self._block_sizes = block_sizes
        self.get_possibilities(length)
        return self.get_possibilities(length) - 1

    def get_possibilities(self, length):
        if -1 <= length < min(self._block_sizes):
            return 1
        assert length > 0
        if self._possible_combinations[length] == -1:
            self._possible_combinations[length] = self._calculate_possible_combinations(length)
        return self._possible_combinations[length]

    def _calculate_possible_combinations(self, length):
        total = 0
        for i in self._block_sizes:
            if length >= i:
                total += self.get_possibilities(length - i)
        total += self.get_possibilities(length - 1)
        return total


def test_combination_counter():
    cc_test = CombinationCounter()
    assert cc_test.count(5, [2]) == 7
    assert cc_test.count(5, [3]) == 3
    assert cc_test.count(5, [4]) == 2


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        cc = CombinationCounter()
        print sum([cc.count(int(sys.argv[1]), [int(x)]) for x in sys.argv[2:]])
