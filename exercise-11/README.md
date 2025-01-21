## Problem to solve:
The program calculates the "day of the year" for a given date. It takes the year, month, and day as input and returns the total number of days that have passed since the beginning of the year. The program also correctly handles leap years and the different number of days in each month.

## Key points to consider:
- The program includes a function to check if a year is a leap year.
- The number of days in each month is taken into account, including adjustments for February in leap years.
- The function returns `None` if an invalid date is provided (e.g., year before 1582 or a negative month).
- The result is the total number of days from the start of the year to the given date.
