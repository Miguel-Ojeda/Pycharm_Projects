# Versión dos después de leer la solución de Reuven!!
# Ufff....

'''
dict.keys() returns a special object of type dict_keys.
dict_keys es un iterator que además soporta muchas de los métodos disponibles en los sets
como la unión | y la intersección &
Así, si hacemos all_keys = first.keys() | second.keys() obtendremos
un set con las keys de ambos diccionarios...
Así nos ahorramos tiempo, porque no tenemos que ir dos veces con las claves repetidas!!!
'''


def dictdiff(dict_1, dict_2) -> dict:
    diferencias = {}
    all_keys = all_keys = dict_1.keys() | dict_2.keys()
    for key in all_keys:
        val_1 = dict_1.get(key, None)
        val_2 = dict_2.get(key, None)
        if val_1 != val_2:
            diferencias[key] = [val_1, val_2]

    return diferencias


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}

diferencias = dictdiff(d1, d5)
print(diferencias)

'''
print(dictdiff(d1, d1)) --> {}
print(dictdiff(d1, d2))  -->  {'c': [3, 4]}
print(dictdiff(d3, d4))  --> {'c': [None, 4], 'd': [3, None]}
print(dictdiff(d1, d5))   ---> {'c': [3, None], 'd': [None, 4]}
'''