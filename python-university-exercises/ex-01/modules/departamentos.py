from time import sleep


class Departamento:

    dias_vacaciones = {
        1: [6, 14, 20],  
        2: [7, 15, 22],  
        3: [10, 20, 30]  
    }

    def vacaciones(self, nombre: str, clave: int, tiempo_servicio: int) -> str:
        try:
            if clave in self.dias_vacaciones:
                indice = min(2, max(0, (tiempo_servicio >= 2) + (tiempo_servicio >= 7)))
                dias = self.dias_vacaciones[clave][indice]

                result = f"El usuario {nombre} tiene {dias} días de vacaciones"
            else:
                result = "Clave de departamento no válida"

        except ValueError as e:
            result = f"Se produjo un error: {e}"

        print("Consultando...")
        sleep(2)

        return result