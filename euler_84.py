import sys
import pytest

GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
R1 = 5
U1 = 12
U2 = 28


def get_squares_with_chances(land_square):
    if land_square in (2, 17, 33):
        yield land_square, 14.0 / 16.0
        yield GO, 1.0 / 16.0
        yield JAIL, 1.0 / 16.0
    elif land_square in (7, 22, 36):
        yield land_square, 3.0 / 8.0
        yield GO, 1.0 / 16.0
        yield JAIL, 1.0 / 16.0
        yield C1, 1.0 / 16.0
        yield E3, 1.0 / 16.0
        yield H2, 1.0 / 16.0
        yield R1, 1.0 / 16.0
        yield (land_square + 5) / 10 * 10 + 5, 2.0 / 16.0
        yield U2 if U1 < land_square < U2 else U2, 1.0 / 16.0
        yield land_square - 3, 1.0 / 16.0
    elif land_square == 30:
        yield JAIL, 1.0
    else:
        yield land_square, 1.0


def get_most_popular_monopoly_squares(dice_sides, n):
    board = [0.0 for _ in range(40)]
    board[0] = 1
    for _ in range(1000):
        new_board = [0.0 for __ in range(40)]
        for start_square in range(40):
            chance_sum = 0
            start_value = board[start_square] * (1 - 1.0 / (dice_sides ** 3))
            for throw in range(2, 2 * dice_sides + 1):
                chance = (dice_sides - abs(dice_sides + 1.0 - throw)) / (dice_sides ** 2.0)
                chance_sum += chance
                land_square = (start_square + throw) % 40
                for square, square_chance in get_squares_with_chances(land_square):
                    new_board[square % 40] += start_value * chance * square_chance
            assert chance_sum == 1
            new_board[JAIL] += board[start_square] / (dice_sides ** 3.0)
        assert 0.99999 < sum(new_board) < 1.000001  # Stupid floating points
        board = new_board
    return list(reversed([board.index(i) for i in sorted(board)[-n:]]))


def test_get_most_popular_monopoly_squares():
    assert get_most_popular_monopoly_squares(6, 3) == [10, 24, 0]


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print get_most_popular_monopoly_squares(int(sys.argv[-2]), int(sys.argv[-1]))
