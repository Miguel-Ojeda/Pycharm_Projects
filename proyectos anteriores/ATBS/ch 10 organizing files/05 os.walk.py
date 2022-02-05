'''
Con os.walk podemos recorrer recursivamente un árbol de directorios,
mostrando todos los archivos y carpetas...
Veamos como funciona con la estructura de directorios creada para el ejemplo...
Esta función devuelve un iterador, de una tupla de 3 elementos...
os.walk() -> Iterator[tuple]
Al ir iterando, la tupla va cambiando...
        (
        carpeta_actual ..... cada una de las carpetas del árbol
        lista_de_subdirectorios que están en esa carpeta actual, (es una lista de strings!!)
        lista_de_ficheros que están en esa carpeta (es una lista de strings!!)
        )
'''

import os
from pathlib import Path

path = Path('ejemplo_os.walk')

for index, (folder_name, lista_subdirs, lista_files) in enumerate(os.walk(path)):
    print(index, 'dir->', folder_name, '\tsubdirs->', lista_subdirs, '\tfiles->', lista_files)

# 0 dir-> ejemplo_os.walk 	subdirs-> ['cats', 'dogs', 'pilotos'] 	files-> ['bacon.txt', 'eggs.txt', 'spam.txt']
# 1 dir-> ejemplo_os.walk\cats 	subdirs-> [] 	files-> ['Jerry.txt', 'Tom.jpg', 'Tom.txt']
# 2 dir-> ejemplo_os.walk\dogs 	subdirs-> ['Legends'] 	files-> ['boxi.txt', 'trudot.txt']
# 3 dir-> ejemplo_os.walk\dogs\Legends 	subdirs-> [] 	files-> ['Milu.txt', 'RinTinTin.txt']
# 4 dir-> ejemplo_os.walk\pilotos 	subdirs-> ['f1', 'motogp'] 	files-> []
# 5 dir-> ejemplo_os.walk\pilotos\f1 	subdirs-> [] 	files-> ['alonso.txt', 'hamilton.txt', 'sainz.txt']
# 6 dir-> ejemplo_os.walk\pilotos\motogp 	subdirs-> ['legend'] 	files-> ['bagnaia.txt', 'marquez.txt', 'quartararo.txt']
# 7 dir-> ejemplo_os.walk\pilotos\motogp\legend 	subdirs-> [] 	files-> ['_____Angel Nieto_____.txt']

# Veamos que hay tantos elementos en el iterador como carpetas distintas...
# En cada paso, mostramos:
#           La carpeta en la que estamos (empezando por la inicial),
#           La lista de subdirectorios que hay en esa carpeta
#           La lista de ficheros que hay en esa carpeta...

# Veamos otra salida posible...
# Para cada una de las 8 carpetas principales por las que va pasando el iterator, mostraremos sus carpetas y sus files
for index, (folder_name, lista_subdirs, lista_files) in enumerate(os.walk(path)):
# for folder_name, lista_subdirs, lista_files in enumerate(os.walk(path)):
    print(f'Carpeta {index + 1} -->  "{folder_name}"')
    # Ahora mostremos las carpetas que contiene
    print('\tLas subcarpetas que contiene son: ', end='')
    for carpeta in lista_subdirs:
        print(f'{carpeta}, ', end='')
    print()
    print('\tLos ficheros que contiene son: ', end='')
    for file in lista_files:
        print(f'{file}, ', end='')
    print()

    print()

# Salida --->
# Carpeta 1 -->  "ejemplo_os.walk"
# 	Las subcarpetas que contiene son: cats, dogs, pilotos,
# 	Los ficheros que contiene son: bacon.txt, eggs.txt, spam.txt,
#
# Carpeta 2 -->  "ejemplo_os.walk\cats"
# 	Las subcarpetas que contiene son:
# 	Los ficheros que contiene son: Jerry.txt, Tom.jpg, Tom.txt,
#
# Carpeta 3 -->  "ejemplo_os.walk\dogs"
# 	Las subcarpetas que contiene son: Legends,
# 	Los ficheros que contiene son: boxi.txt, trudot.txt,
#
# Carpeta 4 -->  "ejemplo_os.walk\dogs\Legends"
# 	Las subcarpetas que contiene son:
# 	Los ficheros que contiene son: Milu.txt, RinTinTin.txt,
#
# Carpeta 5 -->  "ejemplo_os.walk\pilotos"
# 	Las subcarpetas que contiene son: f1, motogp,
# 	Los ficheros que contiene son:
#
# Carpeta 6 -->  "ejemplo_os.walk\pilotos\f1"
# 	Las subcarpetas que contiene son:
# 	Los ficheros que contiene son: alonso.txt, hamilton.txt, sainz.txt,
#
# Carpeta 7 -->  "ejemplo_os.walk\pilotos\motogp"
# 	Las subcarpetas que contiene son: legend,
# 	Los ficheros que contiene son: bagnaia.txt, marquez.txt, quartararo.txt,
#
# Carpeta 8 -->  "ejemplo_os.walk\pilotos\motogp\legend"
# 	Las subcarpetas que contiene son:
# 	Los ficheros que contiene son: _____Angel Nieto_____.txt