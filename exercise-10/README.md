## Problem to solve:
The program simulates a timer that can display the current time in hours, minutes, and seconds. It includes methods to move the timer forward by one second (`nextSecond`) and backward by one second (`prevSecond`), taking care of the changes in hours, minutes, and seconds (e.g., transitioning from 23:59:59 to 00:00:00 and vice versa).

## Key points to consider:
- The timer is initialized with hours, minutes, and seconds (default is 0:0:0).
- The `nextSecond` method increases the time by one second, adjusting the hours, minutes, and seconds when necessary.
- The `prevSecond` method decreases the time by one second, adjusting the hours, minutes, and seconds when necessary.
- The `__str__` method provides a string representation of the timer in the format `HH:MM:SS`, ensuring that both hours, minutes, and seconds are always displayed as two digits.
