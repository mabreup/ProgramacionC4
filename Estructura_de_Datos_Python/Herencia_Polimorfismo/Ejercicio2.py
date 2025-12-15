#Crea una clase base **Empleado** con atributos nombre y salario. Crea clases hijas como Gerente y Técnico, cada una con un método calcular_bono() diferente
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        raise NotImplementedError("Subclase debe implementar el método calcular_bono")
class Gerente(Empleado):
    def calcular_bono(self):
        return (f"Bono a pagar al Gerente: {self.salario * 0.20}") # 20% de bono para gerentes
class Tecnico(Empleado):
    def calcular_bono(self):
        return (f"Bono a pagar al Tecnico: {self.salario * 0.10}") # 10% de bono para técnicos

def Calcula_Bono(Empleados):
    for Empleado in Empleados:
        print(Empleado.calcular_bono())

# Crear instancias de Gerente y Técnico
gerente = Gerente("Ana", 50000)
tecnico = Tecnico("Luis", 30000)
# Crear una lista de empleados
Empleados = [gerente, tecnico]
Calcula_Bono(Empleados)
