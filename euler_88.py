import sys
import pytest
import copy
import numpy as np


def find_minimal_som_product_numbers(k):
    k_array = [0 for _ in range(k + 1)]
    queue = [(4, 4, [2, 2], 2)]
    n = 2
    while len(queue) > 0:
        new_queue = []
        for set_sum, set_product, set, last_increase in queue:
            if set_product - set_sum + len(set) > k:
                continue
            test_k = set_product - set_sum + len(set)
            if k_array[test_k] == 0 or set_product < k_array[test_k]:
                k_array[test_k] = set_product
            for i in range(last_increase):
                if i == len(set) - 1 or set[i] < set[i + 1]:
                    set[i] += 1
                    new_queue.append((set_sum + 1, set_product / (set[i] - 1) * set[i], copy.copy(set), i + 1))
                    set[i] -= 1
        n += 1
        if 2 ** n - n <= k:
            new_queue.append((2 * n, 2 ** n, [2 for _ in range(n)], n))
        queue = new_queue
    return sum(np.unique(k_array))


def test_find_mimimal_som_product_numbers():
    assert find_minimal_som_product_numbers(6) == 30
    assert find_minimal_som_product_numbers(12) == 61


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_minimal_som_product_numbers(int(sys.argv[-1]))
