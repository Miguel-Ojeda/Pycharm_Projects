"""
For this exercise, first create a dict of any size, in which the keys are unique and the
values are also unique. (A key may appear as a value, or vice versa.)
"""

dict_0 = {'a': 1, 'b': 2, 'c': 3}
dict_1 = {'Miguel': 1456, 'Carlos': 2985, 'Carpanta': 30921, 'Marco': 1111, 'Iris': 2350}


def flip_dict(diccionario):
    return {value: key
            for key, value in diccionario.items()}


def flip_dict_v2(diccionario):
    return {diccionario[key]: key
            for key in diccionario}



resultado = flip_dict(dict_0)
print(resultado)
resultado = flip_dict(dict_1)
print(resultado)