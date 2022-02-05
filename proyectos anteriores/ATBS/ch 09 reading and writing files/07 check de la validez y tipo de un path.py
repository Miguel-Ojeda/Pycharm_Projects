# Con un objeto Path tenemos 3 métodos interesantes:
# paht_object.exists() returns True if the path exists or returns False if it
# path_object.is_file() returns True if the path exists and is a file, or returns
# path_object.is_dir()
from pathlib import Path
import os

# Ejemplo: Listar los contenidos del directorio Descargas
# indicando si es directorio o fichero
# En el caso de que sea un fichero poner tb su tamaño y agregarlo para el total

total_size = 0
path_documentos = Path.home() / 'Downloads'
print('Mostrando los contenidos del directorio', path_documentos)
for path_obj in path_documentos.glob('*'):
    if path_obj.is_dir():
        print(f'----> Directorio: {path_obj}')
    else:
        size = os.path.getsize(path_obj)
        print(f'----> Fichero: {path_obj}, con tamaño {os.path.getsize(path_obj)}.')
        total_size += size
print(f'\nEl tamaño total de los ficheros del directorio es de {total_size:_} bytes.')
