#Adivina el número secreto (ejemplo: 7).
numero_secreto = 7
while True:
    Adivina = int(input("Adivina el número secreto (entre 1 y 10) "))
    if Adivina == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    else:
        print("Intenta de nuevo.")



        