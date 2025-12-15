#Crea una clase base **Figura** con un método area(). Implementa clases hijas como Círculo y Cuadrado que calculen el área según corresponda.
import math
class Figura:
    def area(self):
        raise NotImplementedError("Subclase debe implementar el método area")
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return (f"Área del Circulo es: {math.pi * (self.radio ** 2)}")
               # (f"Bono a pagar al Gerente: {self.salario * 0.20}")
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return (f"Área del Cuadrado es: {self.lado ** 2}")
def calcular_areas(figuras):
    for figura in figuras:
        #print figura.area ##    (f"" {figura.area()})
        print(f"{figura.area()}")
# Crear instancias de Círculo y Cuadrado
circulo = Circulo(5)
cuadrado = Cuadrado(4)
# Crear una lista de figuras
figuras = [circulo, cuadrado]
# Llamar a la función calcular_areas
calcular_areas(figuras)
