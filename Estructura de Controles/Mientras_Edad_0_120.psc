//Leer edades hasta que se ingrese una edad fuera del rango 0-120.
Algoritmo Mientras_Edad_0_120
Definir edad Como Entero
Escribir "Ingrese una edad (entre 0 y 120):"
Leer edad
Mientras edad >= 0 Y edad <= 120 Hacer
	Escribir "Edad válida: ", edad
    Escribir "Ingrese otra edad (entre 0 y 120):"
        Leer edad
    FinMientras
FinAlgoritmo
