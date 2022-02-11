"""
In this exercise, we’re going to create a slight variation on map, one that applies
a function to each of the values of a dict.

The result of invoking this function, transform_values, is a new dict
whose keys are the same as the input dict, but whose values have been transformed by the function.

(The name of the function comes from Ruby on Rails, which provides a function of the same name.)

The function passed to transform_values should take a single argument, the dict’s value.

When your transform_values function works, you should be able to invoke it as follows:
d = {'a':1, 'b':2, 'c':3}
transform_values(lambda x: x*x, d)
The result of this call will be the following dict:
{'a': 1, 'b': 4, 'c': 9}
"""

def transform_values(funcion, diccionario):
    return {key: funcion(value)
            for key, value in diccionario.items()}


d = {'a': 1, 'b': 2, 'c': 3}

resultado = transform_values(lambda x: x ** 2, d)
print(resultado)