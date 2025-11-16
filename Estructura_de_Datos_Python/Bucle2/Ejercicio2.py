#Pide 10 números y calcula la suma total.
suma = 0
contador = 0
while contador < 10:
    numero = float(input("Ingresa un número: "))
    suma += numero
    contador += 1
print("La suma total es:", suma)

