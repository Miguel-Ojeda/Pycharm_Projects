"""
Show the lines of a text file that contain at least one vowel and contain more
than 20 characters
Haremos esto pero con un return... retornaremos una lista
con las líneas que tengan al menos 20 caracteres, siempre y cuando alguno de ellos sea una vocal!!
"""
import pprint
from io import StringIO

fake_file = StringIO('''Esta es una línea
123456pqrst t wwr s tv
1254 34a5 23 1234567
12aaaaaaa bcaa
paqxxx 12543234 343143''')


def lines_with_1v_20chars(text_file):
    with open(text_file, encoding='utf-8') as texto:
        return[linea
               for linea in texto
               if len(linea) >= 20 and
               any(vocal in linea.lower() for vocal in 'aeiou')]


# El método de Reuven para comprobar hay una vocal es mucho más sencillo que el mío
# el mío comprueba para cada vocal si está... el método de él es con sets...
# mucho más claro
def lines_with_1v_20chars_v2(text_file):
    with open(text_file, encoding='utf-8') as texto:
        return[linea
               for linea in texto
               if len(linea) >= 20 and
               len(set('aeiou') & set(linea.lower())) >= 1]
    # La última condición quiere decir que la intersección entre las vocales
    # y el texto es no vacía!!!




file = 'files/43-0.txt'


# resultado = lines_with_1v_20chars(file)
# print(resultado)

resultado = lines_with_1v_20chars_v2(file)
pprint.pprint(resultado)