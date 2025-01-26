import random


def generate_string(length):
    """Generates a random string of lowercase letters with the given length."""
    if isinstance(length, int):
        return "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length)
        )
    else:
        return "Please enter an integer number."


def search_word(word, string):
    """Checks whether the given word exists within the string while maintaining order."""

    if not word.isalpha():
        return "Please enter a valid word."

    word = word.lower()
    string_iterator = iter(string)

    if all(letter in string_iterator for letter in word):
        return "The word exists in the string."
    else:
        return "The word does not exist in the string."


while True:
    print(
        "Welcome to Word Search\n",
        "1. Search for a word in a random string\n",
        "2. Search for a word in a custom string\n",
        "3. Exit",
    )

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid option.")
        continue

    match option:
        case 1:
            word = input("Enter the word to search: ")
            string = generate_string(int(input("Enter the length of the string: ")))
            print(search_word(word, string))
        case 2:
            word = input("Enter the word to search: ")
            string = input("Enter the string: ")
            print(search_word(word, string))
        case 3:
            print("Goodbye!")
            exit()
        case _:
            print("Please enter a valid option.")
