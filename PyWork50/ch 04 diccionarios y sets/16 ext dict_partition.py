'''
Write a function , dict_partition, that takes one dict (d) and a function (f) as arguments.
dict_partition will return two dicts, each containing key-value pairs from d.

The decision regarding where to put each of the key-value pairs
will be made according to the output from f, which will be run on each key value pair in d.

** If f returns True, then the key-value pair will be put in the first output dict.
** If f returns False, then the key-value pair will be put in the second output dict.
'''


def dict_partition(diccionario, funcion):
    dict_True = dict_False = {}

    for key, value in diccionario.items():
        if funcion(key, value):
            dict_True[key] = value
        else:
            dict_False[key] = value

    return dict_True, dict_False


