while True:

    print(
        """
        Bienvenido al verficador de numeros mayores
        1. Ingresar numeros
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
            numero_1 = int(input("Ingrese el primer número: "))
            numero_2 = int(input("Ingrese el segundo número: "))
            numero_3 = int(input("Ingrese el tercer número: "))

            numeros = [numero_1, numero_2, numero_3]

            print(f"El número mayor es: {max(numeros)}")

        case 2:
            break

        case _:
            print("Opción incorrecta")
