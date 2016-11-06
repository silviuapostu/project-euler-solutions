import numpy as np
import pandas as pd

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def count_1sundays(first_sunday_ix, days_in_year=365):
    global months
    first_week = np.zeros(7)
    first_week[first_sunday_ix] = 1
    n_weeks = days_in_year // 7
    sundays = np.tile(first_week, 52)
    sundays = np.concatenate(
        (sundays, first_week[:days_in_year - 364]), axis=0)
    months[2] = 28 if days_in_year == 365 else 29
    first_of_months = np.zeros(0)
    for k in months:
        month = np.zeros(months[k])
        month[0] = 1
        first_of_months = np.concatenate((first_of_months, month), axis=0)
    last_sunday = np.nonzero(sundays[-7:])[0][0]
    ctx = len(np.intersect1d(np.nonzero(sundays)[0], np.nonzero(first_of_months)[0]))
    return (ctx, last_sunday)


def p19(start_year=1901, end_year=2000):
    count = 0
    start_sunday = count_1sundays(6)[1]
    for i in range(start_year, end_year + 1, 1):
        if i % 4 == 0 and i % 400 != 0:
            x = count_1sundays(start_sunday, 366)
        else:
            x = count_1sundays(start_sunday, 365)
        count += x[0]
        start_sunday = x[1]
    return count
