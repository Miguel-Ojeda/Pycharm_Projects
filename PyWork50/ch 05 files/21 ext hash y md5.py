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



def get_hash_file(file_name):
    with open(file_name, 'rb') as file:
        # read contents of the file
        data = file.read()
        # return hashlib.md5(data).hexdigest()
        return hashlib.md5(data).hexdigest(),\
               hashlib.sha1(data).hexdigest(),\
               hashlib.sha256(data).hexdigest()


def get_hash_directory_files(directory):
    md5_values = {}
    path_directorio = Path(directory)
    for item in path_directorio.glob('*'):
        if not item.is_dir():
            # print(item)
            try:  # Porque hay ficheros protegidos
                hash = get_hash_file(item)
                md5_values[item.name] = {'MD5': hash[0], 'SHA1': hash[1], 'SHA256': hash[2]}
            except:
                pass

    return md5_values

#             return {file.name: find_longest_words(file) for file in path_directorio.glob('*.txt')}

directorio = 'C:/users/Miguel'
fichero_prueba = 'C:/users/Miguel/spam.txt'
resultado = get_hash_file(fichero_prueba)
pprint.pprint(resultado)
resultado = get_hash_directory_files(directorio)
pprint.pprint(resultado)



# resultado = get_md5(directorio)
# pprint.pprint(resultado)


print('\n\nReuven-------------------------------')
resultado = md5_files_Reuven(directorio)
pprint.pprint(resultado)