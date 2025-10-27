//Calcular el promedio de 5 notas ingresadas.
Algoritmo Para_Promedio
	Definir Nota, Suma Como Real
	Definir i Como Entero
	Suma = 0
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingrese la nota ", i, ":"
		Leer Nota
		Suma = Suma + Nota
	FinPara
	Escribir "El promedio de las 5 notas es: ", suma / 5
FinAlgoritmo
