#Diseña una interfaz con un Canvas donde el usuario pueda dibujar líneas manteniendo presionado el botón del mouse.
import tkinter as tk
class AplicacionDibujo:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizarra")
        self.master.geometry("600x400")
        self.canvas = tk.Canvas(self.master, bg="Black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.iniciar_dibujo)
        self.canvas.bind("<B1-Motion>", self.dibujar)
        self.ultimo_x, self.ultimo_y = None, None
    def iniciar_dibujo(self, event):
        self.ultimo_x, self.ultimo_y = event.x, event.y
    def dibujar(self, event):
        if self.ultimo_x is not None and self.ultimo_y is not None:
            self.canvas.create_line(self.ultimo_x, self.ultimo_y, event.x, event.y, fill="White", width=2)
        self.ultimo_x, self.ultimo_y = event.x, event.y
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionDibujo(root)
    root.mainloop()
    