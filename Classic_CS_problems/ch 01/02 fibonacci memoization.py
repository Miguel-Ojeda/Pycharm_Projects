"""
Memoization es una técnica muy potente, no la conocía...
Consiste, básicamente, en que cuando calculamos un valor de la función,
pues ya puestos, de paso, lo memorizamos!!! para que cuando luego
lo volvamos a pedir, no haga falta calcularlo!!!
"""
import cProfile

# En fibonacci iremos guardando las imágenes de la función fibonacci cuando
# vayamos calculando nuevas imágenes!!
fibonacci: dict[int, int] = {0: 0, 1: 1}

def fib_2(n: int) -> int:
    if n not in fibonacci:
        fibonacci[n] = fib_2(n-1) + fib_2(n-2)
    return fibonacci[n]

resultado = fib_2(8)
print(resultado)
# >>> 21

# veamos la diferencia con la implementación recursiva...
# Antes, para calcular fib_2(20) se realizaban 21891... ¿Ahora?
cProfile.run('fib_2(20)')
'''
25/1    0.000    0.000    0.000    0.000 02 fibonacci memoization.py:13(fib_2)
'''
cProfile.run('fib_2(50)')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     61/1    0.000    0.000    0.000    0.000 02 fibonacci memoization.py:13(fib_2)
'''
# 61 llamadas sólo (antes no se podía hacer pq


