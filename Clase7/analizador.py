# CLASE 7 - ANALIZADOR LEXICO
# AUTOR: PABLO DANIEL RIVAS MARROQUIN

from enum import Enum
from lib2to3.pgen2 import token
import re

class L_tokens(Enum):
    TK_MENOR = "<"
    TK_E_NUMERO = "Numero"
    TK_MAYOR = ">"
    TK_NUMERO = "[0-9]*"
    TK_BARRAINV = "/"
    TK_E_OPERACION = "Operacion"
    TK_IGUAL = "="
    TK_OP_SUMA = "SUMA",
    TK_OP_RESTA = "RESTA"
    TK_E_TIPO = "Tipo"


class Analizador:
    def __init__(self):
        self.cadena = ""
        self.linea = 0
        self.columna = 0  
        self.lista_cadena = []
        self.tmp_cadena = ""

    def quitar(self, _cadena :str, _num : int):
        _tmp = ""
        count = 0
        for i in _cadena:
            if count >= _num:
                _tmp += i
            else:
                self.tmp_cadena += i 
            count += 1
        return _tmp

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea]
        #print(_tmp , " == ", self.tmp_cadena)
        if _tmp == self.tmp_cadena:
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 0 

    def esLaetiqueta(self, _cadena : str, _etiqueta : str):
        tmp = ""
        count = 0
        for i in _cadena:
            if count < len(_etiqueta):
                tmp += i
            count += 1

        if tmp == _etiqueta:
            return True
        else:
            return False

    def Numero(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_NUMERO.value,         # 10
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""

        for i in tokens:
            try:
                patron = re.compile(f'^{i}')
                s = patron.search(_cadena)
                print("| ", self.linea, " | ", self.columna, " | ", s.group())
                self.columna += int(s.end())
                # GUARDAR EL TOKEN
                if i == L_tokens.TK_NUMERO.value:
                    _numero = s.group()
                _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Operacion(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_IGUAL.value,              # =
            "OPERADOR",                     # OPERADOR
            L_tokens.TK_MAYOR.value,        # >
            "NUMERO",                       # NUMERO
            "NUMERO",                       # NUMERO
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_OPERACION.value,  # Operacion
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""
        _operador = None
        for i in tokens:
            try:
                if "NUMERO" == i:
                    if self.esLaetiqueta(_cadena, "<Numero>"):
                        _result = self.Numero(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}

                    elif self.esLaetiqueta(_cadena, "<Operacion="):
                        _result = self.Operacion(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}
                    else:
                        # GUARDAR ERROR
                        print("Ocurrio un error")
                        return {'resultado':_numero, "cadena":_cadena, "Error": True}
                
                else:
                    if "OPERADOR" == i:
                        # SUMA
                        spatron = re.compile(f'^SUMA')
                        t = spatron.search(_cadena)
                        #print("OPERADOR -> ", t)
                        if t != None:
                            i = "SUMA"
                            _operador = L_tokens.TK_OP_SUMA

                        # RESTA
                        spatron = re.compile(f'^RESTA')
                        t = spatron.search(_cadena)
                        if t != None:
                            i = "RESTA"
                            _operador = L_tokens.TK_OP_RESTA

                        if _operador == None:
                            # GUARDAR ERROR
                            print("Ocurrio un error Operacion")
                            return {'resultado':_numero, "cadena":_cadena, "Error": True}

                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    # GUARDAR EL TOKEN
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        # NUMERO1 OPERADOR NUMERO2
        return {'resultado':_numero, "cadena":_cadena, "Error":False}

    def Tipo(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
            "OPERACIONES",                  # OPERACIONES
            L_tokens.TK_MENOR.value,        # <
            L_tokens.TK_BARRAINV.value,     # /
            L_tokens.TK_E_TIPO.value,       # Tipo
            L_tokens.TK_MAYOR.value,        # >
        ]
        _numero = ""

        for i in tokens:
            try:
                
                if "OPERACIONES" == i:
                    salida = True
                    while salida:
                        print("--------------------------------")
                        _result = self.Operacion(_cadena)
                        _cadena = _result['cadena']
                        if _result['Error']:
                            # GUARDAR ERROR
                            print("Ocurrio un error")
                        
                        if self.esLaetiqueta(_cadena, "</Tipo>"):
                            salida = False
                else:
                    patron = re.compile(f'^{i}')
                    s = patron.search(_cadena)
                    # GUARDAR EL TOKEN
                    print("| ", self.linea, " | ", self.columna, " | ", s.group())
                    self.columna += int(s.end())
                    _cadena = self.quitar(_cadena, s.end())
                self.aumentarLinea()
            except:
                # GUARDAR ERROR
                print("Ocurrio un error")
                return {'resultado':_numero, "cadena":_cadena, "Error": True}

        return {'resultado':_numero, "cadena":_cadena, "Error": False}

    def compile(self):
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open("entrada.txt", "r")
        contenido = archivo.readlines()
        archivo.close()

        

        # LIMPIAR MI ENTRADA
        nueva_cadena = ""
        lista_cadena = []

        

        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)

        print(nueva_cadena)
        print(lista_cadena)

        self.lista_cadena = lista_cadena

        print(self.Tipo(nueva_cadena))


Analizador().compile()


#8+9*(8-9-6)