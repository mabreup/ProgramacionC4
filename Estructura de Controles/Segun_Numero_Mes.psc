//Muestre el nombre del mes correspondiente a un número del 1 al 12.
Algoritmo Segun_Numero_Mes
    Definir N Como Entero
    Definir Mes Como Cadena
	Escribir "Ingrese un número del 1 al 12:"
    Leer N
	Segun N Hacer
        1: Mes <- "Enero"
        2: Mes <- "Febrero"
        3: Mes <- "Marzo"
        4: Mes <- "Abril"
        5: Mes <- "Mayo"
        6: Mes <- "Junio"
        7: Mes <- "Julio"
        8: Mes <- "Agosto"
        9: Mes <- "Septiembre"
        10: Mes <- "Octubre"
        11: Mes <- "Noviembre"
        12: Mes <- "Diciembre"
        De Otro Modo:
            Mes <- "un número no aceptado; Debe ser entre 1 y 12."
    FinSegun
	Escribir "Mes correspondiente al numero ",N, " es ", Mes
FinAlgoritmo