import itertools as it
import sys
import pytest
import numpy as np
import copy

GUESS_DEPTH = 3


class UnSolveableException(Exception):
    pass


class SudokuSolver(object):

    def __init__(self):
        self.sudoku = []
        self.possibilities = []

    def load_sudoku(self, sudoku):
        if type(sudoku) == str:
            sudoku = sudoku.splitlines()
        self.sudoku = [[int(c) for c in l if c in "0123456789"]
                       for l in sudoku]
        self._recalculate_possibilities()

    def set_sudoku(self, sudoku, possibilities):
        self.sudoku = copy.deepcopy(sudoku)
        self.possibilities = copy.deepcopy(possibilities)

    def solve(self, depth=GUESS_DEPTH):
        while self._check_possibilities() or self._check_numbers():
            pass
        if any([0 in r for r in self.sudoku]):
            if depth == 0:
                raise UnSolveableException
            child_solver = SudokuSolver()
            for x, y in self.find_spots_with_n_possibilities(2):
                for p in range(0, 9):
                    if self.possibilities[x][y][p] == 0:
                        continue
                    child_solver.set_sudoku(self.sudoku, self.possibilities)
                    child_solver.set(x, y, p + 1)
                    try:
                        return child_solver.solve(depth - 1)
                    except UnSolveableException:
                        pass
        else:
            return sum([self.sudoku[0][i] * 10 ** (2 - i) for i in range(3)])
        raise UnSolveableException()

    def find_spots_with_n_possibilities(self, possibilities):
        for x, y in it.product(range(9), repeat=2):
            if sum(self.possibilities[x][y]) == possibilities:
                yield x, y
            elif sum(self.possibilities[x][y]) == 0 and self.sudoku[x][y] == 0:
                raise UnSolveableException

    @staticmethod
    def _get_friend_pos_iter(x, y):
        """
        Yields all friend positions with a specific spot.
        Useful for iterating over all places that have to match with a spot
        """
        for i in range(9):
            yield x, i
            yield i, y
        square_x, square_y = x / 3, y / 3
        for dx, dy in it.product(range(3), repeat=2):
            yield 3 * square_x + dx, 3 * square_y + dy

    def _recalculate_possibilities(self):
        self.possibilities = np.ones((9, 9, 9))
        for x, y in it.product(range(9), repeat=2):
            val = self.sudoku[x][y]
            if val == 0:
                continue
            self.possibilities[x][y] = np.zeros(9)
            for friend_x, friend_y in self._get_friend_pos_iter(x, y):
                self.possibilities[friend_x][friend_y][val - 1] = 0

    def set(self, x, y, val):
        assert 0 < val < 10
        assert self.sudoku[x][y] == 0
        self.sudoku[x][y] = val
        for friend_x, friend_y in self._get_friend_pos_iter(x, y):
            self.possibilities[friend_x][friend_y][val - 1] = 0
        self.possibilities[x][y] = np.zeros(9)

    def _check_possibilities(self):
        changed = False
        for x, y in it.product(range(9), repeat=2):
            s = sum(self.possibilities[x][y])
            if s == 0 and self.sudoku[x][y] == 0:
                raise UnSolveableException
            elif s == 1:
                changed = True
                self.set(x, y, np.where(self.possibilities[x][y] == 1)[0][0] + 1)
        return changed

    def _check_numbers(self):
        return self._check_row_numbers() or self._check_column_numbers() or self._check_square_numbers()

    def _check_row_numbers(self):
        changed = False
        for x in range(9):
            row = self.possibilities[x]
            sums = np.zeros(9)
            for spot in row:
                sums += spot
            for n in np.where(sums == 1)[0]:
                for y in range(9):
                    if row[y][n] == 1:
                        self.set(x, y, n + 1)
                        changed = True
        return changed

    def _check_column_numbers(self):
        changed = False
        for y in range(9):
            col = [p[y] for p in self.possibilities]
            sums = np.zeros(9)
            for spot in col:
                sums += spot
            for n in np.where(sums == 1)[0]:
                for x in range(9):
                    if col[x][n] == 1:
                        self.set(x, y, n + 1)
                        changed = True
        return changed

    def _check_square_numbers(self):
        changed = False
        for cx, cy in it.product((0, 3, 6), repeat=2):
            square = [[self.possibilities[cx + dy][cy + dx] for dx in range(3)]
                      for dy in range(3)]
            sums = np.zeros(9)
            for row in square:
                for spot in row:
                    sums += spot
            for n in range(9):
                if sums[n] != 1:
                    continue
                for dx, dy in it.product(range(3), repeat=2):
                    if square[dx][dy][n] == 1:
                        self.set(cx + dx, cy + dy, n + 1)
                        changed = True
        return changed


def test_sudoku_solver():
    string = open("euler_96_test.txt").read().splitlines()
    s = SudokuSolver()
    s.load_sudoku(string[0:9])
    assert s.solve() == 483

    s.load_sudoku(string[10:])
    print s.solve()


def find_sudoku_sum(path):
    with open(path) as f:
        string = f.read()
    sudoku_string = string.splitlines()
    solver = SudokuSolver()

    total = 0
    while len(sudoku_string) > 0:
        solver.main = True
        solver.load_sudoku(sudoku_string[1:10])
        sudoku_string = sudoku_string[10:]
        total += solver.solve()
    return total

if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print find_sudoku_sum(sys.argv[-1])
