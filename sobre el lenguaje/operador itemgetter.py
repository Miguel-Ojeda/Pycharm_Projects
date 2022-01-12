# https://docs.python.org/3/library/operator.html?#operator.itemgetter
# MUY INTERESANTE EL OPERADOR ITEMGETTER
# Retorna un objeto callable que podemos utilizar para obtener algún item de una secuencia, diccionario, ...
# 2 formatos:
# operator.itemgetter(item)

# Ejemplo 1:
import operator

f = operator.itemgetter(2)
# Ahora lo que pasa es que f(iterable) es como iterable[2]

print(f('ABCDEF'))  # --> C
print(f([1, 2, 'y', 4])) # --> y

# operator.itemgetter(*items)
# También se puede usar para obtener una tupla de ítems...
f = operator.itemgetter(1, 3, 5)
print(f('ABCDEFGHIJ')) # --> ('B', 'D', 'F')
print(f([1, 2, 5, 6, 7, 8, 9, 23])) # --> (2, 6, 8)

f = operator.itemgetter(slice(2, None))
# Aquí tenemos un callable que nos devuelve la tupla con los elementos desde el tercero(índice 2) hasta el final
print(f('ABCDEFGHIJ'))

# También lo podemos invocar directamente...
# itemgetter(1)('ABCDEFG') --> 'B'
# itemgetter(1, 3, 5)('ABCDEFG') --> ('B', 'D', 'F')
# Lists, tuples, and strings accept an index or a SLICE:
# itemgetter(slice(2, None))('ABCDEFG') --> 'CDEFG'

# También se puede usar en diccionarios con valores hashables...
soldier = {'rank': 'captain', 'name': 'dotterbart'}
# equivalente a soldier = dict(rank='captain', name='dotterbart')
f = operator.itemgetter('rank')
print(f(soldier))

# Otro ejemplo más complejo...
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = operator.itemgetter(1)  # esto lo usaremos en cada tupla del inventario
# para ordenar el inventario por el número podríamos hacer
inventario_ordenado = sorted(inventory, key=getcount)
print(inventario_ordenado)

# obtener la lista de cuántos elementos tenemos de cada tipo en el inventario...
n_items = list(map(getcount, inventory))  # convertimos a lista el map object para poder imprimirlo!!
print(n_items)

