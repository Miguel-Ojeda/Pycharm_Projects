'''
Un diccionario es una estructura que se utiliza para almacenar y acceder, rápidamente,
a un número arbitrario de objetos, que pueden ser cualquier tipo de objetos...
estos objetos los accedemos/identificamos a través de una clave (key)
'''
'''LOS DICCIONARIOS PODEMOS ASEMEJARLOS A UNA GUÍA DE TElËFONOS:
Phone books allow you to QUICKLY retrieve the information (phone number) ASSOCIATED WITH A GIVEN KEY 
(a person’s name). So, INSTEAD OF HAVING TO READ a phone book FRONT TO BACK in order to find someone’s number,
YOU CAN JUMP MORE OR LESS DIRECTLY to a name and look up the associated information. '''

# 1 diccionario estándar dict()
# Ya lo conocemos...
# las claves pueden ser cualquier cosa hashable (o sea, al que se le pueda aplicar la función hash()
# También funcionan con comprehensions...
squares = {x: x * x for x in range(6)}
# >>> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Este diccionario está superoptimizado...
# practicamente el acceso es del orden O(1) para insertar, acceder,  actualizar y borrar.
# Métodos interesantes: key(), items()
print(type(squares))
print(squares)
for key in squares:   # es lo mismo que poner for key in squares.keys()
    print(key)

for key, value in squares.items():
    print(key, '--- el cuadrado es --->', value)

# Cuidado, si la clave no existe en el diccionario, pues se generará un excepción...
# interesantes los métodos get (que no genera error si no existe la clave) y setdefault también...

# A partir de python 3.6 estos diccionarios RECUERDAN EL ORDEN DE INSERCIÓN


# 2 collections.OrderedDict – Remember the Insertion Order of Keys
'''Aunque los estándar ya, >3.6 tb recuerdan el orden, si nuestro código se fundamenta
en que se recuerde el orden de inserción, conviene utilizarlo para asegurarse y dejar
constancia de que tiene que recordarlo!!!'''
import collections
d = collections.OrderedDict(one=1, two=2, three=3)
# >>> d --> OrderedDict([('one', 1), ('two', 2), ('three', 3)])
d['four'] = 4
# >>> d --> OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
# d.keys() odict_keys(['one', 'two', 'three', 'four'])
# Recuerda el orden!!!

# 3 collections.defaultdict – Return Default Values for Missing Keys
# Si en nuestro código cada poco verificamos si un valor existe antes acceder a menudo
# puede interesarnos....
from collections import defaultdict
dd = defaultdict(list)
# esto crea un defaultdict donde, si no existe la clave, automáticamente retorna la lista vacía: []
# si fuera dd = defaultdict(int) el valor defecto sería 0, si fuera str, el valor defecto sería '' , etc
dd['dogs'].append('Rufus') # si no fuera defauldict, esto provocaría una excepción!!!
# O sea, aunque no existe el valor en dogs, no canta error, es como si estuviera [], y luego se actualiza a [Rufus]
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
# Resultado dd --> defaultdict(<class 'list'>, {'dogs': ['Rufus', 'Kathrin', 'Mr Sniffles']})


# collections.ChainMap – Search Multiple Dictionaries as a Single Mapping
# Esto es bestial, es simplemente, que si tenemos varios diccionarios, pues unificarlos...
# unirlos... eso sí... si creamos un ChainMap con dict1, y dict2 y buscamos el valor de una key,
# y hubiera valores en ambos diccioanrios, se devolverá el valor del primer diccionario!!!
from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4, 'one': 5}
chain = ChainMap(dict1, dict2)
# chain --> ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4, 'one': 5})
# chain['three'] --> 3
# chain['one'] --> 1
print(chain['three'])
print(chain['one'])  # --> da 1 pq, aunque está en ambos diccioanarios... nos devuelve el primer valor encontrado
# print(chain['six'])  # da error pq no existe la clave en ningún diccionario de los que forman el ChainMap
chain['six'] = 83   # Lo añade al primer diccionario!!!!
print(chain)  # ChainMap({'one': 1, 'two': 2, 'six': 83}, {'three': 3, 'four': 4, 'one': 5})

