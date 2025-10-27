// Según la calificación (A, B, C, D, F), mostrar el mensaje de rendimiento del estudiante.
Algoritmo Segun_Rendimiento_Estudiante
    Definir Nota Como Caracter
    Definir Rendimeinto Como Cadena
	Escribir "Ingrese la calificación (A, B, C, D, F):"
    Leer Nota
	Nota <- Mayusculas(Nota)
    Segun nota Hacer
        'A': Rendimeinto <- "Excelente"
		'B': Rendimeinto <- "Bueno"
        'C': Rendimeinto <- "Aceptable"
        'D': Rendimeinto <- "Bajo"
        'F': Rendimeinto <- "Deficiente"
        De Otro Modo:
            Rendimeinto <- "Calificación inválida"
    FinSegun
    Escribir "Resultado: ", Rendimeinto
FinAlgoritmo