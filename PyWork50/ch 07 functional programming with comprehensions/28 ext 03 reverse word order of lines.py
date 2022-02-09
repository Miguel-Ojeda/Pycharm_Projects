"""
Use a list comprehension to reverse the word order of lines in a text file.
That is, if the first line is abc def and the second line is ghi jkl,
then you should return the list ['def abc', 'jkl ghi'].
"""
import pprint
from io import StringIO

fake_file = StringIO('''uno dos tres
cuatro cinco seis
caballo perro tren luisito.''')


def reverse_word_order(file):
    with open(file, encoding='utf-8') as file:
        return [' '.join(reversed(linea.split()))
                for linea in file]


'''
lógicamente, no es posible crear lo mismo con generator expressions
si queremos generar un objeto real, como en este caso...'''

file = 'files/43-0.txt'
resultado = reverse_word_order(file)
pprint.pprint(resultado)

'''si quisiéramos devolver un generator pero luego ir iterando pues imagino que sí

def reverse_word_order_gen(file):
    with open(file, encoding='utf-8') as file:
        return (' '.join(reversed(linea.split()))
                for linea in file)
                
generador = reverse_word_order_gen(file)
for linea in generador:
    print(linea)
NO SIRVE, PORQUE EL GENERADOR DEBE TENER ABIERTO EL FICHERO, Y RESULTA QUE DICE QUE ESTÁ CERRADO!!
>>> ValueError: I/O operation on closed file.
'''
