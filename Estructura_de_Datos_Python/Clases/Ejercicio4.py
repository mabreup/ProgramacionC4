#Crea una clase llamada **CuentaBancaria** con atributos titular y balance. Implementa funciones para depositar y retirar.
class CuentaBancaria:
    def __init__(self, titular, balance=0):
        self.titular = titular
        self.balance = balance
    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo balance: {self.balance}")
    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes para retirar.")
        else:
            self.balance -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo balance: {self.balance}")
mi_cuenta = CuentaBancaria("Pedro Pablo", 500)
print(f"Cuenta creada para {mi_cuenta.titular} con balance inicial de {mi_cuenta.balance}")
Op=input("Que operacion desea realizar 1 para deposito, 2 para retirar y 3 para salir: ")
while Op != '3':
    if Op == '1':
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        mi_cuenta.depositar(cantidad)
    elif Op == '2':
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        mi_cuenta.retirar(cantidad)
    else:
        print("Operación no válida.")
    Op=input("Que operacion desea realizar 1 para deposito 2 para retirar y 3 para salir: ")
print(f"Operación finalizada. Balance final: {mi_cuenta.balance}")




