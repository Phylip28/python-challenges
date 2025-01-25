## Problem to solve:
This program calculates the number of times a specific weekday appears in a given year. It extends the `calendar.Calendar` class and implements a method to count occurrences of a given weekday.

## Key points to consider:
- The program accepts a year and a weekday (0 = Monday, 6 = Sunday) as input.
- It iterates through each month of the year, counting the occurrences of the given weekday.
- The `itermonthdays2(year, month)` method is used, which returns tuples where the first value is the day (0 for padding days) and the second value is the weekday.
- The program ensures that only valid weekdays (0-6) are processed.
