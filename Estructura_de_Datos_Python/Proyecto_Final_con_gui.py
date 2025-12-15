#Gestor de Contraseñas
#Objetivo: Almacenar usuarios y contraseñas, verificar su fuerza y alertar sobre contraseñas débiles.
#Componentes: - Vectores: usuarios, contraseñas - Condicionales y bucles: verificación de fuerza - Funciones: RegistrarUsuario, VerificarContraseña, GenerarAlertas
#incluye interfaz grafica y manual de uso.
import tkinter as tk
from tkinter import messagebox
import re
class GestorContraseñas:
    def __init__(self):
        self.usuarios = []
        self.contraseñas = []
    def es_contrasena_segura(self, contraseña):
        if (len(contraseña) < 8 or
            not re.search(r"[A-Z]", contraseña) or
            not re.search(r"[a-z]", contraseña) or
            not re.search(r"[0-9]", contraseña) or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)):
            return False
        return True
    def registrar_usuario(self, usuario, contraseña):
        if usuario in self.usuarios:
            return "El usuario ya existe."
        else:
            if self.es_contrasena_segura(contraseña):
                self.usuarios.append(usuario)
                self.contraseñas.append(contraseña)
                return "Usuario registrado exitosamente."
            else:
                return "La contraseña no es segura."
    
    def generar_alerta(self, contraseña):
        if self.es_contrasena_segura(contraseña):
            return "Contraseña fuerte."
        else:
            return "Contraseña débil. Debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial."
class AplicacionGestorContraseñas:
    def __init__(self, master):
        self.gestor = GestorContraseñas()
        self.master = master
        self.master.title("Gestor de Contraseñas")
        self.master.geometry("400x300")
        self.label_usuario = tk.Label(master, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack()
        self.label_contraseña = tk.Label(master, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()
        self.boton_registrar = tk.Button(master, text="Registrar", command=self.registrar)
        self.boton_registrar.pack()
        self.boton_mostrar = tk.Button(master, text="Mostrar Usuarios", command=self.Mostrar_Usuarios)
        self.boton_mostrar.pack()
        
    def registrar(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        mensaje_registro = self.gestor.registrar_usuario(usuario, contraseña)
        mensaje_alerta = self.gestor.generar_alerta(contraseña)
        messagebox.showinfo("Registro", mensaje_registro + "\n" + mensaje_alerta)
        # limpiar campos tras registro
        if mensaje_registro == "Usuario registrado exitosamente.":
            self.entry_contraseña.delete(0, tk.END)
            self.entry_usuario.delete(0, tk.END)
            

#para mostarar los Usuarios registrados en una ventana grafica
    def Mostrar_Usuarios(self):
        ventana = tk.Toplevel(self.master)
        ventana.title("Usuarios y Contraseñas")
        ventana.geometry("480x500")

        # Encabezados
        encabezado_frame = tk.Frame(ventana)
        encabezado_frame.pack(fill="x", padx=10, pady=(10,0))
     #   tk.Label(encabezado_frame, text="Índice", width=6, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(encabezado_frame, text="Usuario", width=20, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", padx=(6,0))
        tk.Label(encabezado_frame, text="Contraseña", width=26, anchor="w", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w", padx=(6,0))

        # Área con scroll
        frame = tk.Frame(ventana)
        frame.pack(fill="both", expand=True, padx=10, pady=8)

        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Rellenar con los vectores actuales
        for idx, usuario in enumerate(self.gestor.usuarios):
            contraseña = self.gestor.contraseñas[idx] if idx < len(self.gestor.contraseñas) else ""
            tk.Label(scrollable_frame, text=str(idx), width=6, anchor="w").grid(row=idx, column=0, sticky="w")
            tk.Label(scrollable_frame, text=usuario, width=20, anchor="w").grid(row=idx, column=1, sticky="w", padx=(6,0))
            tk.Label(scrollable_frame, text=contraseña, width=26, anchor="w").grid(row=idx, column=2, sticky="w", padx=(6,0))

        # Botón para cerrar
        tk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=(6,10))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGestorContraseñas(root)
    root.mainloop()


