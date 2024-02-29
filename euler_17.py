import sys
import numpy


def get_max_sum(string):
    table = numpy.array([[int(i) for i in l.split()] for l in string.splitlines()])
    height = len(table)
    for row_index in range(height - 1):
        prev_row = table[height - row_index - 1]
        row = table[height - row_index - 2]
        for i in range(len(row)):
            row[i] += max(prev_row[i], prev_row[i + 1])
    return table[0][0]


if __name__ == '__main__':
    print get_max_sum(open(sys.argv[-1]).read())
