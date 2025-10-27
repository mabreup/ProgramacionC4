//Leer números hasta que su suma sea mayor a 100.
Algoritmo  Mientras_Igresa_Numeros_Hasta_Sumar_100
    Definir N, Suma Como Entero
    Suma = 0
	Mientras Suma <= 100 Hacer
        Escribir "Ingrese un número: "
        Leer N
		Suma = Suma + N
    FinMientras
	Escribir "La suma de los numeros digitaods es: ", Suma
FinAlgoritmo