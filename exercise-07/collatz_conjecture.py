number = int(input("Enter a positive integer: "))
steps = 0

while number != 1:
    steps += 1
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)

print("Steps:", steps)
