# EJEMPLO PRACTICO

#------------------------------------
# LECTURA DE ARCHIVO
#------------------------------------
# ABRIR UN ARCHIVO
archivo = open("Archivos/archivo.txt", "r")

# LEEMOS TODO EL ARVHIVO DE ENTRADA
linea = archivo.readline()
print(linea)

while linea != '':
    linea = archivo.readline()
    tmp = linea.split(',')
    print(tmp)

# CERRAR ARCHIVO
archivo.close()


#------------------------------------
# ESCRITURA DE ARCHIVO
#------------------------------------
# ABRIR UN ARCHIVO
archivo = open("Archivos/archivo1.txt", "w")

archivo.write("Hola mundo!")

# CERRAR ARCHIVO
archivo.close()