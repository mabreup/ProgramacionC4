//Calcular el factorial de un número 
Algoritmo Repetir_Factorial
	Definir N, Fact, i Como Entero
	Fact = 1
	i = 1
	Escribir "Digite un numero para calcular su factorial: "
	Leer N
	Repetir
		Fact= Fact * i
		i = i +1
	Hasta Que i > N
	Escribir "El Factorial de ", N, " es: ", Fact
FinAlgoritmo
