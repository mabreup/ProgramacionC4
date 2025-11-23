#Crea una clase llamada **Estudiante** con nombre y calificaciones. Implementa una función que calcule el promedio.
class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
nombre = input("Ingresa el nombre del estudiante: ")
num_calificaciones = int(input("Ingresa el número de calificaciones: "))
calificaciones = []
for i in range(num_calificaciones):
    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
    calificaciones.append(calificacion)
estudiante1 = Estudiante(nombre, calificaciones)
promedio = estudiante1.calcular_promedio()
print(f"El promedio de {estudiante1.nombre} es: {promedio}")

