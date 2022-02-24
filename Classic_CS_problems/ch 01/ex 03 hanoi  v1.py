"""
Write a solver for The Towers of Hanoi that works for any number of towers.
Puedo hacer una función que solucione de forma recursiva
pero utilizando la memoization
la función retorna una lista de tupla con los movimientos
def hanoi(num platos) List[Tuple(inicio, fin)
donde la primera componente es de donde sale el disco, y la segunda
hasta que columna va
Las columnas puedesn ser Inicial, Auxiliar, o Final
"""

from typing import TypeVar, Generic, List, Tuple
T = TypeVar('T')
import cProfile


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)



def hanoi_symbol(inicial: str, final: str, auxiliar: str, n: int) -> List[Tuple[str, str]]:
    """Función que retorna una lista con la solución
    La solución consiste en una lista de tuplas... del tipo
    (origen, fin)
    Ejemplo: [(I, A), (I, F), (A, F)]
    Es la solución al problema de n = 2
    Pasamos de la columna inicial, a la del medio, luego de la inicial a la final,
    y por último de la auxiliar al final"""
    if n == 1:
        return [(inicial, final)]
    else:
        anterior_1 = hanoi_symbol(inicial=inicial, final=auxiliar, auxiliar=final, n=n-1)
        hanoi_1 = hanoi_symbol(inicial=inicial, final=final, auxiliar=auxiliar, n=1)
        anterior_2 = hanoi_symbol(inicial=auxiliar, final=final, auxiliar=inicial, n=n-1)
        anterior_1.extend(hanoi_1)
        anterior_1.extend(anterior_2)
        return anterior_1


resultado = hanoi_symbol('I', 'F', 'A', 3)
print(resultado)
'''
[('I', 'F'), ('I', 'A'), ('F', 'A'), ('I', 'F'), ('A', 'I'), ('A', 'F'), ('I', 'F'),
('I', 'A'), ('F', 'A'), ('F', 'I'), ('A', 'I'), ('F', 'A'), ('I', 'F'), ('I', 'A'),
('F', 'A'), ('I', 'F'), ('A', 'I'), ('A', 'F'), ('I', 'F'), ('A', 'I'), ('F', 'A'),
('F', 'I'), ('A', 'I'), ('A', 'F'), ('I', 'F'), ('I', 'A'), ('F', 'A'), ('I', 'F'),
('A', 'I'), ('A', 'F'), ('I', 'F')]
'''
resultado = hanoi_symbol('I', 'F', 'A', 6)
print(resultado)
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
cProfile.run("hanoi_symbol('I', 'F', 'A', 20)")
'''
2_621_439 function calls (1048578 primitive calls) in 1.361 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.024    0.024    1.361    1.361 <string>:1(<module>)
1_572_862/1    1.152    0.000    1.337    1.337 ex 03 v1.py:40(hanoi_symbol)
        1    0.000    0.000    1.361    1.361 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1048574    0.185    0.000    0.185    0.000 {method 'extend' of 'list' objects}
'''

# Vemos que como es una función recursiva, hanoi symbol se llama en total más de 1 millón y medio de veces
# en total, 1.3 sec


cProfile.run("hanoi_symbol('I', 'F', 'A', 24)")
'''
         41943039 function calls (16777218 primitive calls) in 22.823 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.399    0.399   22.823   22.823 <string>:1(<module>)
25165822/1   19.186    0.000   22.423   22.423 ex 03 v1.py:40(hanoi_symbol)
        1    0.000    0.000   22.823   22.823 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 16777214    3.237    0.000    3.237    0.000 {method 'extend' of 'list' objects}



Process finished with exit code 0
'''