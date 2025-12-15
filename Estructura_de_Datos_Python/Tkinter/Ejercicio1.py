#Crea una ventana básica con Tkinter que muestre un mensaje de bienvenida usando un Label.
import tkinter as tk
def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ventana Basica")
    ventana.geometry("300x200")
    etiqueta_bienvenida = tk.Label(ventana, text="¡Bienvenid@!", font=("Arial", 26))
    etiqueta_bienvenida.pack(pady=50)
    ventana.mainloop()
crear_ventana()
