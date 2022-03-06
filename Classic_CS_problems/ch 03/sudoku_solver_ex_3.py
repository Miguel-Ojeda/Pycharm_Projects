import cProfile
import pprint
import sys
from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from random import choice
from typing import Literal
from dataclasses import dataclass

from csp_repetido import CSP, Constraint

Numero_1_al_9 = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]

class SudokuLocation(NamedTuple):
    row: int
    column: int


class SudokuConstraint(Constraint[List[SudokuLocation], List[Numero_1_al_9]]):
    def __init__(self, variables: List[SudokuLocation]) -> None:
        super().__init__(variables)

    def satisfied(self, assignment: Dict[SudokuLocation, Numero_1_al_9]) -> bool:
        asignadas: List[SudokuLocation] = list(assignment.keys())
        # comprobar fila
        for row in range(9):
            celdas_asignadas = {SudokuLocation(row=row, column=c)
                                for c in range(9)
                                if SudokuLocation(row=row, column=c) in asignadas}
            valores_asignados = {assignment[celda] for celda in celdas_asignadas}
            if len(celdas_asignadas) != len(valores_asignados):
                return False
        # comprobar columnas
        for column in range(9):
            celdas_asignadas = {SudokuLocation(row=r, column=column)
                                for r in range(9)
                                if SudokuLocation(row=r, column=column) in asignadas}
            valores_asignados = {assignment[celda] for celda in celdas_asignadas}
            if len(celdas_asignadas) != len(valores_asignados):
                return False

        # Ahora comprobar cuadrados
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                celdas_asignadas = {SudokuLocation(row=(row + dr), column=(column + dc))
                                    for dr in (0, 1, 2)
                                    for dc in (0, 1, 2)
                                    if SudokuLocation(row=(row + dr), column=(column + dc)) in asignadas}
                valores_asignados = {assignment[celda] for celda in celdas_asignadas}
                if len(celdas_asignadas) != len(valores_asignados):
                    return False

        return True


if __name__ == "__main__":
    locations = [SudokuLocation(row=row, column=column) for row in range(9) for column in range(9)]
    domains: Dict[SudokuLocation, List[Numero_1_al_9]]
    domains = {location: [1, 2, 3, 4, 5, 6, 7, 8, 9] for location in locations}

    '''aquí añadiríamos las propias condiciones del tal'''
    assginment_inicial : Dict[SudokuLocation, Numero_1_al_9]
    # Ejemplo 1
    assginment_inicial = {SudokuLocation(row=0, column=0): 5, SudokuLocation(row=0, column=1): 3,
                          SudokuLocation(row=0, column=4): 7, SudokuLocation(row=1, column=0): 6,
                          SudokuLocation(row=1, column=3): 1, SudokuLocation(row=1, column=4): 9,
                          SudokuLocation(row=1, column=5): 5, SudokuLocation(row=2, column=1): 9,
                          SudokuLocation(row=2, column=2): 8, SudokuLocation(row=2, column=7): 6,
                          SudokuLocation(row=3, column=0): 8, SudokuLocation(row=3, column=4): 6,
                          SudokuLocation(row=3, column=8): 3, SudokuLocation(row=4, column=0): 4,
                          SudokuLocation(row=4, column=3): 8, SudokuLocation(row=4, column=5): 3,
                          SudokuLocation(row=4, column=8): 1, SudokuLocation(row=5, column=0): 7,
                          SudokuLocation(row=5, column=4): 2, SudokuLocation(row=5, column=8): 6,
                          SudokuLocation(row=6, column=1): 6, SudokuLocation(row=6, column=6): 2,
                          SudokuLocation(row=6, column=7): 8, SudokuLocation(row=7, column=3): 4,
                          SudokuLocation(row=7, column=4): 1, SudokuLocation(row=7, column=5): 9,
                          SudokuLocation(row=7, column=8): 5, SudokuLocation(row=8, column=4): 8,
                          SudokuLocation(row=8, column=7): 7, SudokuLocation(row=8, column=8): 9,
                          }
    '''
    SOLUCIÓN
     5  3  4  6  7  8  9  1  2 
     6  7  2  1  9  5  3  4  8 
     1  9  8  3  4  2  5  6  7 
     8  5  9  7  6  1  4  2  3 
     4  2  6  8  5  3  7  9  1 
     7  1  3  9  2  4  8  5  6 
     9  6  1  5  3  7  2  8  4 
     2  8  7  4  1  9  6  3  5 
     3  4  5  2  8  6  1  7  9 
     '''

    # Ejemplo 2
    '''
    assginment_inicial = {SudokuLocation(row=0, column=0): 1,
                          SudokuLocation(row=0, column=4): 9,
                          # SudokuLocation(row=0, column=6): 8,

                          SudokuLocation(row=1, column=0): 9,
                          SudokuLocation(row=1, column=3): 8,
                          # SudokuLocation(row=1, column=6): 1,
                          # SudokuLocation(row=1, column=5): 5,

                          SudokuLocation(row=2, column=1): 3,
                          SudokuLocation(row=2, column=2): 2,
                          SudokuLocation(row=2, column=7): 8,

                          SudokuLocation(row=3, column=4): 8,
                          SudokuLocation(row=3, column=5): 4,
                          SudokuLocation(row=3, column=6): 9,
                          SudokuLocation(row=3, column=7): 3,

                          SudokuLocation(row=4, column=4): 2,
                          SudokuLocation(row=4, column=8): 8,
                          # SudokuLocation(row=4, column=5): 3,
                          # SudokuLocation(row=4, column=8): 1,

                          SudokuLocation(row=5, column=0): 5,
                          SudokuLocation(row=5, column=1): 2,
                          SudokuLocation(row=5, column=7): 1,

                          SudokuLocation(row=6, column=2): 4,
                          SudokuLocation(row=6, column=3): 9,
                          SudokuLocation(row=6, column=4): 5,
                          SudokuLocation(row=6, column=6): 8,

                          SudokuLocation(row=7, column=1): 5,
                          SudokuLocation(row=7, column=6): 1,
                          SudokuLocation(row=7, column=7): 7,
                          # SudokuLocation(row=7, column=8): 5,

                          SudokuLocation(row=8, column=5): 7,
                          # SudokuLocation(row=8, column=7): 7,
                          # SudokuLocation(row=8, column=8): 9,
                          }
    '''
    '''SOLUCIÓN EJEMPLO 2"
     1  8  5  6  9  2  3  4  7 
     9  4  6  8  7  3  5  2  1 
     7  3  2  4  1  5  6  8  9 
     6  1  7  5  8  4  9  3  2 
     4  9  3  1  2  6  7  5  8 
     5  2  8  7  3  9  4  1  6 
     2  7  4  9  5  1  8  6  3 
     3  5  9  2  6  8  1  7  4 
     8  6  1  3  4  7  2  9  5 
     
     El cProfile es el siguiente...
             194_569_966 function calls (194500610 primitive calls) in 168.419 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 84633110   27.782    0.000   44.455    0.000 <string>:1(<lambda>)
        1    0.000    0.000  168.419  168.419 <string>:1(<module>)
   623968    0.888    0.000  166.501    0.000 csp_repetido.py:42(consistent)
  69357/1    0.982    0.000  168.419  168.419 csp_repetido.py:48(backtracking_search)
    69356    0.565    0.000    0.565    0.000 csp_repetido.py:53(<listcomp>)
   623968   14.355    0.000  165.613    0.000 sudoku_solver_ex_3.py:24(satisfied)
  3451980   61.123    0.000   89.366    0.000 sudoku_solver_ex_3.py:28(<setcomp>)
  3451980    3.677    0.000    3.677    0.000 sudoku_solver_ex_3.py:31(<setcomp>)
  1446861   24.708    0.000   35.306    0.000 sudoku_solver_ex_3.py:36(<setcomp>)
  1446861    1.412    0.000    1.412    0.000 sudoku_solver_ex_3.py:39(<setcomp>)
   733770   13.699    0.000   19.313    0.000 sudoku_solver_ex_3.py:46(<setcomp>)
   733770    0.740    0.000    0.740    0.000 sudoku_solver_ex_3.py:50(<setcomp>)
 84633110   16.673    0.000   16.673    0.000 {built-in method __new__ of type object at 0x00007FFE7A21B920}
        1    0.000    0.000  168.419  168.419 {built-in method builtins.exec}
 11403936    1.361    0.000    1.361    0.000 {built-in method builtins.len}
   623968    0.349    0.000    0.349    0.000 {method 'copy' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   623968    0.106    0.000    0.106    0.000 {method 'keys' of 'dict' objects}
     
     
 '''


    csp: CSP[SudokuLocation, int] = CSP(locations, domains)
    csp.add_constraint(SudokuConstraint(locations))
    solution: Optional[Dict[SudokuLocation, Numero_1_al_9]] = csp.backtracking_search(assginment_inicial)
    cProfile.run('solution = csp.backtracking_search(assginment_inicial)')


    # solution: Optional[Dict[SudokuLocation, Numero_1_al_9]] = csp.backtracking_search(assginment_inicial)
    if solution is None:
        print("No solution found!")
    else:
        for row in range(9):
            fila = ''.join(str(solution[SudokuLocation(row=row, column=c)]).center(3) for c in range(9))
            print(fila)

    '''
    domains[SudokuLocation(row=0, column=0)] = [5]
    domains[SudokuLocation(row=0, column=1)] = [3]
    domains[SudokuLocation(row=0, column=4)] = [7]
    domains[SudokuLocation(row=1, column=0)] = [6]
    domains[SudokuLocation(row=1, column=3)] = [1]
    domains[SudokuLocation(row=1, column=4)] = [9]
    domains[SudokuLocation(row=1, column=5)] = [5]
    domains[SudokuLocation(row=2, column=1)] = [9]
    domains[SudokuLocation(row=2, column=2)] = [8]
    domains[SudokuLocation(row=2, column=7)] = [6]
    domains[SudokuLocation(row=3, column=0)] = [8]
    domains[SudokuLocation(row=3, column=4)] = [6]
    domains[SudokuLocation(row=3, column=8)] = [3]
    domains[SudokuLocation(row=4, column=0)] = [4]
    domains[SudokuLocation(row=4, column=3)] = [8]
    domains[SudokuLocation(row=4, column=5)] = [3]
    domains[SudokuLocation(row=4, column=8)] = [1]
    domains[SudokuLocation(row=5, column=0)] = [7]
    domains[SudokuLocation(row=5, column=4)] = [2]
    domains[SudokuLocation(row=5, column=8)] = [6]
    domains[SudokuLocation(row=6, column=1)] = [6]
    domains[SudokuLocation(row=6, column=6)] = [2]
    domains[SudokuLocation(row=6, column=7)] = [8]
    domains[SudokuLocation(row=7, column=3)] = [4]
    domains[SudokuLocation(row=7, column=4)] = [1]
    domains[SudokuLocation(row=7, column=5)] = [9]
    domains[SudokuLocation(row=7, column=8)] = [5]
    domains[SudokuLocation(row=8, column=4)] = [8]
    domains[SudokuLocation(row=8, column=7)] = [7]
    domains[SudokuLocation(row=8, column=8)] = [9]
    '''










