#Crea una clase llamada **Rectangulo** que reciba base y altura. Implementa una función que calcule el área.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
Base = int(input("Ingresa la base: "))
Altura = int(input("Ingresa la altura: "))
rectangulo1 = Rectangulo(Base, Altura)
area1 = rectangulo1.calcular_area()
print(f"El área del rectángulo es: {area1}")
