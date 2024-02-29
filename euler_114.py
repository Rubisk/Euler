import sys
import pytest


class CombinationCounter(object):
    _possible_combinations = None
    _min_block_size = -1

    def count(self, length, min_block_size):
        self._possible_combinations = [-1 for _ in range(length + 1)]
        self._min_block_size = min_block_size
        return self.get_possibilities(length)

    def get_possibilities(self, length):
        if -1 <= length < self._min_block_size:
            return 1
        assert length > 0
        if self._possible_combinations[length] == -1:
            self._possible_combinations[length] = self._calculate_possible_combinations(length)
        return self._possible_combinations[length]

    def _calculate_possible_combinations(self, length):
        total = 0
        for i in range(self._min_block_size, length + 1):
            total += self.get_possibilities(length - i - 1)
        total += self.get_possibilities(length - 1)
        return total


def test_combination_counter():
    cc_test = CombinationCounter()
    assert cc_test.count(7, 3) == 17


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        cc = CombinationCounter()
        print cc.count(int(sys.argv[-2]), int(sys.argv[-1]))
