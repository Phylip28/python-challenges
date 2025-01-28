from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


estudiantes = {}

try:
    with open("./exercise-20/participation.txt", "rt") as src:

        for linea in src:

            if len(linea) == 0:
                raise FileEmpty
            if len(linea.split()) > 4:
                raise BadLine

            nombre = " ".join(linea[:-4].split())
            nota_participacion = float(linea[-4:])

            if nombre in estudiantes:
                estudiantes[nombre] += nota_participacion
            else:
                estudiantes[nombre] = nota_participacion

    for estudiante in estudiantes:

        print(f"{estudiante} {estudiantes[estudiante]}")

except IOError as e:
    print(strerror(e.errno))
except BadLine:
    print("Error en una linea")
except FileEmpty:
    print("El archivo esta vacio")
