'''
Use the hashlib module in the Python standard library, and the md5 function within it,
to calculate the MD5 hash for the contents of every file in a user specified directory.
Then print all the filenames and their MD5 hashes
'''
import pprint
from pathlib import Path
import hashlib

'''
# Comprobado con una página online y parece que es correcto los hashes...
# La solución de Reuven creo que está mal, creo que simplemente calcula el hash del nombre de los ficheros!!
def md5_files(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass
            
    return output
'''


import glob
# La solución de Reuven creo que está mal, creo que simplemente calcula el hash del nombre de los ficheros!!
# Además comprobé con herramienta online y vi que , efectivamente mi implementación está bine
# y esta no
def md5_files_Reuven(dirname):
    output = {}
    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass

    return output


def get_hash_file_v1(file_name):
    with open(file_name, 'rb') as file:
        # read contents of the file
        data = file.read()
        # return hashlib.md5(data).hexdigest()
        return {'MD5': hashlib.md5(data).hexdigest(),
                'SHA1': hashlib.sha1(data).hexdigest(),
                'SHA256': hashlib.sha256(data).hexdigest()
                }


def get_hash_file_v2(file_name):
    """A veces el fichero es demasiado grande...
    En ese caso podemos ir leyendo poco a poco y pasándolos a la función hash...
    """
    hash_md5 = hashlib.md5()
    hash_sha1 = hashlib.sha1()
    hash_sha256 = hashlib.sha256()

    with open(file_name, 'rb') as file:
        # for chunk in file.read(4096):  esto no sirve!!! no genera un iterador!!!
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hash_md5.update(chunk)
            hash_sha256.update(chunk)
            hash_sha1.update(chunk)

    return {'MD5': hash_md5.hexdigest(),
            'SHA1': hash_sha1.hexdigest(),
            'SHA256': hash_sha256.hexdigest()}


'''
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
'''


def get_hash_directory_files(directory):
    hash_values = {}
    path_directorio = Path(directory)
    for item in path_directorio.glob('*'):
        if not item.is_dir():
            # print(item)
            try:  # Porque hay ficheros protegidos
                # hash_item = get_hash_file_v1(item)
                hash_item = get_hash_file_v2(item)
                hash_values[item.name] = hash_item
            except:
                pass

    return hash_values


#             return {file.name: find_longest_words(file) for file in path_directorio.glob('*.txt')}

directorio = 'C:/users/Miguel'
fichero_prueba = 'C:/users/Miguel/spam.txt'
# resultado = get_hash_file_v1(fichero_prueba)
# pprint.pprint(resultado)
# resultado_2 = get_hash_file_v2(fichero_prueba)
# pprint.pprint(resultado_2)
resultado = get_hash_directory_files(directorio)
pprint.pprint(resultado)
