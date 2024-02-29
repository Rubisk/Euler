import sys
import pytest
from euler_116 import CombinationCounter


def test_combination_counter():
    cc_test = CombinationCounter()
    assert cc_test.count(5, [2, 3, 4]) + 1 == 15


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        cc = CombinationCounter()
        print cc.count(int(sys.argv[1]), [int(x) for x in sys.argv[2:]]) + 1
