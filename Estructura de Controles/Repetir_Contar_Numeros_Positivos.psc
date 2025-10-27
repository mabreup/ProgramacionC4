//Leer números hasta que se ingrese un número negativo, mostrando la cantidad de positivos.
Algoritmo  Repetir_Contar_Numeros_Positivos
    Definir N, contador Como Entero
    contador <- 0
	Escribir "Ingrese un número Y si desa termiar digite un numero negativo:"
    Leer N
	Repetir
		 contador <- contador + 1
        Escribir "Ingrese otro número, si desa termiar digite un numero negativo:"
        Leer N
	Hasta Que N < 0
	Escribir "Cantidad de números Positivos: ", contador
FinAlgoritmo