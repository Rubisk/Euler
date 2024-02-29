import collections
import sys
import pytest


HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

DIAMONDS = 0
CLUBS = 1
SPACES = 2
HEARTS = 3

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def string_to_hand(string):
    cards = string.split(" ")
    hand = []
    for card in cards:
        if len(card) == 0:
            continue
        hand.append((VALUES.index(card[0]), card[1]))
    assert len(hand) == 5
    return hand


def get_scores(counts):
    scores = {i: [] for i in range(1, 5)}
    for k in counts.keys():
        scores[counts[k]].append(k)
    for i in range(1, 5):
        scores[i] = sorted(scores[i], reverse=True)
    return scores


def rate_hand(hand):
    colors = [card[1] for card in hand]
    values = sorted([card[0] for card in hand])
    flush = True
    straight = True

    counts = collections.Counter(values)
    scores = get_scores(counts)

    for i in range(1, len(colors)):
        flush &= (colors[i] == colors[0])
        straight &= (values[i] == values[i - 1] + 1)
    if straight and flush:
        if max(values) == 12:
            assert min(values) == 8
            return ROYAL_FLUSH, scores
        return STRAIGHT_FLUSH, scores

    if 4 in counts.values():
        return FOUR_OF_A_KIND, scores

    if 3 in counts.values() and 2 in counts.values():
        return FULL_HOUSE, scores

    if flush:
        return FLUSH, scores
    if straight:
        return STRAIGHT, scores

    if 3 in counts.values():
        return THREE_OF_A_KIND, scores
    if 2 in counts.values():
        if len(counts.values()) == 3:
            return TWO_PAIRS, scores
        return ONE_PAIR, scores
    return HIGH_CARD, scores


def compare_hands(left, right):
    left, right = string_to_hand(left), string_to_hand(right)
    left, right = rate_hand(left), rate_hand(right)
    if left[0] > right[0]:
        return 1
    if left[0] < right[0]:
        return 0
    for i in reversed(range(1, 5)):
        for j in range(len(left[1][i])):
            if left[1][i][j] > right[1][i][j]:
                return 1
            if left[1][i][j] < right[1][i][j]:
                return 0
    assert False


def evaluate_file(string):
    f = open(string)
    for line in f.readlines():
        line = line.split(" ")
        yield compare_hands(" ".join(line[:5]), " ".join(line[5:]))
    f.close()


def test_rate_hands():
    assert rate_hand(string_to_hand("6D 5H 7H 8D 9H")) == (STRAIGHT, {1: [7, 6, 5, 4, 3], 2: [], 3: [], 4:[]})
    assert rate_hand(string_to_hand("5H 6H 7H 8H 9H"))[0] == STRAIGHT_FLUSH
    assert rate_hand(string_to_hand("4H 6H 7H 8H 9H"))[0] == FLUSH
    assert rate_hand(string_to_hand("5D 5D 5H 8H 9H"))[0] == THREE_OF_A_KIND
    assert rate_hand(string_to_hand("5D 5D 4H 4H 9H")) == (TWO_PAIRS, {1: [7], 2: [3, 2], 3: [], 4: []})
    assert rate_hand(string_to_hand("TH AH QH JH KH"))[0] == ROYAL_FLUSH
    assert rate_hand(string_to_hand("TH KD QH JH 2H"))[0] == HIGH_CARD
    assert rate_hand(string_to_hand("TH TD QH JH 2H"))[0] == ONE_PAIR
    assert rate_hand(string_to_hand("TH QD TH JH 2H")) == (ONE_PAIR, {1: [10, 9, 0], 2: [8], 3: [], 4: []})
    assert rate_hand(string_to_hand("TH TH TH TH 2H")) == (FOUR_OF_A_KIND, {1: [0], 2: [], 3: [], 4: [8]})
    assert rate_hand(string_to_hand("TH TH TH 2H 2H")) == (FULL_HOUSE, {1: [], 2: [0], 3: [8], 4: []})
    assert rate_hand(string_to_hand("AD 7H 6H 4H JH"))[0] == HIGH_CARD


def test_compare_hands():
    assert compare_hands("5H 5C 6S 7S KD", "2C 3S 8S 8D TD") == 0
    assert compare_hands("5D 8C 9S JS AC", "2C 5C 7D 8S QH") == 1
    assert compare_hands("2D 9C AS AH AC", "3D 6D 7D TD QD") == 0
    assert compare_hands("4D 6S 9H QH QC", "3D 6D 7H QD QS") == 1
    assert compare_hands("2H 2D 4C 4D 4S", "3C 3D 3S 9S 9D") == 1
    assert compare_hands("AC 3D AS 8C TD", "7H KH 5D 6C JD") == 1
    assert compare_hands("TC 9C 8C 7C 6C", "TD 9D 8D 7D JD") == 0
    assert compare_hands("9H 8H 7H 5H 4H", "9D 6D 7D 8D 4D") == 0
    assert compare_hands("8H 6H 3H 5H 4H", "9D 5D 7D 8D 4D") == 0
    assert compare_hands("8D 6D 6H 4D 4H", "9S 4C 4C 6S 6S") == 0
    assert compare_hands("AD 7H 6H 4H JH", "KC TD TS 7D 6S") == 0


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum(evaluate_file(sys.argv[-1]))
