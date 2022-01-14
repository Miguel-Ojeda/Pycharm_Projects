# A Counter is a dict subclass for counting hashable objects.
# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative counts.

# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

# Creamos un counter (es una especie de diccionarios don de para cada clave cuenta el número de veces que aparece...
c = Counter('gallahad')
print(c)
# Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})

c = Counter({'red': 4, 'blue': 2})
print(c)
# Counter({'red': 4, 'blue': 2})

c = Counter(['eggs', 'ham', 'eggs', 'bacon', 'sausages', 'bacon', 'eggs'])
print(c)
# Counter({'eggs': 3, 'bacon': 2, 'ham': 1, 'sausages': 1})
# c['eggs']  --> 3

# Tiene bastantes métodos para usar: total(), elements(), most_common
# Muy interesante el método most_common([n])
# Counter('abracadabra').most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]
# Devuelve una lista de tuplas, con los n valores que más se repiten...
# Cada elemento de la tupla es ( valor, número_de_veces_que se repite)

# ver python workout, ejercicio 12 !!!  --->


# Write a function, most_repeating_word, that takes a sequence of strings as input. The
# function should return the string that contains the greatest number of repeated letters. In other words
#  For each word, find the letter that appears the most times.
#  Find the word whose most-repeated letter appears more than any other.
# That is, if words is set to words = ['this', 'is', 'an', 'elementary', 'test', 'example']
# then your function should return elementary

# from collections import Counter
# https://docs.python.org/3/library/collections.html#collections.Counter



words = ['this', 'is', 'an', 'elementary', 'test', 'example']
words2 = ['this', 'is', 'annnnnnnn', 'elementary', 'test', 'example']

# Segunda versión!!! Mucho más sencillo
def cuenta_maximas_letras_repeticiones(word: str):
    return Counter(word).most_common(1)[0][1]

print('Segunda versión... utilizando la función máx con una key que funciona por palabras y es más sencilla')
print('La palabra con más repetidas de la lista es: ', max(words, key=cuenta_maximas_letras_repeticiones))
print('La palabra con más repetidas de la lista 2 es: ', max(words2, key=cuenta_maximas_letras_repeticiones))














