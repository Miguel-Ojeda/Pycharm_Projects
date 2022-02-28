# Resolución de laberintos don depth first search
from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, Node, node_to_path, bfs


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
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: Optional[MazeLocation] = None) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start

        if goal is None:
            goal = MazeLocation(row=rows-1, column=columns - 1)
        self.goal: MazeLocation = goal
        '''
        El grid es una lista de filas de celdas.... grid = [fila-1, fila-2, fila-3, ...]
        Inicialmente rellenamos todo con celdas vacías
        '''
        self._grid: List[List[Cell]] = [[Cell.EMPTY for _ in range(columns)] for _ in range(rows)]
        # populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)
        # fill the start and goal locations in
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.random() < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self):
        output = ''
        for row in self._grid:
            output += ' '.join([cell.value for cell in row]) + '\n'
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, location: MazeLocation) -> List[MazeLocation]:
        # Nos dice a donde podemos ir desde nuestra ubicación.... que esté libre
        locations: List[MazeLocation] = []
        if location.row + 1 < self._rows and self._grid[location.row + 1][location.column] != Cell.BLOCKED:
            locations.append(MazeLocation(location.row + 1, location.column))
        if location.row - 1 >= 0 and self._grid[location.row - 1][location.column] != Cell.BLOCKED:
            locations.append(MazeLocation(location.row - 1, location.column))
        if location.column + 1 < self._columns and self._grid[location.row][location.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(location.row, location.column + 1))
        if location.column - 1 >= 0 and self._grid[location.row][location.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(location.row, location.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == '__main__':
    laberinto = Maze(rows=10, columns=10, sparseness=.22)
    print(laberinto)
    solution_1: Optional[Node[MazeLocation]] = dfs(laberinto.start, laberinto.goal_test, laberinto.successors)
    if solution_1 is None:
        print('No tiene solución DFS el laberinto')
    else:
        path_1 = node_to_path(solution_1)
        laberinto.mark(path_1)
        print(laberinto)
        laberinto.clear(path_1)

    solution_2: Optional[Node[MazeLocation]] = bfs(laberinto.start, laberinto.goal_test, laberinto.successors)
    if solution_2 is None:
        print('No tiene solución  BFS el laberinto')
    else:
        path_2 = node_to_path(solution_2)
        laberinto.mark(path_2)
        print(laberinto)
        laberinto.clear(path_2)