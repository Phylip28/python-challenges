def is_prime(num):
    """Checks if a number is prime using an optimized approach."""

    if num == 2:
        return True

    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):  # Only checking odd numbers
        if num % i == 0:
            return False
    return True


def print_primes(start, end):
    """Prints all prime numbers in the given range."""

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print(" ".join(map(str, primes)))


# Example usage
print_primes(1, 20)
