//Contar cuántos números positivos se ingresan antes de ingresar un número negativo
Algoritmo  Mientras_Contar_Numeros_Positivos
    Definir N, contador Como Entero
    contador <- 0
	Escribir "Ingrese un número Y si desa termiar digite un numero negativo:"
    Leer N
	Mientras N >= 0 Hacer
        contador <- contador + 1
        Escribir "Ingrese otro número, si desa termiar digite un numero negativo:"
        Leer N
    FinMientras
	Escribir "Cantidad de números Positivos: ", contador
FinAlgoritmo