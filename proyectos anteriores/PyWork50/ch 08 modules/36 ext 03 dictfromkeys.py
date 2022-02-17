"""
The dict.fromkeys method (http://mng.bz/1zrV) makes it easy to create a new dict.
For example, dict.fromkeys('abc') will create the dict {'a':None, 'b':None, 'c':None}.

You can also pass a value that will be assigned to each key,
as in dict.fromkeys('abc', 5), resulting in the dict {'a':5, 'b':5, 'c':5}.

Implement a function that does the same thing as dict.keys but whose second argument is a function.
The value associated with the key will be the result of invoking f(key).
"""

# Antes de nada, probemos como funciona fromkeys

d = dict.fromkeys('abcd', 14)
# >>> {'a': 14, 'b': 14, 'c': 14, 'd': 14}
print(d)

d = dict.fromkeys([1, 2, 'ab', 0.27, 'abc'], 'valor')
print(d)
# >>> {1: 'valor', 2: 'valor', 'ab': 'valor', 0.27: 'valor', 'abc': 'valor'}


# Hagamos algo parecido, cogiendo un iterable y creando un diccionario con los items de ese iterable
# el valor que le damos a cada clave sera el que nos salga de aplicar la función dada
def dict_from_keys_function(iterable, function):
    return {key: function(key)
            for key in iterable}


d = dict_from_keys_function('hOla.', str.upper)
print(d)
# >>> {'h': 'H', 'O': 'O', 'l': 'L', 'a': 'A', '.': '.'}

d = dict_from_keys_function('hOla.', str.isupper)
print(d)
# >>> {'h': False, 'O': True, 'l': False, 'a': False, '.': False}

d = dict_from_keys_function('ho1m22ab', str.upper)
print(d)
# >>> {'h': 'H', 'o': 'O', '1': '1', 'm': 'M', '2': '2', 'a': 'A', 'b': 'B'}

# le asignamos el carácter siguiente...
d = dict_from_keys_function('ho1m22ab', lambda char: chr(ord(char) + 1))
print(d)
# >>> {'h': 'i', 'o': 'p', '1': '2', 'm': 'n', '2': '3', 'a': 'b', 'b': 'c'}

d = dict_from_keys_function([71, 102, 115, 118, 123], lambda x: chr(x))
print(d)
# >>> {71: 'G', 102: 'f', 115: 's', 118: 'v', 123: '{'}
