#Pide 5 notas, calcula la suma y el promedio final.
suma = 0
contador = 1
while contador <= 5:
    nota = float(input(f"Ingresa la nota # {contador} :" ))
    suma += nota
    contador += 1
promedio = suma / 5
print(f"El promedio final es: {promedio}")
