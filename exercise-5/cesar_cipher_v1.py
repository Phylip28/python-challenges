def encryptMessage(message):
    encrypted = ""

    for letter in message:
        if not letter.isalpha():
            continue

        letter = letter.upper()
        value_ascii = ord(letter) + 1

        if value_ascii > ord("Z"):
            value_ascii = ord("A")

        encrypted += chr(value_ascii)

    return encrypted


def decryptMessage(message):
    decrypted = ""

    for letter in message:
        if not letter.isalpha():
            continue

        letter = letter.lower()
        value_ascii = ord(letter) - 1

        if value_ascii < ord("A"):
            value_ascii = ord("Z")

        decrypted += chr(value_ascii)

    return decrypted


while True:

    print(
        "Welcome to the Cesar Cipher\n",
        "1. Encrypt message\n",
        "2. Decrypt message\n",
        "3. Exit",
    )
    option = int(input("Select an option: "))

    match option:
        case 1:
            message = input("Enter the message to encrypt: ")
            encrypted_message = encryptMessage(message)

            if encrypted_message.isalpha() and encrypted_message.isupper():
                print(f"The message was successfully encrypted: {encrypted_message}")
            else:
                print("The message was not encrypted correctly, please try again.")
        case 2:
            message = input("Enter the message to decrypt: ")
            decrypted_message = decryptMessage(message)

            if decrypted_message.isalpha() and decrypted_message.islower():
                print(f"The message was successfully decrypted: {decrypted_message}")
            else:
                print("The message was not decrypted correctly, please try again.")
        case 3:
            print("Exiting...")
            break
        case default:
            print("Invalid option, please try again.")

    print("---" * 25)
