days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_sundays_on_first_of_month():
    year = 1901
    month = 0
    day = 1  # Tuesday, Sunday = 6
    sundays = 0
    while year <= 2000:
        if year % 4 == 0:
            days_in_months[1] = 29
        else:
            days_in_months[1] = 28
        while month <= 11:
            day += days_in_months[month]
            day %= 7
            if day == 6:
                sundays += 1
            month += 1
        month = 0
        year += 1
    return sundays


if __name__ == "__main__":
    print get_sundays_on_first_of_month()