#Crea una clase base llamada **Animal** con un método hablar(). Luego crea clases hijas como Perro y Gato que sobreescriban el método
#hablar() para devolver sonidos específicos.
class Animal:
    def hablar(self):
       raise NotImplementedError("Subclase debe implementar el método hablar")
class Perro(Animal):
    def hablar(self):
        return "Guau"
class Gato(Animal):
    def hablar(self):
        return "Miau"
def hacer_hablar(animales):
    for animal in animales:
        print(animal.hablar())
# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()
# Crear una lista de animales
animales = [perro, gato]
# Llamar a la función hacer_hablar
hacer_hablar(animales)

