# Resolución de laberintos don depth first search
from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt


class Cell(Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


'''
podemos hacerlo tb en formato api...
Cell = Enum('Cell', 'EMPTY BLOCKED ... '))
pero creo que no podríamos anotar ni los valores ni los tipos
'''


class MazeLocation(NamedTuple):
    row: int
    column: int


'''
Equivalente a:
MazeLocation = NamedTuple('MazeLocation', 'row column' ó (row, column))
Pero no podríamos anotar los tipos!!
'''


# Generación aleatoria del laberinto... usamos un valor, sparseness, para configurar los huecos que hay
class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # Rellenamos el tablero todo de celdas vacías...
        self._grid: List[List[Cell]] = [[Cell.EMPTY for _ in range(columns)] for _ in range(rows)]


