def encryptMessage(message, shift_value):
    encrypted = ""
    if 1 <= shift_value <= 25:
        for char in message:
            if char.isspace() or char.isdigit():
                encrypted += char
            else:
                if char.isupper():
                    if ord(char) + shift_value > 90:
                        offset = ord(char) + shift_value - 91
                        encrypted += chr(ord("A") + offset)
                    else:
                        encrypted += chr(ord(char) + shift_value)
                else:
                    if ord(char) + shift_value > 122:
                        offset = ord(char) + shift_value - 123
                        encrypted += chr(ord("a") + offset)
                    else:
                        encrypted += chr(ord(char) + shift_value)
    else:
        return (
            f"Please enter a shift value between 1 and 25.\nYou entered: {shift_value}"
        )
    return encrypted


def decryptMessage(message, key):
    decrypted = ""

    if 1 <= key <= 25:
        for char in message:
            if char.isspace() or char.isdigit():
                decrypted += char
            else:
                if char.isupper():
                    if ord(char) - key < 65:
                        offset = ord(char) - key + 65
                        decrypted += chr(offset)
                    else:
                        decrypted += chr(ord(char) - key)
                else:
                    if ord(char) - key < 97:
                        offset = ord(char) - key + 97
                        decrypted += chr(offset)
                    else:
                        decrypted += chr(ord(char) - key)
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
            shift_value = int(input("Enter a shift value (must be between 1 and 25): "))
            print(encryptMessage(message, shift_value))

        case 2:
            message = input("Enter the message to decrypt: ")
            key = int(input("Enter the key (must be between 1 and 25): "))
            print(decryptMessage(message, key))

        case 3:
            print("Exiting...")
            break
        case default:
            print("Invalid option, please try again.")

    print("---" * 25)
