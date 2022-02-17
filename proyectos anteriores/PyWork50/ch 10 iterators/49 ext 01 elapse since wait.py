"""
The existing function elapsed_since reported how much time passed between iterations.

Now write a generator function that takes two arguments—a piece
of data and a minimum amount of time that must elapse between iterations.

If the next element is requested via the iterator protocol (i.e., next), and the time
elapsed since the previous iteration is greater than the user-defined minimum,
then the value is returned. If not, then the generator uses time.sleep to wait
until the appropriate amount of time has elapsed
"""
import time


def elapsed_since_wait(iterable, min_time):
    tiempo_anterior = None
    for item in iterable:
        if tiempo_anterior:
            diferencia = time.perf_counter() - tiempo_anterior
            if diferencia < min_time:
                time.sleep(min_time - diferencia)
            diferencia = time.perf_counter() - tiempo_anterior
        else:
            diferencia = 0
        tiempo_anterior = time.perf_counter()
        yield (diferencia, item)


secuencia = 'abcde'
secuencia_2 = [1, [1, 2, ], 'ab', 'cdE']

for i in elapsed_since_wait(secuencia_2, 1):
    print(i)