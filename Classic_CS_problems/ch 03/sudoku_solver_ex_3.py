import pprint
import sys
from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from random import choice
from typing import Literal
from dataclasses import dataclass

from csp_repetido import CSP, Constraint

Numeros_1_al_9 = Optional[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]]

'''
@dataclass
class Mini_linea:
    item_1: Numeros_1_al_9
    item_2: Numeros_1_al_9
    item_3: Numeros_1_al_9
    
    def __init__(self):
        item_1 = item_2 = item_3 = None
        
    def elementos(self) -> set[Numeros_1_al_9]:
        return {self.item_1, self.item_2, self.item_3}

@dataclass
class Tres_mini_lineas:
    linea_1: Mini_linea
    linea_2: Mini_linea
    linea_3: Mini_linea
    
    def __init__(self):
        linea_1 = Mini_linea()
        linea_2 = Mini_linea()
        Linea_3 = Mini_linea()
        
    def elementos(self) -> set[Numeros_1_al_9]:
        return self.linea_1.elementos() | self.linea_2.elementos() | self.linea_3.elementos()
'''
'''
@dataclass
class Sudoku:
    cuadrados: List[Tres_mini_lineas]
    def __init__(self):
        for i in range(9):
            self.cuadrados[i] = Tres_mini_lineas()
'''

Sudoku = List[List[Numeros_1_al_9]]  # type alias for grids
def generate_Sudoku() -> Sudoku:
    valor: Numeros_1_al_9 = None
    return [[valor for c in range(9)] for r in range(9)]


def display_Sudoku(sudoku: Sudoku):
    for row in sudoku:
        print(''.join(str(row[col]).center(6) for col in range(9)))

class SudokuLocation(NamedTuple):
    column: int
    row: int
    def __repr__(self):
        return f'<{self.column}, {self.row}>'

class SudokuConstraint(Constraint[List[SudokuLocation], List[Numeros_1_al_9]]):
    def __init__(self, variables: List[Numeros_1_al_9]) -> None:
        super().__init__(variables)

    def satisfied(self, assignment: Dict[Numeros_1_al_9, List[SudokuLocation]]) -> bool:
        '''
        locations: List[GridLocation]
        for indice, (palabra, locations) in enumerate(assignment.items()):
            # compruebo si la palabra actual tiene alguna localización en común
            # con alguna de las palabras posteriores restantes...
            resto_palabras = list(assignment.keys())
            resto_palabras.remove(palabra)
            for otra_palabra in resto_palabras:
                grid_locations_comunes = set(locations) & set(assignment[otra_palabra])
                if grid_locations_comunes == set():
                    continue  # No hay que realizar ninguna comprobación

                for grid_location in grid_locations_comunes:
                    indice_palabra_actual = locations.index(grid_location)
                    indice_otra_palabra = assignment[otra_palabra].index(grid_location)
                    letra_palabra_actual = palabra[indice_palabra_actual]
                    letra_otra_palabra = otra_palabra[indice_otra_palabra]
                    if letra_otra_palabra != letra_palabra_actual:
                        return False
        '''
        return True


if __name__ == "__main__":
    sudoku = generate_Sudoku()

    # for row in sudoku:
    #     print(row)
    # # sys.exit()
    # display_Sudoku(sudoku)
    #
    # sys.exit()
    # grid: Grid = generate_grid(9, 9)
    # words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY", 'MIGUEL', 'BRAULIO', 'ANA', 'MARYO']

    domains: Dict[int, List[Numeros_1_al_9]] = {}
    for row in sudoku:
        for col in row:
            domains[sudoku[row][col]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, List[GridLocation]] = CSP(words, locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            # random reverse half the time
            '''Quito la opción de dar la vuelta, pq daría error ahora
            ya que admitimos el overlapping de palabras si la letra es igual'''
            # if choice([True, False]):
            #     grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)