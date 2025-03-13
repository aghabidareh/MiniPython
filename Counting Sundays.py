# Function to determine if a year is a leap year
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0


month_days = {
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

current_day = 1

sunday_count = 0

for year in range(1901, 2001):
    if is_leap_year(year):
        month_days[2] = 29
    else:
        month_days[2] = 28

    for month in range(1, 13):
        if current_day == 6:
            sunday_count += 1

        current_day = (current_day + month_days[month]) % 7

print(sunday_count)
