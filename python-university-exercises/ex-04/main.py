from modules.calculadora import Calculadora

calculadora = Calculadora()

while True:

    print(
        """
        Calculadora
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. División entera
        6. Exponente
        7. Módulo
        8. Salir
        """
    )

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    match opcion:

        case 1:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.suma(numero1, numero2))

        case 2:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.resta(numero1, numero2))

        case 3:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.multiplicacion(numero1, numero2))

        case 4:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.division(numero1, numero2))

        case 5:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.division_entera(numero1, numero2))

        case 6:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.exponente(numero1, numero2))

        case 7:
            numero1 = int(input("Ingrese el primer número: "))
            numero2 = int(input("Ingrese el segundo número: "))

            print(calculadora.modulo(numero1, numero2))

        case 8:
            print("Saliendo...")
            break

        case _:
            print("Opción incorrecta")
