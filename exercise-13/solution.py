import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year: int, weekday: int) -> int:
        if weekday < 0 or weekday > 6:
            raise ValueError("Weekday must be in the range 0-6")

        count_day = 0
        for month in range(1, 13):
            for day, day_of_week in self.itermonthdays2(year, month):
                if day != 0 and day_of_week == weekday:
                    count_day += 1
        return count_day


calendar_instance = MyCalendar()
year = int(input("Enter the year: "))
day_of_week = int(input("Enter a weekday (0 = Monday, 6 = Sunday): "))

print(
    f"The weekday {day_of_week} appears {calendar_instance.count_weekday_in_year(year, day_of_week)} times in {year}."
)
