'''
The challenge for this exercise is to write a wordcount function that mimics the wc
Unix command. The function will take a filename as input and will print four lines
of output:
1 Number of characters (including whitespace)
2 Number of words (separated by whitespace)
3 Number of lines
4 Number of unique words (case sensitive, so “NO” is different from “no”)
'''


from collections import defaultdict
from io import StringIO

fake_file = StringIO('''This is a test file.

It contains 28 words and 20 different words.

It also contains 165 characters.

It also contains 11 lines.

It is also self-referential.

Wow!''')

def word_count(filename):
    total_chars = total_lines = total_palabras = 0
    palabras_distintas = set()
    with open(filename, encoding='UTF-8') as file:
        for linea in file:
            total_lines += 1
            total_chars += len(linea)   # incluimos whitespaces
            for palabra in linea.split():
                palabras_distintas.add(palabra)
                total_palabras += 1

    total_palabras_distintas = len(palabras_distintas)
    print(f'Número de caracteres: {total_chars:,}')
    print(f'Número de palabras: {total_palabras:,}')
    print(f'Número de líneas: {total_lines:,}')
    print(f'Número de palabras distintas: {total_palabras_distintas:,}')


def word_count_v2(filename):
    '''Reuven guarda los datos en un diccioanrio para que estén mejor organizados...'''

    counts = {'characters': 0, 'words': 0, 'lines': 0, 'palabras distintas': 0}
    palabras_distintas = set()

    with open(filename, encoding='UTF-8') as file:
        for linea in file:
            counts['lines'] += 1
            counts['characters'] += len(linea)   # incluimos whitespaces

            # Hace mucho más rápido lo de contar las palabras y añadir los elementos!!!
            # Nosotros íbamos palabra por palabra para añadir al set... pero se puede utilziar el método
            # update que nos mete una lista de elementos en el set...
            palabras = linea.split()
            counts['words'] += len(palabras)
            palabras_distintas.update(palabras)

    counts['palabras distintas'] = len(palabras_distintas)

    for key in counts:
        print(f'{key}: {counts[key]:,}')

word_count('files/43-0.txt')
word_count_v2('files/43-0.txt')

