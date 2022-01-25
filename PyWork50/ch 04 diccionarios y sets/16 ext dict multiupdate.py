'''
The dict.update method merges two dicts.

Write a function that takes any number of dicts and returns a dict that reflects
the combination of all of them.
If the same key appears in more than one dict, then the most recently merged
dict’s value should appear in the output.
'''

# La función update actualiza un diccionario con los valores de otro diccioanrio
# o con los key, values de un iterable proporcionado...
# Básicamente, le damos un objeto con key, values y actualiza nuestro diccionario con los nuevos keys, values


def multi_update(*diccionarios):
    resultado = {}
    for diccioanario in diccionarios:
        resultado.update(diccioanario)
    return resultado
