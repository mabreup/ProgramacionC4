#Crea una calculadora sencilla que pueda sumar dos números usando Labels, Entries y Buttons.
import tkinter as tk
def sumar_numeros():
    try:
        num1 = int(entrada_num1.get())
        num2 = int(entrada_num2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa números válidos.")
ventana = tk.Tk()
ventana.title("Calculadora que suma 2 numeros")
ventana.geometry("400x300")
etiqueta_num1 = tk.Label(ventana, text="Número 1:", font=("Arial", 12))
etiqueta_num1.pack(pady=5)
entrada_num1 = tk.Entry(ventana, font=("Arial", 12))
entrada_num1.pack(pady=5)
etiqueta_num2 = tk.Label(ventana, text="Número 2:", font=("Arial", 12))
etiqueta_num2.pack(pady=5)
entrada_num2 = tk.Entry(ventana, font=("Arial", 12))
entrada_num2.pack(pady=5)
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_numeros, font=("Arial", 14))
boton_sumar.pack(pady=10)
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12))
etiqueta_resultado.pack(pady=5)
ventana.mainloop()
