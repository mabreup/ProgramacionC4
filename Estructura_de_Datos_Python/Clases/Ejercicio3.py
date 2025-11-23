#Crea una clase llamada **Coche** con atributos marca y velocidad. Agrega una función que aumente la velocidad.
class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad del {self.marca} es ahora {self.velocidad} km/h.")
mi_coche = Coche("Toyota")
mi_coche.acelerar(20)
mi_coche.acelerar(30)
mi_coche.acelerar(50)
mi_coche.acelerar(10)
mi_coche.acelerar(15)
mi_coche.acelerar(25)
mi_coche.acelerar(40)
mi_coche.acelerar(5)
mi_coche.acelerar(60)