Funcion reporte ( Usuarios, contraseñas, Seguridad, total_usuarios )
	 Escribir ""
	 Escribir "=== REPORTE DE USUARIOS Y SEGURIDAD DE CONTRASEÑAS  ==="
	 Escribir "===      PARA VALIDAR QUE FUERON GUARDADOS          ==="
    Para i <- 1 Hasta total_usuarios - 1 Con Paso 1
		Escribir "Registro: ",i
        Escribir "Usuario: ", Usuarios[i]
        Escribir "Contraseña: ", Contraseñas[i]
        Escribir "Nivel de seguridad: ", Seguridad[i]
        Escribir "-----------------------------"
    FinPara
Fin Funcion

Funcion VerificaClave <- verifica ( Contraseña )
	// Verificar fuerza de la contraseña
        tiene_mayuscula = Falso
        tiene_minuscula = Falso
        tiene_numero = Falso
		Si Longitud(contraseña) >= 8 Entonces
			tamano = Verdadero
		    Para i <- 1 Hasta longitud(contraseña) Con Paso 1 Hacer
				caracte = SubCadena(contraseña, i, i)
				Si SubCadena(contraseña, i, i) >= "A" Y SubCadena(contraseña, i, i) <= "Z" Entonces
					tiene_mayuscula =Verdadero
				FinSi
				Si SubCadena(contraseña, i, i) >= "a" Y SubCadena(contraseña, i, i) <= "z" Entonces
					tiene_minuscula = Verdadero
				FinSi
				Si SubCadena(contraseña, i, i) >= "0" Y SubCadena(contraseña, i, i) <= "9" Entonces
					tiene_numero = Verdadero
				FinSi
			FinPara
		FinSi
		
        // Evaluar nivel de seguridad
        Si tamano = Verdadero Y tiene_mayuscula = Verdadero Y tiene_minuscula = Verdadero Y tiene_numero = Verdadero
			Entonces
            VerificaClave <- "Fuerte"
		Sino
            VerificaClave <- "Débil"
        FinSi
Fin Funcion

// Gestor de Contraseñas Seguras 
//Objetivo: Almacenar usuarios y contraseñas, verificar su fuerza y alertar sobre 
//contraseñas débiles. 
//Componentes: - Vectores: usuarios, contraseñas - Condicionales y bucles: verificación 
//de fuerza - Funciones: RegistrarUsuario, VerificarContraseña, GenerarAlertas - Tipos de 
//datos: cadena, lógico
Algoritmo Gestor_Contraseñas_Seguras
    Definir usuario, Clave, contraseña, continuar, nivel_seguridad Como Cadena
    Definir tamano, tiene_mayuscula, tiene_minuscula, tiene_numero Como logico
    total_usuarios = 1
	Dimension Usuarios[100], Contraseñas[100], Seguridad[100]
    
	Escribir "=== Gestor de Contraseñas Seguras ==="

    Repetir
        Escribir "Ingrese el nombre de usuario:"
        Leer usuario

        Escribir "Ingrese la contraseña (Debe contener Minimo 8 caracteres, Maysculas, Minusculas y Numeros:"
        Leer Clave
		
	//Funcion  para verificar la Clave
		nivel_seguridad <- verifica (Clave)
		
	// Evaluar nivel de seguridad
        Si  nivel_seguridad = "Fuerte"
			Entonces
           	Escribir "Contraseña aceptada."
		Sino
            Escribir "ALERTA: La contraseña ingresada es débil. Considere mejorarla."
        FinSi

        // Guardar datos
		 Usuarios[total_usuarios] <- usuario
         Contraseñas[total_usuarios] <- Clave
         Seguridad[total_usuarios] <- nivel_seguridad
         total_usuarios <- total_usuarios + 1

        Escribir "¿Desea registrar otro usuario? (S/N)"
        Leer continuar
	Hasta Que continuar = 'N' o continuar = "n"

    // Reporte final
	reporte(Usuarios,contraseñas, Seguridad, total_usuarios)

    Escribir "Fin del gestor de contraseñas."
FinAlgoritmo
