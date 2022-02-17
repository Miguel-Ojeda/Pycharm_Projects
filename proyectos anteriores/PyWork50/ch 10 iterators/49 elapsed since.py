"""
In this exercise, write a generator function whose argument must be iterable.

With each iteration, the generator will return a two-element tuple.
* The first element in the tuple will be an integer indicating how many seconds have passed since the previous
iteration.
* The tuple’s second element will be the next item from the passed argument.

Note that the timing should be relative to the previous iteration, not when
the generator was first created or invoked. Thus the timing number in the first iteration will be 0.

You can use time.perf_counter, which returns the number of seconds since the program was started.
You could use time.time, but perf_counter is considered more reliable for such purposes.

También podemos usar perf_counter_ns que devuelve el tiempo en nanosegundos....
"""

import time
import random



def elapsed_since(iterable):
    tiempo_anterior = None
    for item in iterable:
        if tiempo_anterior:
            diferencia = time.perf_counter() - tiempo_anterior
        else:
            diferencia = 0
        tiempo_anterior = time.perf_counter()
        yield (diferencia, item)


secuencia = 'abcde'
secuencia_2 = [1, [1, 2, ], 'ab', 'cdE']

for i in elapsed_since(secuencia_2):
    print(i)

