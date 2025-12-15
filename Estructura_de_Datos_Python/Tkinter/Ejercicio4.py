#Crea un Listbox que muestre una lista de elementos. Agrega un botón para añadir nuevos elementos a la lista.

import tkinter as tk
from tkinter import messagebox

class AplicacionListbox:
    def __init__(self, master):
        self.master = master
        self.master.title("Listbox")
        self.master.geometry("360x300")

        tk.Label(master, text="Elementos:").pack(anchor="w", padx=10, pady=(8,0))

        # Frame para Listbox + scrollbar
        lb_frame = tk.Frame(master)
        lb_frame.pack(fill="both", expand=True, padx=10, pady=6)

        self.listbox = tk.Listbox(lb_frame, height=10)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(lb_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Entrada y botones
        entrada_frame = tk.Frame(master)
        entrada_frame.pack(fill="x", padx=10, pady=(0,10))

        self.entry_nuevo = tk.Entry(entrada_frame)
        self.entry_nuevo.pack(side="left", fill="x", expand=True)

        boton_agregar = tk.Button(entrada_frame, text="Agregar", command=self.agregar_elemento)
        boton_agregar.pack(side="left", padx=(6,0))

        boton_eliminar = tk.Button(master, text="Eliminar seleccionado", command=self.eliminar_seleccionado)
        boton_eliminar.pack(padx=10, pady=(0,8), anchor="e")

        # Opcional: elementos iniciales
        elementos_iniciales = ["Manzana", "Guineo", "Papa", "Pera"]
        for e in elementos_iniciales:
            self.listbox.insert(tk.END, e)

        # Bind Enter para agregar
        self.entry_nuevo.bind("<Return>", lambda event: self.agregar_elemento())

    def agregar_elemento(self):
        texto = self.entry_nuevo.get().strip()
        if not texto:
            messagebox.showwarning("Información", "Ingrese un elemento para agregar.")
            return
        self.listbox.insert(tk.END, texto)
        self.entry_nuevo.delete(0, tk.END)
        self.entry_nuevo.focus_set()

    def eliminar_seleccionado(self):
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "No hay ningún elemento seleccionado.")
            return
        for idx in reversed(seleccion):
            self.listbox.delete(idx)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionListbox(root)
    root.mainloop()