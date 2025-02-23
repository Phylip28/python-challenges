while True:
    try:
        filas = int(input("Numero de filas: "))
        columnas = int(input("Numero de columnas: "))
        break

    except ValueError:
        print("Debe ingresar un numero entero")

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
                print("Debe ingresar un numero entero")
    matriz.append(fila)

print("Matriz:")
for fila in matriz:
    print(" ".join(map(str, fila)))
