"""
Write a function, apply_to_each, that takes two arguments:
a function that takes a single argument, and an iterable.

Return a list whose values are the result of applying the function to each element in the iterable.

(If this sounds familiar, it might be—this is an implementation of the classic map function,
still available in Python. You can find a description of map in chapter 7.)
"""


def apply_to_each(func, iterable):
    return [func(item) for item in iterable]


resultado = apply_to_each(str.capitalize, 'abcfgh')
print(resultado)
# >>> ['A', 'B', 'C', 'F', 'G', 'H']

resultado = apply_to_each(str.capitalize, {'árbol', 'mesa', 'hipopótamo'})
print(resultado)
# >>> ['Hipopótamo', 'Árbol', 'Mesa']

resultado = apply_to_each(len, ['ho', 'holala', 'supercalifragist', [1, 2, 3], range(10)])
print(resultado)
# >>> [2, 6, 16, 3, 10]


