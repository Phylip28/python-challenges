frases = []

while True:

    print(
        """
        Bienvenido al eliminador de palabras
        1. Ingresar frase
        2. Listar frases
        3. Eliminar palabra de frase
        4. Salir
        """
    )

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    match opcion:

        case 1:
            frase = input("Ingrese una frase: ")
            frases.append(frase)
            print("Frase ingresada correctamente.")

        case 2:
            print("Listando frases...")
            for id, frase in enumerate(frases, 1):
                print(f"{id}. {frase}")

        case 3:
            while True:
                try:
                    id_frase = int(input("Ingrese el número de la frase: ")) - 1
                    palabra = input("Ingrese la palabra a eliminar: ")

                    if id_frase < 0 or id_frase >= len(frases):
                        print("El número de frase no es válido.")
                        continue

                    frases[id_frase] = frases[id_frase].replace(palabra, "")

                    print(f"\n {frases[id_frase]}")
                    print("Palabra eliminada correctamente.")
                    break

                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue

        case 4:
            print("Saliendo...")
            break

        case _:
            print("Opción incorrecta")
