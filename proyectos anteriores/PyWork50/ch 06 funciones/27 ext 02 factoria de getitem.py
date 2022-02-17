"""
Write a function, create_getitem, that takes a single argument and returns a function f.

The returned f can then be invoked on any data structure whose elements can be selected
via square brackets, and then returns that item.

So if I invoke f = getitem('a'), and if I have a dict d = {'a':1, 'b':2}, then f(d) will return 1.

(This is very similar to operator.itemgetter, a very useful function in many circumstances.)
"""

def create_getitem(item):

    def get_item(structure):
        return structure[item]

    return get_item


f_1 = create_getitem(1)
f_2 = create_getitem(2)
f_a = create_getitem('a')
f_profesion = create_getitem('profesion')

lista = [2, 3, 6, 8]
print(f_1(lista))
print(f_2(lista))

tupla = ('abc', 'def', 'ghi', 'jkl')
print(f_1(tupla))
print(f_2(tupla))

lista = [{2, 3, 6}, [3, 4], 6, 8]
print(f_1(lista))
print(f_2(lista))
print(f_1(f_1(lista)))

tupla = ('abc', {'def', 0}, 'ghi', 'jkl')
print(f_1(tupla))
print(f_2(tupla))

diccionario = { 1: 14, 'a': 'madrid', 'profesion': 'dfs'}
print(f_a(diccionario))
print(f_profesion(diccionario))



