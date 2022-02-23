"""
Write a solver for The Towers of Hanoi that works for any number of towers.
Puedo hacer una función que solucione de forma recursiva
pero utilizando la memoization
la función returna una lista de tupla con los movimientos
def hanoi(num platos) List[Tuple(inicio, fin)
donde la primera componenete es de donde sale el disco , y la segunda
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


# resultado = hanoi_symbol('I', 'F', 'A', 5)
# print(resultado)
cProfile.run("hanoi_symbol('I', 'F', 'A', 20)")