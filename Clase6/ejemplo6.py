# CLASE 6

# IMPORTAR LIBRERIA RE
import re


# COMPILADOR EXPRESIONES REGULARES
patron = re.compile(r'bar foo')

text = """ bar foo bar
foo barbar foo
foofoo foo bar
"""

# SEARCH nos devuelvela coincidencia en cualquier ubicacion
s = patron.search(text)
print("serch -> ", s)

# FINDALL nos devuelve una lista con todas las coincidencias, pero solo los caracteres
fa = patron.findall(text)
print("finfall -> ", fa)

# FINDINTER nos devuelve una lista con todas las coincidencias, pero con sus atributos
fi = patron.finditer(text)
print("findinter -> ", fi)

# GRUOP(): devuelve la coincidencia con la expresion regular
# START(): devuelve la posicion inicial de la coincidencia
# END(): devuelve la posicion final de la coincidencia
# SPAN(): devuelve una tupla con la posicion incial y final de la coincidencia
for i in fi:
    print("group-> ", i.group(), " | start-> ", i.start(), " | end-> ", i.end(), " | span-> ", i.span())