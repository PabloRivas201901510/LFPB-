
from enum import Enum

class tipos_controles(Enum):
    Etiqueta = 1,
    Boton = 2,
    Check = 3,
    Contenedor = 4


class Control:
    def __init__(self, _nombre, _tipo):
        self.nombre = _nombre 
        self.tipo = _tipo
        self.valor = ""
        self.contenedor = None


    def getName(self):
        return self.nombre

    def setContenedor(self, name):
        self.contenedor = name

    def imprimir(self):
        print(self.nombre, " | ", self.tipo, " | ", self.valor, " | ", self.contenedor)



def addContenedor(Contenedor:Control, Controlador:Control):
    if Contenedor == "this":
        Controlador.setContenedor("this")
    else:
        name1 = Contenedor.getName()
        Controlador.setContenedor(name1)

lista_controles = []

a = Control("Etiqueta1", tipos_controles.Etiqueta)
lista_controles.append(a)
b = Control("Contenedor1", tipos_controles.Contenedor)
lista_controles.append(b)

addContenedor(b, a)
addContenedor("this", b)


# ID.add(ID)
# Contenedor1.add(Etiqueta1)



for i in lista_controles:
    i.imprimir()






