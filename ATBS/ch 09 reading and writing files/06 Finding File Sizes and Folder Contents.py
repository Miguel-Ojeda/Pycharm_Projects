# Finding File Sizes and Folder Contents

import os
from pathlib import Path
# Saber el tamaño de un fichero...
size = os.path.getsize('C:/Windows/System32/calc.exe')
print(size)  # 27648

# Lista los contenidos de un directorio
contenido = os.listdir('C:/Windows/System32')
# Nos devuelve una lista con los contenidos... es muy largo en este caso
print(len(contenido))  # 4789 items en el directorio...

# listdir devuelve una lista con las cadenas de cada uno de los items...
# Veamos los listado del working directory...
contenido = os.listdir('.')
print(contenido)
# ['01 objetos path, usar forward_slash y operador slash.py', '02 cwd y home directory.py', ....
for item in contenido:
    print(item)
# 01 objetos path, usar forward_slash y operador slash.py
# 02 cwd y home directory.py
# 03 creando directorios nuevos.py
# 04 paths abs y rel.py
# 05 obteniendo las partes de un path.py
# 06 Finding File Sizes and Folder Contents.py

# El listado que obtenemos es relativo!!!

# Cuánto ocupan todos los ficheros del directorio actual, por ejemplo??
size = 0
# Contenido ya tiene el nombre de fichero, con lo que la función getsize servirá si están en el working directory
for item in contenido:
    size += os.path.getsize('01 objetos path, usar forward_slash y operador slash.py')
print('El tamaño total de los ficheros del directorio actual es de', size, 'bytes.')

# ¿Cómo hacer lo mismo pero en otro directorio que no sea el working directory?
# En ese caso hay que pasar a getsize la ruta completa...
# Veamos un ejemplo de cómo calcular el tamaño total de los ficheros de 'home'
path = Path.home()
print(path)
listado_ficheros = os.listdir(path)
size = 0
for _, fichero in enumerate(listado_ficheros):
    ruta_completa = path / fichero
    size_fichero = os.path.getsize(ruta_completa)
    # size_fichero = os.path.getsize(fichero) esto no serviría pq los ficheros no están en el CWD
    size += size_fichero
    print(f'Fichero {_}: {fichero} / Tamaño: {size_fichero}')
print(f'El tamaño total de todos los ficheros es de {size} bytes.')

# También se puede hacer lo anterior de manera MÁS COMPLICADO usando siempre el módulo os
# Por ejemplo, para el directorio system32 sería...
totalSize = 0
for filename in os.listdir('C:/Windows/System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
# PERO LO VEO MUCHO MENOS CLARO QUE LA FORMA ANTERIOR

# Además el módulo pathlib tb incluye una método, glob() que permite
# listar contenidos de un directorio, pero con modificadores!!!
# USANDO GLOB PATTERNS, que son algo parecido a regex, pero más simplificado
# método path_object.glob(<expr.>) nos devuelve, para la expresión utilizada,
# un generator que al iterar sobre él nos da los ficheros y directorios que hacen match...
# Ejemplo
path = Path.home()
# Si queremos obtener un generador que incluya todos los ficheros y directorios, utilizaremos la expre. '*'
generator = path.glob('*')
# Los elementos del generador van a ser Path Objects!!
# Para ver el generador podemos hacer una lista y ver lo que hay.l..
lista_path_objects = list(generator)
# Listando elementos de la lista del generador...
print('Listando elementos del generador')
for item in lista_path_objects:
    print(item, repr(item))
# Listando elementos del generador
# C:\Users\Miguel\.afirma WindowsPath('C:/Users/Miguel/.afirma')
# C:\Users\Miguel\.android WindowsPath('C:/Users/Miguel/.android')
# C:\Users\Miguel\.bash_history WindowsPath('C:/Users/Miguel/.bash_history')
# ...

# Si queremos obtener los ficheros pdf de home podríamos hacer
generator_pdf = Path.home().glob('*.pdf')
lista_path_objects_pdf = list(generator_pdf)
print('Listando elementos del generador con los pdf...')
for item in lista_path_objects_pdf:
    print(item, repr(item))
# Listando elementos del generador con los pdf...
# C:\Users\Miguel\Game Development Using Python.pdf WindowsPath('C:/Users/Miguel/Game Development Using Python.pdf')
# C:\Users\Miguel\Game of Life (extraido de new turing omnibus).pdf WindowsPath('C:/Users/Miguel/Game of Life (extraido de new turing omnibus).pdf')

# Expresiones para usar con glob()
# * es cualquier cosa
# ? es cualquier caracter simple

# Podemos iterar directamente sobre el generador, no hace falta convertirlo antes a lista
# Veamos otro ejemplo de como listar todos los txt del directorio windows system32
print('Listando txt de C / win.... system32')
path_object = Path('C:/Windows/System32')
for item in path_object.glob('*.txt'):
    print(item)

# Resumiendo, para listar contenidos de directorios podemos hacerlo tanto con módulo os.listdir() como
# con el método glob de los objetos del pathlib...
# PERO ES MÁS POTENTE EL mÉTODO DEL GLOB, PQ PODEMOS CONFIGURARLO CON EXPRESIONES
# y más sencillo TB!!!




