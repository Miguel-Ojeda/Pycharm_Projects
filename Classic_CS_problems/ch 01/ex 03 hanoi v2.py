"""
V2
"""
import cProfile
import pprint

Solucion = list[tuple[str, str]]
# definimos un Alias para el  tipo de la solucion de Hanoi
# Por ejemplo, la solución para hanoi de 3 discos es:
# [('I', 'F'), ('I', 'A'), ('F', 'A'), ('I', 'F'), ('A', 'I'), ('A', 'F'), ('I', 'F')]


def transformar(solucion_anterior: Solucion,
                inicial: str, final: str, auxiliar: str) -> Solucion:
    transformacion = {'I': inicial, 'A': auxiliar, 'F': final}
    solucion_transformada = []
    for a, b in solucion_anterior:
        trans_a, trans_b = transformacion[a], transformacion[b]
        # solucion_transformada.append(tuple(trans_a, trans_b))
        solucion_transformada.append((transformacion[a], transformacion[b]))
    return solucion_transformada


def hanoi(n: int) -> Solucion:
    """Parecido a la versión 1,
    pero vamos a ir generando, y memorizando, todas las soluciones anteriores a la buscada....
    'soluciones[n]' contendrá la lista de tuplas con la solución de hanoi(n) para pasar
    de la inicial a la final...
    """
    # Solucion para el caso n = 1
    solucion_actual = [('I', 'F')]

    for index in range(2, n + 1):
        solucion_anterior = solucion_actual
        # Primero llevamos n-1 discos de la primera columna, (inicial) a la segunda (auxiliar=
        # Para ello simplemente deemos utilizar la solución que tenemos calculada anterior
        # pero cambiando la columna final por la auxiliar y viceversa
        # print(index)
        transformacion_anterior = transformar(solucion_anterior, inicial='I', final='A', auxiliar='F')
        # print(transformacion_anterior)
        solucion_actual = transformacion_anterior
        # print(solucion_actual)
        # Ahora pasamos un disco, el de abajo del todo_, de la pila inicial, a la final
        solucion_actual.append(('I', 'F'))
        # print(solucion_actual)
        # ahora volvemos a pasar los n-1 discos (la solución anterior) pero de la columna 2 a la 3
        # para ello simplemente utilziamos la solución anterior, pero cambiamos I por A, y A por I
        transformacion_anterior = transformar(solucion_anterior, inicial='A', final='F', auxiliar='I')
        # print(transformacion_anterior)
        solucion_actual.extend(transformacion_anterior)
        # print(solucion_actual)

    return solucion_actual




resultado = hanoi(5)
pprint.pprint(resultado)
'''
[('I', 'F'), ('I', 'A'), ('F', 'A'), ('I', 'F'), ('A', 'I'), ('A', 'F'), ('I', 'F'),
('I', 'A'), ('F', 'A'), ('F', 'I'), ('A', 'I'), ('F', 'A'), ('I', 'F'), ('I', 'A'),
('F', 'A'), ('I', 'F'), ('A', 'I'), ('A', 'F'), ('I', 'F'), ('A', 'I'), ('F', 'A'),
('F', 'I'), ('A', 'I'), ('A', 'F'), ('I', 'F'), ('I', 'A'), ('F', 'A'), ('I', 'F'),
('A', 'I'), ('A', 'F'), ('I', 'F')]
'''
resultado = hanoi(6)
print('\n\n')
pprint.pprint(resultado)
'''
[('I', 'A'), ('I', 'F'), ('A', 'F'), ('I', 'A'), ('F', 'I'), ('F', 'A'), ('I', 'A'),
('I', 'F'), ('A', 'F'), ('A', 'I'), ('F', 'I'), ('A', 'F'), ('I', 'A'), ('I', 'F'),
('A', 'F'), ('I', 'A'), ('F', 'I'), ('F', 'A'), ('I', 'A'), ('F', 'I'), ('A', 'F'),
('A', 'I'), ('F', 'I'), ('F', 'A'), ('I', 'A'), ('I', 'F'), ('A', 'F'), ('I', 'A'),
('F', 'I'), ('F', 'A'), ('I', 'A'), ('I', 'F'), ('A', 'F'), ('A', 'I'), ('F', 'I'),
('A', 'F'), ('I', 'A'), ('I', 'F'), ('A', 'F'), ('A', 'I'), ('F', 'I'), ('F', 'A'),
('I', 'A'), ('F', 'I'), ('A', 'F'), ('A', 'I'), ('F', 'I'), ('A', 'F'), ('I', 'A'),
('I', 'F'), ('A', 'F'), ('I', 'A'), ('F', 'I'), ('F', 'A'), ('I', 'A'), ('I', 'F'),
('A', 'F'), ('A', 'I'), ('F', 'I'), ('A', 'F'), ('I', 'A'), ('I', 'F'), ('A', 'F')]
'''
# cProfile.run("hanoi_symbol('I', 'F', 'A', 20)")
'''
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.026    0.026    1.403    1.403 <string>:1(<module>)
1572862/1    1.185    0.000    1.377    1.377 ex 03 v1.py:40(hanoi_symbol)
        1    0.000    0.000    1.403    1.403 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1048574    0.191    0.000    0.191    0.000 {method 'extend' of 'list' objects}
'''

# Veamos ahora como funcional el profile....
cProfile.run("hanoi(20)")
'''
  2097190 function calls in 1.394 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.032    0.032    1.394    1.394 <string>:1(<module>)
       38    1.105    0.029    1.337    0.035 ex 03 v2.py:13(transformar)
        1    0.013    0.013    1.362    1.362 ex 03 v2.py:24(hanoi)
        1    0.000    0.000    1.394    1.394 {built-in method builtins.exec}
  2_097_129    0.232    0.000    0.232    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# ahora comparativa con 24 discos
# Antes (versión 01) 23 segundos,
'''         41_943_039 function calls (16777218 primitive calls) in 22.823 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.399    0.399   22.823   22.823 <string>:1(<module>)
25165822/1   19.186    0.000   22.423   22.423 ex 03 v1.py:40(hanoi_symbol)
        1    0.000    0.000   22.823   22.823 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 16777214    3.237    0.000    3.237    0.000 {method 'extend' of 'list' objects}
Process finished with exit code 0
'''

# Versión con memoria, ahora 24 discos
cProfile.run("hanoi(24)")
# Tarda más o menos lo mismo, pero no es recursiva...
'''
        33554478 function calls in 22.601 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.571    0.571   22.601   22.601 <string>:1(<module>)
       46   17.963    0.391   21.625    0.470 ex 03 v2.py:13(transformar)
        1    0.222    0.222   22.031   22.031 ex 03 v2.py:24(hanoi)
        1    0.000    0.000   22.601   22.601 {built-in method builtins.exec}
 33554405    3.662    0.000    3.662    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       23    0.183    0.008    0.183    0.008 {method 'extend' of 'list' objects}
'''
