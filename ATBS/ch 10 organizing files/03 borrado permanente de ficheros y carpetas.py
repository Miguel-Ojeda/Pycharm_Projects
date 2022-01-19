# Tenemos opciones con os y con shutil
import os
import shutil
from pathlib import Path
'''
os.unlink(path) will delete the file at path.
os.rmdir(path) will delete the folder at path. This folder must be empty!!
shutil.rmtree(path) will remove the folder at path,
and all files and folders it contains will also be deleted.
OBS. QUE shutil no tiene para borrar 1 ficheros!!!
'''

# Ejemplo, borrar todos los ficheros *.rxt de nuestro home
'''
path = Path.home()
paths_ficheros_rxt = path.glob('*.rxt')
for fichero in paths_ficheros_rxt:
    print(f'Borrando fichero {str(fichero)}')
    os.unlink(fichero)
'''


