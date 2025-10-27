//Leer números hasta que el usuario ingrese 0 y mostrar cuántos números ingresó.
Algoritmo  Mientras_Contar_Numeros_Digitados
    Definir numero, contador Como Entero
    contador <- 0
	Escribir "Ingrese un número Y si desa termiar digite 0:"
    Leer numero
	Mientras numero <> 0 Hacer
        contador <- contador + 1
        Escribir "Ingrese otro número, si desa termiar digite 0:"
        Leer numero
    FinMientras
	Escribir "Cantidad de números Digitados: ", contador
FinAlgoritmo