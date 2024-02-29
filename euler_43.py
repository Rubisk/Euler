import sys
import pytest


def get_all_possible_options(n, string, prime):
    for c in string:
        if int((c + str(n))[:3]) % prime == 0:
            yield c + str(n)


def get_all_numbers():
    last_three = 17
    while last_three < 1000:
        number = str(last_three)
        while len(number) < 3:
            number = "0" + number
        if len([d for d in "0123456789" if d not in number]) != 7:
            last_three += 17
            continue
        numbers = [number]

        for p in [13, 11, 7, 5, 3, 2]:
            new_numbers = []
            for n in numbers:
                string = [d for d in "0123456789" if d not in n]
                # print [d for d in "0123456789" if d not in n], n
                new_numbers.extend(get_all_possible_options(n, string, p))
            numbers = new_numbers
        for n in numbers:
            yield int([d for d in "0123456789" if d not in n][0] + n)
        last_three += 17


def test_get_all_numbers():
    print [len(str(n)) for n in get_all_numbers()]
    assert all([len(str(l)) == 10 for l in get_all_numbers()])
    assert 1406357289 in [g for g in get_all_numbers()]


def test_get_all_possible_options():
    assert [g for g in get_all_possible_options(289, "0134567", 13)] == ['7289']


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
    else:
        print sum([x for x in get_all_numbers()])