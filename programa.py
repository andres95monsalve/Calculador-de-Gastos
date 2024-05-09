import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RegistroGastos:
    def __init__(self):
        self.gastos_diarios = {}

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos_diarios:
            self.gastos_diarios[categoria] += monto
        else:
            self.gastos_diarios[categoria] = monto

    def mostrar_gastos(self):
        ventana_resultados = tk.Toplevel()
        ventana_resultados.title("Gastos Detallados")
        ventana_resultados.geometry("270x90")  
        centrar_ventana(ventana_resultados)  

        for categoria, monto in self.gastos_diarios.items():
            tk.Label(ventana_resultados, text=f'{categoria}: ${monto}').pack()

        total = sum(self.gastos_diarios.values())
        tk.Label(ventana_resultados, text=f'Total: ${total}').pack()

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

def registrar_gasto(registro, categoria_entry, monto_entry):
    categoria = categoria_entry.get()
    monto = float(monto_entry.get())
    registro.agregar_gasto(categoria, monto)
    categoria_entry.delete(0, tk.END)
    monto_entry.delete(0, tk.END)

def salir(ventana):
    confirmacion = messagebox.askokcancel("Confirmar", "¿Estás seguro de que quieres salir?")
    if confirmacion:
        ventana.destroy()

def main():
    registro = RegistroGastos()

    ventana = tk.Tk()
    ventana.title("Registro de Gastos")
    ventana.geometry("300x200")  
    centrar_ventana(ventana)  

    imagen = Image.open("logo.jpg")
    imagen = imagen.resize((32, 32))  
    icono = ImageTk.PhotoImage(imagen)
    ventana.iconphoto(True, icono)

    label_logo = tk.Label(ventana, image=icono)
    label_logo.pack()

    label_categoria = tk.Label(ventana, text="Categoría del gasto:")
    label_categoria.pack()
    categoria_entry = tk.Entry(ventana)
    categoria_entry.pack()

    label_monto = tk.Label(ventana, text="Monto del gasto:")
    label_monto.pack()
    monto_entry = tk.Entry(ventana)
    monto_entry.pack()

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=5)  

    boton_agregar = tk.Button(frame_botones, text="Agregar Gasto",
                              command=lambda: registrar_gasto(registro, categoria_entry, monto_entry))
    boton_agregar.pack(side=tk.LEFT, padx=5)  

    boton_mostrar = tk.Button(frame_botones, text="Mostrar Gastos", command=registro.mostrar_gastos)
    boton_mostrar.pack(side=tk.LEFT, padx=5)  

    frame_salir = tk.Frame(ventana)
    frame_salir.pack(pady=5)

    boton_salir = tk.Button(frame_salir, text="Salir", command=lambda: salir(ventana))
    boton_salir.pack()  

    ventana.mainloop()

if __name__ == '__main__':
    main()
