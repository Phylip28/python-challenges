# Solution 1 - Iterative Approach
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for _ in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 11):
    print(n, "->", fib(n))


# Solution 2 - Recursive Approach
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 11):
    print(n, "->", fibonacci(n))
