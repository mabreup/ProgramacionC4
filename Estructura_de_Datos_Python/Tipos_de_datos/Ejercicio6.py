#Pregunta al usuario si tiene internet en casa (1 = Sí, 0 = No) y guarda la respuesta como lógico.
tiene_internet = bool(int(input("¿Tienes internet en casa? (1 = Sí, 0 = No): ")))
if tiene_internet == 1:
    tiene_internet = True
    print("Tiene internet en casa")
if tiene_internet == 0:
    tiene_internet = False
    print("No tiene internet en casa")
    