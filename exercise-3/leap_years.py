# Solution 1

yearr = int(input("Enter a year: "))


def leapYear(year):
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


print(leapYear(yearr))

# Solution 2

year = int(input("Enter a year: "))

if year < 1582:
    print("It is not within the Gregorian calendar period")
else:
    if year % 4:
        print("Common year")
    elif not year % 100:
        print("Leap year")
    elif not year % 400:
        print("Common year")
    else:
        print("Leap year")
