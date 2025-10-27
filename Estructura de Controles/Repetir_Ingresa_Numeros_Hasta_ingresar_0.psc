//Pedir números y sumarlos hasta que el usuario ingrese 0
Algoritmo  Repetir_Ingresa_Numeros_Hasta_ingresar_0
    Definir N, Suma Como Entero
    Suma = 0
	Repetir
		 Escribir "Ingrese un número, Para terminar Digite 0: "
        Leer N
		Suma = Suma + N
	Hasta Que N = 0
	Escribir "La suma de los numeros digitaods es: ", Suma
FinAlgoritmo