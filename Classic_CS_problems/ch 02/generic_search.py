from __future__ import annotations

from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
# from typing_extensions import Protocol
from heapq import heappush, heappop
from collections import deque


'''
C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other
'''

T = TypeVar('T')


def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


def binary_contains(sequence: Sequence[T], key: T) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def pop(self) -> T:
        return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

    def __repr__(self) -> str:
        return repr(self._container)

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: Deque[T] = deque()

    def pop(self) -> T:
        return self._container.popleft()

    def push(self, item: T) -> None:
        self._container.append(item)

    def __repr__(self) -> str:
        return repr(self._container)

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container


# Para poder referenciar dentro de Node al mismo Node es necesario
# from __future__ import annotations, para aceptar anotaciones...
class Node(Generic[T]):
    # Podría representar, por ejemplo, cada MazeLocation de un laberinto, etc...
    # Lo importante es que guarda información del estado anterior!!!
    # Lo utilizamos en algoritmos de búsqueda
    # los campos costo y heurística los usamos en otros algoritmos!!
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]])\
        -> tuple[int, Optional[Node[T]]]:
    # el retorno es una tupla, con el número de veces que tardamos, y el nodo...
    """
    Es muy potente porque es general... valdría para cualquier estructura, laberinto, etc.
    Lo único que necesitamos es:
    * Darle una situación inicial,
    * Un callable que nos permite obtener sucesores,
    * Un callable que nos permite si ya hemos conseguido nuestro objetivo
    El resultado podría ser un Nodo (final) que representa el resultado, ya que
    se puede recorrer en sentido inverso para ver donde hemos estado
    """
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, parent=None))
    explored: Set[T] = {initial}
    estados_recorridos = 0
    while not frontier.empty:
        estados_recorridos += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return estados_recorridos, current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, parent=current_node))
    return estados_recorridos, None  # went through everything and never found goal


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]])\
        -> tuple[int, Optional[Node[T]]]:
    # el retorno es una tupla, con el número de veces que tardamos, y el nodo...
    """
    El algoritmo es exactamente el mismo que del de Depth First Search...
    La diferencia está en que utilizamos una cola en lugar de un stack...
    Por ello al hacer pop para ampliar la frontera, iremos mirando primero los vecinos más cercanos
    """
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, parent=None))
    explored: Set[T] = {initial}
    estados_recorridos = 0
    while not frontier.empty:
        estados_recorridos += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return estados_recorridos, current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, parent=current_node))
    return estados_recorridos, None  # went through everything and never found goal


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


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

    # Importante
    '''
    To determine the priority of a particular element versus another of its kind,
    heappush() and heappop(), compare them by using the < operator.
    This is why we needed to implement __lt__() on Node earlier.
    One Node is compared to another by looking at its respective f(n),
    which is simply the sum of the properties cost and heuristic
    '''


def astar(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]],
          heuristic: Callable[[T], float]) -> tuple[int, Optional[Node[T]]]:
    # Algoritmo de búsqueda A*
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, parent=None, cost=0.0, heuristic=heuristic(initial)))
    # ¡O sea, el costo inicial es 0, pq partimos del nodo initial, no hay que moverse!
    explored: Dict[T, float] = {initial: 0.0}
    estados_recorridos = 0
    while not frontier.empty:
        estados_recorridos += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return estados_recorridos, current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            '''
            Se podría mejorar para casos generales, de momento nos vale así suponiendo un grid
            en el que nos movemos horizontal o vertical... entonces, al dar un paso más, el costo
            es el costo actual más 1.
            '''
            if child not in explored or explored[child] > new_cost:
                # ¡O sea, podemos añadirlo incluso si ya está, si el costo calculado es menos que el que figura!!
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return estados_recorridos, None  # went through everything and never found goal








