'''
Use os.listdir (http://mng.bz/YreB) to get the names of files in the current
directory. What file extensions (i.e., suffixes following the final . character)
appear in that directory? It’ll probably be helpful to use os.path.splitext
(http://mng.bz/GV4v).

NOTA... The scandir() function returns directory entries along with file attribute information,
giving better performance for many common use cases.
'''
'''
os.listdir(path='.')
Return a list containing the names of the entries in the directory given by path.
The list is in arbitrary order, and does not include the special entries '.' and '..'
even if they are present in the directory.
If a file is removed from or added to the directory during the call of this function,
whether a name for that file be included is unspecified.
'''

import os
import os.path
import pprint


def lista_extensiones(directorio):
    extensiones = set()
    lista_ficheros = os.listdir(directorio)
    for file in lista_ficheros:
        extension = os.path.splitext(file)[1]
        extensiones.add(extension)

    return extensiones


# Igual que lo anterior, pero abreviando...
def lista_extensiones_v2(directorio):
    extensiones = set()
    for file in os.listdir(directorio):
        extensiones.add(os.path.splitext(file)[1])

    return extensiones

# Con set comprehensions... no me gusta demasiado, la verdad...
# Es la solución de Reuven... quizás sea cuestión de acostumbrarse....
def lista_extensiones_v3(directorio):
    return {os.path.splitext(file)[1] for file in os.listdir(directorio)}


path_dir = os.environ['HOMEPATH']
extensiones = lista_extensiones_v3(path_dir)
pprint.pprint(extensiones)




