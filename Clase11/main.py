from enum import Enum




class Analizador:
    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.tmp_cadena = ""
        self.lista_cadena = []
        self.EstadoActual = 0

    def aumentarLinea(self):
        _tmp = self.lista_cadena[self.linea]
        #print(_tmp , " == ", self.tmp_cadena)
        if _tmp == self.tmp_cadena:
            self.linea += 1
            self.tmp_cadena = ""
            self.columna = 0 

    def verificarToken(self, entrada:str, token:str):
        count = 0

        for i in range(0, len(token)):
            if count >= len(entrada):
                return {"result":None, "count":count}
            if entrada[i] != token[i]:
                return {"result":None, "count":count}
            count += 1

        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1

        self.tmp_cadena += token

        return {"result":nueva_cadena, "count":count}

    def quitar(self, entrada:str, token:str):
        nueva_cadena = ""
        count_1 = 0
        lista = entrada.split(token)
        for j in lista:
            if count_1 == len(lista) - 1:
                nueva_cadena += j
            elif count_1 > 0:
                nueva_cadena += j + token

            count_1 += 1
        return nueva_cadena


    def verificarID(self, entrada:str):
        count = 0
        llave = False
        alfabeto = ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "_"]
        for i in entrada:
            llave = False
            for j in alfabeto:
                if i == j:
                    llave = True
                    break
            if llave == False:
                return {"result":None, "count":count}

            count += 1

        return {"result":True, "count":count}

        


    def lecturaporEstados(self, cadena):
        self.EstadoActual = "Q0"

        while cadena != "":

            if self.EstadoActual == "Q0":
                token = "<"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "A"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "A":
                token = "!"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "B"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "B":
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "C"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "C":
                token = "-"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "D"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "D":
                token = "Controles"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "E"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "E":
                token = ">"
                res = self.verificarToken(cadena, token)
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break
                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                self.EstadoActual = "F"
                #aumentar linea
                self.aumentarLinea()

            elif self.EstadoActual == "F":
                token = "<"
                res = self.verificarToken(cadena, token)
               
                if res["result"] == None:
                    tokens = ["Boton", "Texto", "Contenedor"]
                    
                    for i in tokens:
                        res = self.verificarToken(cadena, i)
                        if res["result"] != None:
                            token = i
                            self.EstadoActual = "H"
                            break
                else:
                    self.EstadoActual = "G"
                
                #VERIFICAR ERROR
                if res["result"] == None:
                    print("ERROR")
                    break

                print( self.linea, " | ", self.columna," | ",  token)
                cadena = res["result"]
                self.columna += res["count"]
                #aumentar linea
                
                self.aumentarLinea()
                

            elif self.EstadoActual == "H":
                tmp = cadena.split(";")
                id = tmp[0]
                print(self.verificarID(id))
                cadena = self.quitar(cadena, id)
                print("--> ",cadena)
                break
                    

    def compile(self):
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open("entrada.gpw", "r")
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

        #print("-------------------")
        #print(nueva_cadena)
        #print("-------------------")
        #print(lista_cadena)

        self.lista_cadena = lista_cadena
        self.lecturaporEstados(nueva_cadena)


a = Analizador()
a.compile()