// Según el número del día (1-7), mostrar su nombre correspondiente
Algoritmo Segun_Dia_Semana
    Definir N Como Entero
    Definir Dia Como Cadena
	Escribir "Ingrese un número del 1 al 7:"
    Leer N
	Segun n Hacer
        1: Dia <- "Dommingo"
        2: Dia <- "Lunes"
        3: Dia <- "Martes"
        4: Dia <- "Miercoles"
        5: Dia <- "Jueves"
        6: Dia <- "Viernes"
        7: Dia <- "Sabado"
        De Otro Modo:
            Dia <- "un número no aceptado; Debe ser entre 1 y 7."
    FinSegun
    Escribir "Dia correspondiente al numero ",N, " es ", Dia
FinAlgoritmo