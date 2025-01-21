def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and isYearLeap(year):
        return 29

    elif year < 1582 or month < 1 or month > 12:
        return None
    else:
        return days[month]


def dayOfYear(year, month, day):

    total_days = day

    for m in range(1, month):
        total_days += daysInMonth(year, m)

    return total_days


print(dayOfYear(2000, 12, 31))
