from modules.operaciones_con_matrices import *


while True:

    print(
        """
        Bienvenido al operador de matrices
        1. Sumar matrices
        2. Restar matrices
        3. Salir
        """
    )

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    match opcion:

        case 1:
            OperacionesConMatrices.sumar_matriz()

        case 2:
            OperacionesConMatrices.restar_matriz()
        case 3:
            print("Saliendo...")
            break

        case _:
            print("Opción incorrecta")
