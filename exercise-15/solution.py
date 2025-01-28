def display_led(input_number):
    input_number = str(input_number)

    # LED representation of numbers 0-9
    led_numbers = [
        "###\n# #\n# #\n# #\n###",  # Number 0
        "  #\n  #\n  #\n  #\n  #",  # Number 1
        "###\n  #\n###\n#  \n###",  # Number 2
        "###\n  #\n###\n  #\n###",  # Number 3
        "# #\n# #\n###\n  #\n  #",  # Number 4
        "###\n#  \n###\n  #\n###",  # Number 5
        "###\n#  \n###\n# #\n###",  # Number 6
        "###\n  #\n  #\n  #\n  #",  # Number 7
        "###\n# #\n###\n# #\n###",  # Number 8
        "###\n# #\n###\n  #\n###",  # Number 9
    ]

    # Generate list with each number's LED lines
    output = [""] * 5  # Each number has 5 lines
    for char in input_number:
        if input_number.isdigit():
            led = led_numbers[int(char)].split("\n")
            for i in range(5):
                output[i] += led[i] + " "
        else:
            return f"Invalid input: {input_number} (only digits allowed)"

    return "\n".join(output)


# Request user input
user_input = input("Enter the number to display (digits only): ")
result = display_led(user_input)

print(result)
