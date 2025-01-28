# Solution 1


def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    factorials = 1
    for i in range(2, n + 1):
        factorials = factorials * i

    return factorials


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(f"Factorial of {i} is {factorial(i)}")

# Solution 2


def fact(n):
    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)


n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(f"Factorial of {i} is {fact(i)}")
