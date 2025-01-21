from os import strerror

filename = input("Enter the file name: ")
letters = {}

try:
    with open(filename, "rt") as src:
        char = src.read(1)

        while char != "":
            char = char.lower()
            if char != " ":
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
            char = src.read(1)

        ext = filename.find(".")
        output_filename = filename[:ext] + ".hist"
        sorted_letters = dict(sorted(letters.items(), key=lambda item: item[1]))

        with open(output_filename, "wt") as dst:
            text = ""
            for letter in sorted_letters:
                text += f"{letter} -> {letters.get(letter)}\n"
            dst.write(text)

except IOError as e:
    print(strerror(e.errno))
