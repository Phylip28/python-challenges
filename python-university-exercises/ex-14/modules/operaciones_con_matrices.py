class OperacionesConMatrices:

    @staticmethod
    def crear_matriz(filas: int, columnas: int) -> list:
        """Crea una matriz ingresada por el usuario."""
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                while True:
                    try:
                        valor = int(input(f"Elemento [{i}][{j}]: "))
                        fila.append(valor)
                        break
                    except ValueError:
                        print("Debe ingresar un número entero")
            matriz.append(fila)
        return matriz

    @staticmethod
    def imprimir_matriz(matriz: list) -> None:
        """Imprime una matriz de manera formateada."""
        for fila in matriz:
            print(" ".join(map(str, fila)))
        print()

    @staticmethod
    def imprimir_ecuacion(equation: list) -> None:
        """Imprime una ecuación con matrices y operadores horizontalmente."""
        matrices = [elem for elem in equation if isinstance(elem, list)]
        if not matrices:
            print("No hay matrices para mostrar.")
            return
        num_filas = len(matrices[0])
        for fila_idx in range(num_filas):
            line_parts = []
            for elem in equation:
                if isinstance(elem, list):
                    row_str = "  ".join(map(str, elem[fila_idx]))
                    line_parts.append(row_str)
                else:
                    line_parts.append(f" {elem} ")
            print("   ".join(line_parts))
        print()

    @staticmethod
    def _operacion_matrices(operacion: str) -> None:
        """Realiza una operación (+, -) entre varias matrices."""
        lista_de_matrices = []

        while True:
            try:
                numero_de_matrices = int(
                    input("Ingrese el número de matrices a operar (mínimo 2): ")
                )
                if numero_de_matrices < 2:
                    print("Debe ingresar al menos 2 matrices.")
                else:
                    break
            except ValueError:
                print("Debe ingresar un número entero.")

        while True:
            try:
                filas = int(input("Ingrese el número de filas: "))
                columnas = int(input("Ingrese el número de columnas: "))
                break
            except ValueError:
                print("Debe ingresar un número entero.")

        print("Ingrese los valores para la matriz 1")
        matriz_inicial = OperacionesConMatrices.crear_matriz(filas, columnas)
        lista_de_matrices.append(matriz_inicial)
        matriz_resultante = [fila.copy() for fila in matriz_inicial]

        for matriz_idx in range(numero_de_matrices - 1):
            print(f"Ingrese los valores para la matriz {matriz_idx + 2}")
            matriz_actual = OperacionesConMatrices.crear_matriz(filas, columnas)
            lista_de_matrices.append(matriz_actual)

            for fila in range(filas):
                for columna in range(columnas):
                    if operacion == "+":
                        matriz_resultante[fila][columna] += matriz_actual[fila][columna]
                    elif operacion == "-":
                        matriz_resultante[fila][columna] -= matriz_actual[fila][columna]

        equation = []
        for i in range(numero_de_matrices):
            equation.append(lista_de_matrices[i])
            if i < numero_de_matrices - 1:
                equation.append(operacion)
        equation.append("=")
        equation.append(matriz_resultante)

        print("\nOperación realizada:")
        OperacionesConMatrices.imprimir_ecuacion(equation)

    @staticmethod
    def sumar_matriz() -> None:
        """Suma varias matrices ingresadas por el usuario."""
        OperacionesConMatrices._operacion_matrices("+")

    @staticmethod
    def restar_matriz() -> None:
        """Resta varias matrices ingresadas por el usuario."""
        OperacionesConMatrices._operacion_matrices("-")
