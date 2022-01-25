'''
Write a function, dictdiff, that takes two dicts as arguments. The function returns
a new dict that expresses the difference between the two dicts.
If there are no differences between the dicts, dictdiff returns an empty dict.
For each key-value pair that differs, the return value of dictdiff will have a key-value pair
in which the value is a list containing the values from the two different dicts.
If one of the dicts doesn’t contain that key, it should contain None.
The following provides some examples:
d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1)) --> {}
print(dictdiff(d1, d2))  -->  {'c': [3, 4]}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4))  --> {'c': [None, 4], 'd': [3, None]}
d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5))   ---> {'c': [3, None], 'd': [None, 4]}
'''


def dictdiff(dict_1: dict, dict_2: dict) -> dict:
    diferencias = dict()

    # Primero recorremos el primer diccionario para ver las diferencias respecto al segundo...
    for key, value_1 in dict_1.items():
        value_2 = dict_2.get(key, None)
        if value_1 == value_2:
            continue
        # Else...
        diferencias[key] = [value_1, value_2]
    # Ahora mismo con el segundo diccionario...
    for key, value_2 in dict_2.items():
        if key in dict_1:
            # Ya lo analizamos antes!!!
            continue
        # Else... como no están dict_1 y sí en dict_2
        diferencias[key] = [None, value_2]

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