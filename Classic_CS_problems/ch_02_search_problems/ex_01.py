"""
Show the performance advantage of binary search over linear search by creating
a list of one million numbers and timing how long it takes the linear_contains()
and binary_contains() functions defined in this chapter to find various numbers in the list.
"""
CANTIDAD_ITEMS = 1_000_000
REPETICIONES_BUSQUEDA = 1_000

import random
from generic_search import linear_contains, binary_contains

lista_items = [random.randint(0, 10_000_000) for i in range(CANTIDAD_ITEMS)]
lista_items_ordenada = sorted(lista_items)

print(f'{len(lista_items):_}')
print(f'{len(lista_items_ordenada):_}')
print(lista_items[:24])
print(lista_items_ordenada[:24])


def test_lineal():
    for i in range(REPETICIONES_BUSQUEDA):
        linear_contains(lista_items, 15)

def test_binario():
    for i in range(REPETICIONES_BUSQUEDA):
        binary_contains(lista_items_ordenada, 15)


import cProfile
cProfile.run('test_lineal()')
'''  TARDA CASI 55 segundos!!!
         1004 function calls in 54.740 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   54.740   54.740 <string>:1(<module>)
        1    0.006    0.006   54.740   54.740 ex_01.py:21(test_lineal)
     1000   54.735    0.055   54.735    0.055 generic_search.py:33(linear_contains)
        1    0.000    0.000   54.740   54.740 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
cProfile.run('test_binario()')
''' TARDA 8 milésimas de segundo!!!
         2004 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.000    0.000    0.008    0.008 ex_01.py:25(test_binario)
     1000    0.007    0.000    0.007    0.000 generic_search.py:40(binary_contains)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''



