
import tkinter as tk

def dest(_ven):
    _ven.destroy()

def enviarInformacion(_ventana, _nombre, _apellido, _edad, _genero):
    _ventana = tk.Toplevel()
    _ventana.geometry('500x500')
    tk.Label(_ventana, text='INFORMACION DEL USUARIO').place(x=50, y=275)
    tk.Label(_ventana, text='Mi nombre es').place(x=50, y=300)
    tk.Label(_ventana, textvariable=_nombre).place(x=150, y=300)
    tk.Label(_ventana, text='Mi Apellido es').place(x=50, y=325)
    tk.Label(_ventana, textvariable=_apellido).place(x=150, y=325)
    tk.Label(_ventana, text='Mi edad es').place(x=50, y=350)
    tk.Label(_ventana, textvariable=_edad).place(x=150, y=350)
    tk.Label(_ventana, text='Mi genero es').place(x=50, y=375)
    tk.Label(_ventana, textvariable=_genero).place(x=150, y=375)
    tk.Button(_ventana, text='CERRAR', command= lambda : dest(_ventana)).place(x=50, y=50)
    _ventana.mainloop()


if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.geometry('500x500')
    ventana.title('Ejemplo clase 4')

    tk.Label(ventana, text='Nombre: ').place(x=50, y=50)
    tk.Label(ventana, text='Apellido: ').place(x=50, y=75)
    tk.Label(ventana, text='Edad: ').place(x=50, y=100)
    tk.Label(ventana, text='Genero: ').place(x=50, y=125)

    nombre = tk.StringVar()
    apellido = tk.StringVar()
    edad = tk.StringVar()
    genero = tk.StringVar()
    tk.Entry(ventana, textvariable=nombre).place(x=150, y=50)
    tk.Entry(ventana, textvariable=apellido).place(x=150, y=75)
    tk.Entry(ventana, textvariable=edad).place(x=150, y=100)
    tk.Entry(ventana, textvariable=genero).place(x=150, y=125)

    tk.Button(ventana, text='Enviar', command= lambda : enviarInformacion(ventana, nombre, apellido, edad, genero)).place(x=300, y=125)

    ventana.mainloop()


# pip 

# pip install pyinstaller

# pyinstaller  tu_script.py




