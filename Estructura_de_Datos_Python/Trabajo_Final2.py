#Almacenar usuarios y contraseñas, verificar su fuerza y alertar sobre contraseñas débiles.
from tabulate import tabulate
import re
def es_contrasena_segura(contrasena):
    if (len(contrasena) < 8 or
        not re.search(r"[A-Z]", contrasena) or
        not re.search(r"[a-z]", contrasena) or
        not re.search(r"[0-9]", contrasena) or
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)):
        return False
    return True
usuarios = []
contrasenas = []
while True:
    usuario = input("Ingresa un nombre de usuario (o 'salir' para terminar): ")
    if usuario.lower() == 'salir':
        break
    else:
         if usuario in usuarios:
            print("El nombre de usuario ya existe. Por favor, elige otro.")
         else:
              contrasena = input(f"Ingresa una contraseña segura para el usuario {usuario}: ")
              if es_contrasena_segura(contrasena):
                usuarios.append((usuario))
                contrasenas.append((contrasena))
                print("Usuario y contraseña guardados exitosamente.")
              else:
                print("La contraseña no es segura. Debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas, números y caracteres especiales.")
cantidad_usuarios = len(usuarios)
while cantidad_usuarios > 0:
    print("Usuario:", usuarios[cantidad_usuarios - 1], "- Contraseña:", contrasenas[cantidad_usuarios - 1])
    cantidad_usuarios -= 1
tabla = list(zip(usuarios, contrasenas))
print(tabulate(tabla, headers=["Usuario", "Contraseña"], tablefmt="github"))



