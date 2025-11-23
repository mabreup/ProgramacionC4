#Crea una clase llamada **Usuario** con atributos nombre y edad. Implementa una función que muestre los datos del usuario.
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
# Crear una instancia de la clase Usuario
usuario1 = Usuario("Juan", 30)
# Mostrar los datos del usuario
usuario1.mostrar_datos()
usuario2 = Usuario("María", 25)
usuario2.mostrar_datos()
usuario3 = Usuario("Luis", 40)
usuario3.mostrar_datos()


