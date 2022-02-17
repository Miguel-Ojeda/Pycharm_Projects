"""
The current version of all_lines returns all of the lines from the first file, then
all of the lines from the second file, and so forth.

Modify the function such that it returns the first line from each file,
and then the second line from each file, until all lines from all files are returned.

When you finish printing lines from shorter files, ignore those files while continuing
to display lines from the longer files.
"""
'''
Creo que mi solución es mucho mejor que la de Reuven
Además él elimina elementos de la lista mientras itera sobre ellos (creo que fallaría)
Yo para evitar esto creo una shallow copy...
Además, antes de nada elimino los ficheros None,... no como él que los mete en un if que se ejecuta siempre...
Aquí lo que tenemos que hacer, es cuando el resultado de hacer readline sea none
significará que ya hemos leído todo_ el fichero, y, por lo tanto, habrá que removerlo de la lista de ficheros...
'''

from pathlib import Path


def try_open(path_fichero):
    # Nos devuelve el manejador del fichero (o None, si no puede abrir)
    try:
        file = open(path_fichero, encoding='utf-8')
        return file
    except:
        return None



def all_lines_all_files_alt(directorio):
    path = Path(directorio)
    lista_path_ficheros = path.glob('*')
    # 1º obtenemos una lista con todos los manejadores de ficheros
    # si no se puede abrir será None
    files = [try_open(path_fichero)
             for path_fichero in lista_path_ficheros]
    # quitamos los ficheros que no pudimos abrir (o sea, donde file es distinto de None)
    files = [file
             for file in files
             if file]

    while files:  # mientras quede algún fichero activo en la lista....
        lista_de_ficheros_con_contenido = files.copy()  # Shallow copy
        for file in lista_de_ficheros_con_contenido:
            linea = file.readline()
            if linea:
                yield linea
            else:
                files.remove(file)



directorio = 'files'

for linea in all_lines_all_files_alt(directorio):
    print(linea)