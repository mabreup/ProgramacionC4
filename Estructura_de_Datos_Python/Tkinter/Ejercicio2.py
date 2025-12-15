#Crea una interfaz con un Entry y un Button. Al presionar el botón, muestra el texto escrito en el Entry en un Label.
import tkinter as tk
def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=texto)
ventana = tk.Tk()
ventana.title("Mostrar Texto")
ventana.geometry("400x200")
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)
boton_mostrar = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto, font=("Arial", 14))
boton_mostrar.pack(pady=10)
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 10))
etiqueta_resultado.pack(pady=10)
ventana.mainloop()
