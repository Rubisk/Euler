import sys
import pytest
from euler_114 import CombinationCounter


class CombinationFinder(CombinationCounter):

    def find_first_above(self, minimum, min_block_size):
        self._possible_combinations = [-1]
        self._min_block_size = min_block_size
        count = 0
        while self.get_possibilities(count) < minimum:
            count += 1
            self._possible_combinations.append(-1)
        return count


def test_find_first_above():
    cc_test = CombinationFinder()
    assert cc_test.find_first_above(1000000, 10) == 57


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        cc = CombinationFinder()
        print cc.find_first_above(int(sys.argv[-2]), int(sys.argv[-1]))
