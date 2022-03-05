'''
The variables are the words, and the domains are the possible locations of those words.
For the purposes of expediency, our word search will not include words that overlap.
You can improve it to allow for overlapping words as an exercise.
'''

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from random import choice

from csp_repetido import CSP, Constraint
Grid = List[List[str]]  # type alias for grids
class GridLocation(NamedTuple):
    row: int
    column: int

    def __repr__(self):
        return f'<{self.row},{self.column}>'
'''
Initially, we will fill the grid with the letters of the English alphabet (ascii_
uppercase). We will also need a function for displaying the grid.
'''
def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase)
             for column in range(columns)]
            for row in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))



# Función que calcula para cada variable (palabra a buscar)
# su dominio, esto es, la lista con las localizaciones en las que podría estar
def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length)
            rows: range = range(row, row + length)
            if col + length <= width:
                # left to right
                domain.append([GridLocation(row, c) for c in columns])
                # diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            if row + length <= height:
                # top to bottom
                domain.append([GridLocation(r, col) for r in rows])
                # diagonal towards bottom left
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain


class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        # if there are any duplicates grid locations then there is an overlap
        all_locations = [locs for values in assignment.values() for locs in values]
        return len(set(all_locations)) == len(all_locations)




if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            # random reverse half the time
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)