import os
from pathlib import Path
import re
import shutil

path_dir_base = Path.cwd() / 'eeuu dates'
# Aquí es donde están los ficheros con fechas americanas...
# Algunos ficheros son normales, pero otros contienen en su nombre alguna fecha del tipo
# DD-MM-YYYY  (fechas americanas)
# 1 o 2 dígitos para el día, lo mismo para el mes, EL AÑO SIEMPRE 4 o dos dígitos!!

# Para obtener ficheros con nombres aleatorios pprimero ejecutar project aux.py

# primero habrá que detectar las fechas... con una expresión regular...

usa_date_regex = '''^(.*?)              #Puede haber algo al principio, modo non-greedy con ?
                    ((0|1)?\d)-         # esto sería el mes
                    ((0|1|2|3)?\d)-     # esto sería el día
                    ((19|20)\d\d)       # esto sería el año
                    (.*?)$              # puede haber luego cualquier cosa hasta fin, non-greedy con ?
'''

pattern = re.compile(usa_date_regex, re.VERBOSE)

pack_ficheros = path_dir_base.glob('*.*')

for file in pack_ficheros:
    match_obj = pattern.search(file.name)
    if match_obj:
        prefijo = match_obj.group(1)
        month = match_obj.group(2)
        day = match_obj.group(4)
        year = match_obj.group(6)
        sufijo = match_obj.group(8)
        print(str(file.name), f'----> Pre: {prefijo}, dia: {day}, mes: {month}, year: {year}, sufijo: {sufijo}')
        euro_name = ''.join([prefijo, day, '-', month, '-', year, sufijo])
        dest_path = path_dir_base / euro_name
        print(f'Renombrando a ---> {euro_name}')
        # Tengo que poner el path completo, si no da error pq supone que es en el working directory...
        shutil.move(path_dir_base / file.name, path_dir_base / euro_name)

        # os.rename()
        # print('renombrando a ->')
    else:
        # print(file.name)
        pass
