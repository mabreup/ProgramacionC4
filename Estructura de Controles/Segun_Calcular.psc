// Según el tipo de operación (+, -, *, /), mostrar el resultado entre dos números.
Algoritmo Segun_Calcular
    Definir Operacion Como Caracter
    Definir N1,N2, Resultado Como Entero
	Escribir "Ingrese el valor de N1:"
	Leer N1
	Escribir "Ingrese el valor de N2:"
	Leer N2
	Escribir "Que operacion desar realizar (+, -, *, /):"
    Leer Operacion
	Segun Operacion Hacer
        '+': Escribir "La suma de los números es: ", N1+N2
		'-': Escribir "La resta de los números es: ", N1-N2
        '*': Escribir "El producto de los números es: ", N1*N2
        '/':Escribir "La division de los números es: ", N1/N2
        De Otro Modo:
			Escribir "Operacion invalida."
    FinSegun
FinAlgoritmo