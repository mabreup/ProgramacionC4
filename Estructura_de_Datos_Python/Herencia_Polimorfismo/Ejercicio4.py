#Crea una clase **Vehiculo** con un método mover(). Crea clases hijas como Carro y Bicicleta que implementen su propia versión del método

class Vehiculo:
    def mover(self):
        raise NotImplementedError("Subclase debe implementar el método mover")
class Carro(Vehiculo):
    def mover(self):
        return "El carro se está conduciendo"
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se está pedaleando"
def hacer_mover(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo.mover()) 
# Crear instancias de Carro y Bicicleta
carro = Carro()
bicicleta = Bicicleta()
# Crear una lista de vehículos
vehiculos = [carro, bicicleta]
# Llamar a la función hacer_mover
hacer_mover(vehiculos)
