# IMPORTAR LA LIBRERIA
import tkinter as tk

def metodo1(ventana):
    tk.Label(ventana, text="Aparezco", font=("Arial Black", 16), fg="Blue").grid(row=0, column=0)
    

# CREAR VENTANA
ventana = tk.Tk()

# TITULO DE VENTANA
ventana.title("Ejemplo Practico")

# TAMAÑO DE VENTANA
ventana.geometry('1000x500')

# Etiquetas
texto_mod = tk.StringVar()
lbl1 = tk.Label(ventana, textvariable=texto_mod, font=("Arial Black", 16), fg="Blue")
lbl1.place(x= 100 , y= 100)
texto_mod.set("Saludo")

lbl2 = tk.Label(ventana, text="Adios estudiantes de LFP B-")
lbl2.grid(row=0, column=1)

# Entradas
texto_mod_entry1 = tk.StringVar()
texto_mod_entry1.set("Hola")
tk.Entry(ventana, textvariable=texto_mod_entry1, font=("Arial Black", 16)).place(x= 200 , y= 100)

# Botones
tk.Button(ventana, text="Enviar", font=("Arial Black", 16), command=lambda : metodo1(ventana)).place(x= 600 , y= 100)

# ABRIR LA VENTA
ventana.mainloop()