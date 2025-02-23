texto = input("Introduce una cadena de texto: ")

for i in range(len(texto) - 1, -1, -1):
    print(texto[i], end="")
