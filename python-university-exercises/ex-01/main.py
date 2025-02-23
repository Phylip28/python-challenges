from modules.departamentos import Departamento

instancia_departamento = Departamento()

while True:

    print(
        """
        Bienvenido al verficador de vacaciones
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
            nombre = input("Nombre: ")
            clave = int(input("Clave: "))
            tiempo_servicio = int(input("Tiempo de servicio (Tiempo en años): "))
            print(instancia_departamento.vacaciones(nombre, clave, tiempo_servicio))

        case 2:
            break

        case _:
            print("Opción incorrecta")
