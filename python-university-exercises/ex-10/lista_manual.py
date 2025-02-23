lista = []


while True:
    try:
        tamano_lista = int(input("Ingrese el tamaño de la lista: "))
        break

    except ValueError:
        print("Por favor, ingrese un número entero.")
        continue


for elemento in range(tamano_lista):
    while True:
        try:
            entero = int(input(f"Ingrese el elemento {elemento + 1}: "))

            lista.append(entero)
            break

        except ValueError:
            print("Por favor, ingrese un número entero.")

print("Lista ingresada:", lista)
