from __future__ import annotations

from typing import Generic, TypeVar, List, Optional, Callable, Set, Deque
from collections import deque


T = TypeVar('T')


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


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    """
    Es muy potente porque es general... valdría para cualquier estructura, laberinto, etc...
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

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, parent=current_node))
    return None

def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    """
    El algoritmo es exactamente el mismo que del de Depth First Search...
    La diferencia está en que utilizamos una cola en lugar de un stack...
    Por ello al hacer pop para ampliar la frontera, iremos mirando primero los vecinos más cercanos
    """
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, parent=None))
    explored: Set[T] = {initial}

    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, parent=current_node))





def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path








