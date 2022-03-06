'''
The variables are the words, and the domains are the possible locations of those words.
For the purposes of expediency, our word search will not include words that overlap.
You can improve it to allow for overlapping words as an exercise.
'''
import pprint
import sys
from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from random import choice

from csp_repetido import CSP, Constraint
Grid = List[List[str]]  # type alias for grids


class GridLocation(NamedTuple):

    column: int
    row: int

    def __repr__(self):
        return f'<{self.column}, {self.row}>'


class Box(NamedTuple):

    columns: int
    rows: int
    id: int  # Lo usamos para el display en el grid....

'''
Initially, we will fill the grid with spaces
'''
def generate_grid(rows: int, columns: int) -> Grid:
    return [['*' for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))



# Función que calcula para cada variable (palabra a buscar)
# su dominio, esto es, la lista con las localizaciones en las que podría estar
def generate_domain(box: Box, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length_x: int = box.columns
    length_y: int = box.rows
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length_x)
            rows: range = range(row, row + length_y)
            if col + length_x <= width and row + length_y <= height:
                domain.append([GridLocation(c, r) for r in rows for c in columns ])
    return domain


class BoxAllocationConstraint(Constraint[Box, List[GridLocation]]):
    def __init__(self, boxes: List[Box]) -> None:
        super().__init__(boxes)
        # self.words: List[str] = words

    def satisfied(self, assignment: Dict[Box, List[GridLocation]]) -> bool:
        # if there are any duplicates grid locations then there is an overlap
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)





if __name__ == '__main__':
    grid: Grid = generate_grid(9, 9)
    box_1 = Box(columns=1, rows=6, id=1)
    box_2 = Box(columns=4, rows=4, id=2)
    box_3 = Box(columns=3, rows=3, id=3)
    box_4 = Box(columns=2, rows=2, id=4)
    box_5 = Box(columns=5, rows=2, id=5)
    box_6 = Box(columns=3, rows=7, id=6)
    box_7 = Box(columns=3, rows=2, id=7)
    box_8 = Box(columns=2, rows=3, id=8)
    box_9 = Box(columns=1, rows=2, id=9)

    box_list = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]

    ocupacion = 0
    for box in box_list:
        ocupacion += box.columns * box.rows
    print(ocupacion, '/', len(grid)*len(grid[0]))

    location = generate_domain
    # # resultado = generate_domain(box_2, grid)
    # for row in resultado:
    #     print(row)
    # sys.exit()
    locations: Dict[Box, List[List[GridLocation]]] = {}
    for box in box_list:
        locations[box] = generate_domain(box, grid)

    casos = 1
    for box in box_list:
        casos *= len(locations[box])
    print(f'Los casos a buscar serían: {casos:_}')



    csp: CSP[Box, List[GridLocation]] = CSP(box_list, locations)

    csp.add_constraint(BoxAllocationConstraint(box_list))

    solution: Optional[Dict[Box, List[GridLocation]]] = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
    else:
        for box, grid_locations in solution.items():
            for location in grid_locations:
                grid[location.row][location.column] = str(box.id)
        display_grid(grid)





