"""
Create a dict whose keys are filenames and whose values are the lengths of the
files. The input can be a list of files from os.listdir (http://mng.bz/YreB) or
glob.glob (http://mng.bz/044N)

A la función le pasamos, simplemente, el directorio base!!
Hay que listar todos los ficheros, con su tamaño (si es directorio, pues no)
"""
import pprint
from pathlib import Path
import stat


def get_dict_file_size(directorio):
    return {fichero: fichero.stat().st_size
            for fichero in Path(directorio).glob('*')
            if fichero.is_file()
            }


directorio = Path('D:/Documentos')
resultado = get_dict_file_size(directorio)
pprint.pprint(resultado)

