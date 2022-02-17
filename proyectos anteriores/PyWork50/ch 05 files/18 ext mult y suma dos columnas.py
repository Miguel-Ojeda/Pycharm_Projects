'''
Create a text file (using an editor, not necessarily Python) containing two tab-separated columns,
with each column containing a number. Then use Python to read through the file you’ve created.
For each line, multiply each first number by the second, and then sum the results from all the lines.
Ignore any line that doesn’t contain two numeric columns
'''

# import string
from io import StringIO   # Para pruebas!!!

fake_file = StringIO(
'''
10\t20
30\t2
2\t4
12\t1
''')

def multiplica_y_suma(filename):
    suma = 0
    # for linea in open(filename):
    for linea in fake_file:
        lista = linea.split('\t')
        if len(lista) != 2:
            continue
        num_1 = lista[0].strip()
        num_2 = lista[1].strip()
        if not num_1.isdecimal() or not num_2.isdecimal():
            continue
        else:
            suma += int(num_1) * int(num_2)

    return suma

print(multiplica_y_suma('cualquier-cosa'))