from pathlib import Path
import os
import random

# Programa axuiliar...
# crea un número aleatorio de ficheros al azar, algunos con fechas EEUU
# En su nombre incluye DD-MM-YYYY
# 1 o 2 dígitos para el día, lo mismo para el mes, para el año 2 o 4 dígitos...
FICHEROS_A_CREAR = 500

path_dir_base = Path.cwd() / 'eeuu dates'
path_dir_base.mkdir(exist_ok=True)

import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.printable)
#
# letras = random.choices(string.ascii_letters, k=12)
# print(letras)
# letras = random.sample(string.ascii_letters, 5)
# print(letras)
# letras = ''.join(letras)
# print(letras)


for _ in range(FICHEROS_A_CREAR):
    nombre_fichero = ''

    prefijo_size = random.choice(range(5))
    if prefijo_size:
        letras_prefijo = random.choices(string.ascii_letters, k=prefijo_size)
        nombre_fichero = ''.join(letras_prefijo)

    hay_fecha = random.choice(range(5))
    if hay_fecha <= 2:
        month = random.randint(1, 12)
        day = random.randint(1, 31)

        padding_day, padding_month = random.choices((0, 1), k=2)

        if padding_month:
            month = f'{month:02}'
        else:
            month = f'{month}'

        if padding_day:
            day = f'{day:02}'
        else:
            day = f'{day}'

        year = f'{random.randint(1900, 2099)}'  # El año siempre serán 4 dígitos!!!

        nombre_fichero += f'{month}-{day}-{year}'

    else:
        nombre_fichero += '98'  # para que al menos halla algo!!!

    sufijo_size = random.choice(range(5))
    if sufijo_size:
        letras_sufijo = random.sample(string.ascii_letters, prefijo_size)
        nombre_fichero += ''.join(letras_sufijo)


    with open(path_dir_base / f'{nombre_fichero}.txt', 'w') as file:
        file.write(f'Hola, soy el fichero {nombre_fichero}.txt')
        print(f'Creando el fichero {nombre_fichero}.txt')



