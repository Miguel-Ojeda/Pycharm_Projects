"""
Modify all_lines such that it doesn’t return a string with each iteration, but
rather a tuple.

The tuple should contain four elements:

* the name of the file,
* the current number of the file (from all those returned by os.listdir),
* the line number within the current file,
* and the current line"""

from pathlib import Path

def all_lines_all_files(directorio):
    path = Path(directorio)
    lista_ficheros = path.glob('*')
    for num_fichero, fichero in enumerate(lista_ficheros):
        try:
            with open(fichero, encoding='utf-8') as file_text:
                for index, linea in enumerate(file_text):
                    yield (f'{fichero.name}', f'fichero {num_fichero}', f'línea {index}', linea)
        except:
            pass


directorio = 'files'

for linea in all_lines_all_files(directorio):
    print(linea)




