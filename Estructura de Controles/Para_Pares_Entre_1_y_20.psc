//Contar cuántos números pares hay entre 1 y 20
Algoritmo Para_Pares_Entre_1_y_20
	Definir Cont, i Como Entero
	Cont = 0
	Para i <- 1 Hasta 20 Con Paso 1 Hacer
		Si i MOD 2 = 0 Entonces
			Cont = Cont + 1
		FinSi
	FinPara
	Escribir "La cantidad de numeros pares entre el 1 y 20 es: ", Cont
FinAlgoritmo
