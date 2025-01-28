texto_1 = input("Enter the first text to compare: ").lower().replace(" ", "")
texto_2 = input("Enter the second text to compare: ").lower().replace(" ", "")

if texto_1 != "" and texto_2 != "":
    sorted_1 = sorted(texto_1)
    sorted_2 = sorted(texto_2)
    if sorted_1 == sorted_2:
        print("They are anagrams")
    else:
        print("They are not anagrams")
elif texto_1 == "":
    print("The first text is empty")
else:
    print("The second text is empty")
