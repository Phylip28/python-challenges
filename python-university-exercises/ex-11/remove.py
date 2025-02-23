lista = ["A", "B", "b", "c", "E", "E", "f"]

print(lista)

elemento_a_remover = input("Ingrese el elemento que desea remover: ")

lista.remove(elemento_a_remover.upper())
lista.remove(elemento_a_remover.lower())

print(lista)
