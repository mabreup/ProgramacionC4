//Ingresar notas hasta que el usuario ingrese -1, y luego mostrar el promedio
Algoritmo  Repetir_Hasta_Ingresa_Menos1
    Definir Nota, Suma, i Como Entero
    Suma = 0
	i = 0
	Repetir
		 Escribir "Ingrese la nota, para saber el promedio digite -1:"
		 Leer Nota
		 Si Nota <> -1 Entonces
			 Suma = Suma + Nota
			 i = i + 1
		 FinSi
	Hasta Que Nota = -1
	Escribir "El promedio de las notas es: ", Suma / i
FinAlgoritmo