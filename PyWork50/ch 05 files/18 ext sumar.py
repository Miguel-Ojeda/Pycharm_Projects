'''
Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.
'''
# import string
from io import StringIO   # Para pruebas!!!

fake_file = StringIO('''
Hola 24 que tal 23 está hoy 02
y luego 03 y 4 y 29 y 30 estarán hoy 0.8
''')



def suma_enteros(filename):
    suma = 0
    # for linea in open(filename):
    for linea in fake_file:
        for palabra in linea.split():
            if palabra.isdecimal():
                suma += int(palabra)

    return suma


print(suma_enteros('lo que sea'))
