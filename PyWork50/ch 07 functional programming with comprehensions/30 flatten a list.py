"""
In this exercise, we’ll practice doing such unraveling.
Write a function that takes a list of lists (just one element deep) and returns
a flat, one-dimensional version of the list.
Thus, invoking flatten([[1,2], [3,4]]) will return [1,2,3,4]

Note that there are several possible solutions to this problem;
I’m asking you to solve it with list comprehensions.
Also note that we only need to worry about flattening a two-level list.

O sea, el objetivo el aplanar la lista de listas, con list comprehensions
Supondremos que cada ítem de la lista principal es otra lista... (ya plana!!)
O sea, los ítems son listas planas como en el ejemplo dado al principio
"""

def flatten_list(lista):
    return [item
            for sublista in lista
            for item in sublista
            ]


lista = [[], [1,2], [3,4], [5, 6, 7, 8], [9], [10]]
lista_plana = flatten_list(lista)
print(lista_plana)