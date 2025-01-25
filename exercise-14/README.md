## Problem to solve:
This program determines whether a number is prime and prints all prime numbers within a given range. Two solutions are provided:
1. A naive approach that checks divisibility against all numbers up to `n-1`.
2. An optimized approach that:
   - Returns `False` for even numbers greater than 2.
   - Only checks divisibility up to the square root of `n`, reducing unnecessary comparisons.

## Key points to consider:
- The naive method is inefficient for large numbers.
- The optimized method significantly reduces the number of iterations.
- A function `print_primes(start, end)` prints all prime numbers in a given range.
