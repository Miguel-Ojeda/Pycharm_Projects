"""
Create a dict whose keys are currency names and
whose values are the price of that currency in U.S. dollars.

Write a function that asks the user what currency they use,
then returns the dict from the previous exercise as before, but with its
prices converted into the requested currency
"""
import pprint

CURRENCY_DOLARES = {'us dollar': 1, 'euro': 0.88, 'libra esterlina': 0.74,
                       'dolar canadiense': 1.2736, 'real brasil': 5.2532, 'fijan dollar': 2.13,
                       'bolivian': 6.91, 'dinar líbano': 4.60}

# Esto es del ejercicio anterior... precios en dólares
libros = [('Santiago Posteguillo', 'Africanus', 22),
          ('JK Rowling', 'El prisionero de Azkabán', 14),
          ('George Orwell', '1984', 9),
          ('Miguel de_Cervantes', 'El Quijote', 27),
          ('Ken Follett', 'Los Pilares de la Tierra', 17),
          ('Isaac Asimov', 'La fundación', 32),
          ]

'''
El objetivo es conseguir lo mismo que antes, pero pasando los precios de, en vez de dólares, como están
a lo que nos digan...
Se supone que los precios son en dólares
{'1984': {'Autor (apellido)': 'Orwell',
          'Autor (nombre)': 'George',
          'Precio': 9},
 'Africanus': {'Autor (apellido)': 'Posteguillo',
               'Autor (nombre)': 'Santiago',
               'Precio': 22},
 'El Quijote': {'Autor (apellido)': 'de_Cervantes',
                'Autor (nombre)': 'Miguel',
                'Precio': 27},
 'El prisionero de Azkabán': {'Autor (apellido)': 'Rowling',
                              'Autor (nombre)': 'JK',
                              'Precio': 14},
 'La fundación': {'Autor (apellido)': 'Asimov',
                  'Autor (nombre)': 'Isaac',
                  'Precio': 32},
 'Los Pilares de la Tierra': {'Autor (apellido)': 'Follett',
                              'Autor (nombre)': 'Ken',
                              'Precio': 17}}
'''


# Ahora hagamos la función que muestre lo anterior, pero en vez de en dólares, en la moneda que elijamos
# Partimos de los datos iniciales, la lista de tuplas ....
def get_prices_in(books, moneda_elegida):
    if moneda_elegida in CURRENCY_DOLARES:
        return {titulo: {'Autor nombre': nombre.split()[0],
                         'Autor apellido': nombre.split()[1],
                         'Precio': precio * CURRENCY_DOLARES[moneda_elegida]}
                for nombre, titulo, precio in books
                if moneda_elegida in CURRENCY_DOLARES
                }


resultado = get_prices_in(libros, 'euro')
pprint.pprint(resultado)
'''
Este es el resultado cuando utilizamos euros....
{'1984': {'Autor apellido': 'Orwell', 'Autor nombre': 'George', 'Precio': 7.92},
 'Africanus': {'Autor apellido': 'Posteguillo',
               'Autor nombre': 'Santiago',
               'Precio': 19.36},
 'El Quijote': {'Autor apellido': 'de_Cervantes',
                'Autor nombre': 'Miguel',
                'Precio': 23.76},
 'El prisionero de Azkabán': {'Autor apellido': 'Rowling',
                              'Autor nombre': 'JK',
                              'Precio': 12.32},
 'La fundación': {'Autor apellido': 'Asimov',
                  'Autor nombre': 'Isaac',
                  'Precio': 28.16},
 'Los Pilares de la Tierra': {'Autor apellido': 'Follett',
                              'Autor nombre': 'Ken',
                              'Precio': 14.96}}
'''
