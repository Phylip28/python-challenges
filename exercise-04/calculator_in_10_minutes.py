# Calculator in 10 minutes


class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


while True:
    print(
        """Calculator
          1. Add
          2. Subtract
          3. Multiply
          4. Divide
          5. Exit"""
    )

    option = int(input("Enter an option: "))

    match option:
        case 1:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = Calculator().add(num1, num2)
            print(result)
        case 2:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = Calculator().subtract(num1, num2)
            print(result)
        case 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = Calculator().multiply(num1, num2)
            print(result)
        case 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = Calculator().divide(num1, num2)
            print(result)
        case 5:
            break
