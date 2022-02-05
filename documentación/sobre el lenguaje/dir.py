# La función dir nos lista todos los métodos a los que podemos llamar sobre un objeto

l = list()

print(dir(l))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# etc !!!!!

import collections

c = collections.Counter()
metodos_counter = dir(c)
# ['__add__', '__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__iadd__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__le__', '__len__',
# '__lt__', '__missing__', '__module__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__sub__', '__subclasshook__', '__weakref__', '_keep_positive', 'clear', 'copy', 'elements', 'fromkeys', 'get',
# 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'total', 'update', 'values']

# Veamos los métodos que no son magic...
for metodo in metodos_counter:
    if metodo.startswith('__') and metodo.endswith('__'):
        continue
    else:
        print(metodo)


def_dic = collections.defaultdict()
metodos_default_dic = dir(def_dic)
# Veamos los métodos que no empiezan por _
print('\n\n\nAlgunos métodos de defaultdic:\n\n')
for metodo in metodos_default_dic:
    if metodo.startswith('_'):
        continue
    else:
        print(metodo)

