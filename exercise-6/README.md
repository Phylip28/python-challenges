## Problem to solve:
The program calculates the "Life Digit" based on the user's birth date. The Life Digit is derived by summing all digits of the birth date repeatedly until a single-digit number is obtained.

## Key points to consider:
- The user inputs their birth date in any format (e.g., `dd/mm/yyyy`, `dd-mm-yyyy`, etc.).
- Non-numeric characters such as slashes (`/`), dashes (`-`), spaces, and zeros (`0`) are removed before processing.
- The program sums all remaining digits.
- If the sum is greater than 9, the process repeats until a single-digit number is obtained.
- The program follows a recursive approach to reduce the number.
