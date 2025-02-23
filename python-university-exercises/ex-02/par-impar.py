while True:

    print(
        """
        Bienvenido al verficador de numeros pares o impares
        1. Consultar
        2. Salir
        """
    )

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    match opcion:

        case 1:
            numero = int(input("Ingrese un número: "))
            if numero % 2 == 0:
                print(f"El número {numero} es par")
            else:
                print(f"El número {numero} es impar")

        case 2:
            break

        case _:
            print("Opción incorrecta")
