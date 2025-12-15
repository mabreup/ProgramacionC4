#Crea una clase **Dispositivo** con un método encender(). Crea clases hijas como Laptop y Teléfono que sobreescriban el comportamiento del método.
class Dispositivo:
    def encender(self):
        raise NotImplementedError("Subclase debe implementar el método encender")
class Laptop(Dispositivo):
    def encender(self):
        return "La laptop se está encendiendo" 
class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono se está encendiendo"
def hacer_encender(dispositivos):
    for dispositivo in dispositivos:
        print(dispositivo.encender())
# Crear instancias de Laptop y Teléfono
laptop = Laptop()
telefono = Telefono()
# Crear una lista de dispositivos
dispositivos = [laptop, telefono]
# Llamar a la función hacer_encender
hacer_encender(dispositivos)
