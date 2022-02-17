"""
Modify all_lines such that it takes two arguments—a directory name, and a
string. Only those lines containing the string (i.e., for which you can say s in
line) should be returned. If you know how to work with regular expressions
and Python’s re module, then you could even make the match conditional on a
regular expression.
"""

# Pues es fácil, es como 48 all lines pero cambiando la línea del yield... poniendo una condición
from pathlib import Path

def all_lines_all_files(directorio, string):
    path = Path(directorio)
    lista_ficheros = path.glob('*')
    for fichero in lista_ficheros:
        try:
            with open(fichero, encoding='utf-8') as file_text:
                for linea in file_text:
                    # esta es la línea que añadí... el if...
                    if string in linea:
                        yield linea
        except:
            pass
