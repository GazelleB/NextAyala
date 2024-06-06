def gen_secs():
    for second in range(60):
        yield second


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    # return the time as a string
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start=2024):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    for day in range(1, days_in_month[month] + 1):
        yield day


def gen_date():
    # returns the full date as a string
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


date_gen = gen_date()
count = 0

while True:
    date = next(date_gen)
    count += 1
    if count % 1000000 == 0:
        print(date)
