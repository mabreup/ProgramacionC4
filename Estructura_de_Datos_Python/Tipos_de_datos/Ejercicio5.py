#Pide al usuario que escriba su edad y muestra Verdadero si es mayor de edad (18+), Falso en caso contrario.
edad = int(input("Por favor, ingresa tu edad: "))
if edad >= 18:
    es_mayor = "Verdadero"
else:
    es_mayor = "Falso"
print("¿Es mayor de edad?", es_mayor)
