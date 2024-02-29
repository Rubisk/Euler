import sys
import pytest
import itertools as it


def compute_efficiencies(maximum):
    found = [-1 for _ in range(maximum + 1)]
    queue = [{1}]
    efficiency = 0
    found[1] = 0
    checked = [{1}]
    while -1 in found[1:]:
        efficiency += 1
        new_queue = []
        count = 0
        for made_set in queue:
            count += 1
            for one, two in it.product(made_set, repeat=2):
                number = one + two
                if number > maximum:
                    continue
                if number not in made_set and made_set.union({number}) not in checked:
                    new_queue.append(made_set.union({number}))
                    checked.append(made_set.union({number}))
                    if found[number] == -1:
                        found[number] = [efficiency, made_set.union({number})]
        queue = new_queue
        print len(queue), len(checked)
    for i in range(1, maximum + 1):
        print i, found[i]
    return found


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print compute_efficiencies(int(sys.argv[-1]))
