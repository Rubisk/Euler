import sys
import pytest


def find_circle(network, path=None):
    network_size = len(network)
    if path is None:
        path = [0]
    skip = [] if len(path) == 1 else [path[-2]]
    for i in range(network_size):
        checking = network[path[-1]][i]
        if checking != 0 and i not in skip:
            if i in path:
                return path[path.index(i):]
            else:
                deeper = find_circle(network, path + [i])
                if deeper is not None:
                    return deeper
    return None


def optimize_network(network):
    circle = find_circle(network)
    while circle is not None:
        size = len(circle)
        numbers = [network[circle[i]][circle[(i + 1) % size]] for i in range(size)]
        to_remove = numbers.index(max(numbers))
        x, y = circle[to_remove], circle[(to_remove + 1) % size]
        network[x][y] = 0
        network[y][x] = 0
        circle = find_circle(network)
    return network


def test_optimize_network():
    n = optimize_network(network_from_file("euler_107_test.txt"))
    assert sum([sum(l) for l in n]) / 2 == 93


def network_from_file(path):
    string = open(path).read()
    return [[int(x if x != "-" else 0) for x in line.split(",")] for line in string.splitlines()]


def analyze_network(path):
    n = network_from_file(path)
    return sum([sum(l) for l in n]) / 2 - sum([sum(l) for l in optimize_network(n)]) / 2

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print analyze_network(sys.argv[-1])
