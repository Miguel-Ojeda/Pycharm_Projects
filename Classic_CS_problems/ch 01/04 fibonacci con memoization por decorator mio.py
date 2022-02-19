"""
Haremos lo mismo ahora, decoraremos la función recursiva del principio para
conseguir la memoization, pero intentando crear nuestro propio decorador
no utilizar el que ya existe en Python.
Esto no es lógico, deberíamos aprovechar el que ya está implmentado,
sólo es para practicar
"""

import cProfile

memo = {}

def memoization(func):
    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]
    return wrapper


@memoization
def fib_4(n: int) -> int:
    if n < 2:
        return n
    return fib_4(n - 1) + fib_4(n - 2)


'''Recordemos que sin el decorador los resultados eran...
21891/1    0.009    0.000    0.009    0.009 04 fibonacci con memoization por decorator mio.py:23(fib_4)
'''
cProfile.run('fib_4(20)')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     39/1    0.000    0.000    0.000    0.000 04 fibonacci con memoization por decorator mio.py:14(wrapper)
     21/1    0.000    0.000    0.000    0.000 04 fibonacci con memoization por decorator mio.py:21(fib_4)
'''