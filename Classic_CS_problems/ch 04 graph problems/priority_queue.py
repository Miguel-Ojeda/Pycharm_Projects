"""
Esto es simplemente lo que teníamos del capítulo 2 en el fichero generic search
pero la parte de cola por prioridades, para poder utilizarlo más cómodamente
en la implementación del minimum spanning tree (el subárbol dentro de un grafo con pesos
que tiene el menor peso total
"""

"""
Observar que nosotros utilziaremos esta cola por prioridades para extraer el menor
nodo... esto lo podemos hacer pq los nodos tienen definidos el __lt__
"""
from typing import List, Generic, TypeVar
from heapq import heappush, heappop

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        # in by priority
        heappush(self._container, item)

    def pop(self) -> T:
        # out by priority
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)