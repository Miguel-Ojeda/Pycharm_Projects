"""
Given a text file, what are the lengths of the different words?
Return a set of different word lengths in the file.
"""
import pprint

from io import StringIO
fake_file = StringIO(
'''Primera línea
Esto es otra línea
1 2 de animal murciélago''')

def get_len_words(text_file):
    with open(text_file, encoding='utf-8') as tf:
        return {len(word)
                for linea in tf
                for word in linea.split()}


file = 'files/43-0.txt'
resultado = get_len_words(file)
pprint.pprint(resultado)





