// Ingrese una letra y muestre su valor ASCII
Función resultado <- Ascii(letra)
	Definir codigoAscii, resultado, i Como Entero
	codigoAscii <- 0
	Definir Muestra Como Cadena
	Muestra <- 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	Para i<-0 Hasta Longitud(Muestra) Hacer
		Si Subcadena(Muestra,i,i)=letra Entonces
			codigoAscii <- i+64
			resultado <- codigoAscii
		FinSi
	FinPara
	Si codigoAscii=0 Entonces
		Para i<-0 Hasta Longitud(Muestra) Hacer
			Si Subcadena(Minusculas(Muestra),i,i)=letra Entonces
				codigoAscii <- i+96
				resultado <- codigoAscii
			FinSi
		FinPara
	FinSi
	Si codigoAscii=0 Entonces
		Escribir 'El carácter digitado no es una letra.'
	FinSi
FinFunción

Algoritmo Dato_Caracter_Ascii
	Definir letra Como Cadena
	Definir valorAscii Como Entero
	Escribir 'Ingrese una letra: '
	Leer letra
	valorAscii <- Ascii(letra)
	Si valorAscii<>0 Entonces
		Escribir 'El código ASCII de ', letra, ' es: ', valorAscii
	SiNo
		Escribir 'El carácter ', letra, ' no es una letra.'
	FinSi
FinAlgoritmo
