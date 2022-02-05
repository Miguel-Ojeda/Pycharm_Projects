'''
Ask the user for a directory name.
Show all of the files in the directory, as well as how long ago the directory was modified.
You will probably want to use a combination of os.stat and the
Arrow package on PyPI (http://mng.bz/nPPK) to do this easily.
'''

import os
import pprint
import arrow   # Librería para manejo más sencillo del tiempo

from stat import *

def mod_times(dirname):
    output = {}

    for one_filename in Path(dirname).glob('*'):
        try:
            stat_result = os.stat(one_filename)
            modification_time = stat_result.st_mtime
            # Es el tiempo de la última modificación (tiempo como siempre en segundos desde el UNIX epoch
            # Con arrow podemos pasar de segundos a días, por ejemplo...
            tiempo_dias = (arrow.now() - arrow.get(modification_time)).days
            output[one_filename] = f'{tiempo_dias} días'

        except:
            pass

    return output


from pathlib import Path



#
# directorio = 'C:/users/Miguel'
# fichero_prueba = 'C:/users/Miguel/spam.txt'
# resultado = get_hash_file(fichero_prueba)
# pprint.pprint(resultado)
# resultado = get_hash_directory_files(directorio)
# pprint.pprint(resultado)

directorio = 'C:/users/Miguel'
resultado = mod_times(directorio)
pprint.pprint(resultado)
