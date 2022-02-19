"""
Se puede hacer que Python implemente, por nosotros, el proceso de memoization
Podemos utilizar un decorator que trae Python para ello...
Veámoslo...
decorator @functools.lru_cache() este decorator hace que, cada vez que se implemente
la función a la que decora, el valor sea cacheado!!! de forma automática, sin hacer nada!!!
"""

from functools import lru_cache
import cProfile

# Esta es la implementación cutre.... la recursiva que utilizamos al principio
# Pero incluye el decorador!!
@lru_cache(maxsize=None)
def fib_3(n: int) -> int:
    if n < 2:
        return n
    return fib_3(n - 1) + fib_3(n - 2)

cProfile.run('fib_3(50)')
'''
51/1    0.000    0.000    0.000    0.000 03 fibonacci con memoization por decorators.py:14(fib_3)
Sí, se realiza el cacheo como hicimos en 02 fibonacci momoization!!
Sin nosotros hacer nada!!!'''