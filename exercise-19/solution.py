# Get user input and remove spaces
text = input("Enter a text: ").replace(" ", "").lower()

if not text:
    print("Please enter a valid text.")
else:
    if text == text[::-1]:
        print("The text is a palindrome.")
    else:
        print("The text is not a palindrome.")
