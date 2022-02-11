"""
Expand the transform_values exercise, taking two function arguments, rather than just one.
The first function argument will work as before, being applied to the value and producing output.
The second function argument takes two arguments, a key and a value, and determines whether
there will be any output at all.
That is, the second function will return True or False and will allow us to selectively
create a key-value pair in the output dict.

O sea, la primera función es similar a map, y la segunda hace las funciones de filter...
"""

def transform_value_and_filter(funcion, filtro, diccionario):
    return {key: funcion(value)
            for key, value in diccionario.items()
            if filtro(key, value)}

