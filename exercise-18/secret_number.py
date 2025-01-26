from random import randint

# Generate a random secret number between 1 and 100
secret_number = randint(1, 100)
user_number = None
attempts = 1
attempts_limit = 10

print("Welcome to the Number Guessing Game!")
print(f"You have {attempts_limit} attempts to guess the number.")

while attempts <= attempts_limit:
    try:
        user_number = int(input("Enter a number -> "))

        if user_number == secret_number:
            print("Congratulations! You win")
            break
        elif user_number > secret_number:
            print("The number is smaller.")
        else:
            print("The number is greater.")

        attempts += 1

    except ValueError:
        print("Invalid input! Please enter an integer.")

else:
    print(f"You lost! The correct number was {secret_number}.")
