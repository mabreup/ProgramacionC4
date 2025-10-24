// Ingrese su nombre y apellido y muestre su nombre completo
Algoritmo Dato_Cadena_Nombre_Apellido
	Definir Nombre, Apellido, Esp, Nom Como Cadena
	Esp <- ' '
	Escribir 'Por favor digite su Nombre: '
	Leer Nombre
	Escribir 'Por favor su Apellido: '
	Leer Apellido
	Nom <- Concatenar(Nombre,Esp)
	Escribir 'Su nombre completo es: ', Concatenar(Nom,Apellido)
FinAlgoritmo
