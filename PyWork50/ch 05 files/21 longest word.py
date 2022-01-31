'''
In this exercise, write two functions. find_longest_word takes a filename as an
argument and returns the longest word found in the file. The second function, find-
_all_longest_words, takes a directory name and returns a dict in which the keys are
filenames and the values are the longest words from each file.

NOTE There are several ways to solve this problem. If you already know how
to use comprehensions, and particularly dict comprehensions, then that’s
probably the most Pythonic approach. But if you aren’t yet comfortable with
them, and would prefer not to jump to read about them in chapter 7, then no
worries—you can use a traditional for loop, and you’ll be just fine
'''


from io import StringIO
import pprint
from pathlib import Path

fake_file = StringIO('''This is a test file.

It contains 28 words and 20 different words.

It also contains 165 characters.

It also contains 11 lines.

It is also self-referential.

self-referencial- y también auto-referencial*

Wow!''')



def find_longest_words(filename):
    output = {'max_longitud': 0, 'palabras_mas_largas': []}
    with open(filename, encoding='UTF-8') as file:
        for linea in file:
            for palabra in linea.split():
                if len(palabra) > output['max_longitud']:
                    output['max_longitud'] = len(palabra)
                    output['palabras_mas_largas'] = [palabra]
                elif len(palabra) == output['max_longitud']:
                    output['palabras_mas_largas'].append(palabra)

    return output


def find_all_longest_words(directory):
    ''' mira en cada fichero cuál es la palabra más larga...
    '''
    resultado = dict()
    # Devolveremos un diccionario, cuyas claves van a ser los nombres de los ficheros
    # y sus values el diccionario que devuelve la función find_longest_word
    path_directorio = Path(directory)
    # Por si acaso, sólo miramos en los que tienen extensión txt

    '''
    Opción 1:
    lista_de_ficheros = path_directorio.glob('*.txt')
    for file in lista_de_ficheros:
        resultado[file.name] = find_longest_words(file)
    return resultado
    '''
    '''
    Opción 2: dict comprehensions...
    lista_de_ficheros = path_directorio.glob('*.txt')
    resultado = {file.name: find_longest_words(file) for file in lista_de_ficheros}
    return resultado
    '''
    '''Opción 3: hacemos dict comprehensions, pero nos ahorramos tb el paso del glob aparte'''
    # resultado = {file.name: find_longest_words(file) for file in path_directorio.glob('*.txt')}
    # return resultado
    return {file.name: find_longest_words(file) for file in path_directorio.glob('*.txt')}





# resultado = find_longest_words('books/46-0.txt')
# pprint.pprint(resultado)

analisis = find_all_longest_words('books')
pprint.pprint(analisis)
