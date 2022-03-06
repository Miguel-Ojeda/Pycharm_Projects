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


def heuristica(celda: SudokuLocation, assignment: Dict[SudokuLocation, Numero_1_al_9]) -> float:
    '''básicamente lo que haremos será asignar a la celda, el número de restricciones
    que posee, o sea, miraremos en las asignaciones y veremos cuantas valores están
    asignados en su fila, columna y cuadrado...
    mientras más restricciones tenga, pues mejor, pq teóricamente debería ser más fácil encontrar
    el valor correcto!!!!
    '''
    celdas_asignadas_fila = {SudokuLocation(row=celda.row, column=c)
                             for c in range(9)
                             if SudokuLocation(row=celda.row, column=c) in assignment}

    celdas_asignadas_columna = {SudokuLocation(row=r, column=celda.column)
                                for r in range(9)
                                if SudokuLocation(row=r, column=celda.column) in assignment}

    # Hallamos ahora la celda donde empieza el cuadrado
    start_row = (celda.row // 3) * 3
    start_column = (celda.column // 3) * 3

    celdas_asignadas_cuadrado = {SudokuLocation(row=start_row + dr, column=start_column + dc)
                                 for dr in (0, 1, 2)
                                 for dc in (0, 1, 2)
                                 if SudokuLocation(row=start_row + dr, column=start_column + dc) in assignment}

    celdas_asignadas = celdas_asignadas_cuadrado | celdas_asignadas_columna | celdas_asignadas_cuadrado
    return len(celdas_asignadas)


def heuristica_con_restriccion(celda: SudokuLocation, assignment: Dict[SudokuLocation, Numero_1_al_9]) \
        -> tuple[float, List[Numero_1_al_9]]:
    '''Es lo mismo que antes, pero tb devolvemos los valores que puede tomar
    '''
    celdas_asignadas_fila = {SudokuLocation(row=celda.row, column=c)
                             for c in range(9)
                             if SudokuLocation(row=celda.row, column=c) in assignment}

    celdas_asignadas_columna = {SudokuLocation(row=r, column=celda.column)
                                for r in range(9)
                                if SudokuLocation(row=r, column=celda.column) in assignment}

    # Hallamos ahora la celda donde empieza el cuadrado
    start_row = (celda.row // 3) * 3
    start_column = (celda.column // 3) * 3

    celdas_asignadas_cuadrado = {SudokuLocation(row=start_row + dr, column=start_column + dc)
                                 for dr in (0, 1, 2)
                                 for dc in (0, 1, 2)
                                 if SudokuLocation(row=start_row + dr, column=start_column + dc) in assignment}

    celdas_asignadas = celdas_asignadas_cuadrado | celdas_asignadas_columna | celdas_asignadas_cuadrado
    valores_asignados = set(assignment[celda] for celda in celdas_asignadas)
    dominio = [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9] if i not in valores_asignados]
    return len(celdas_asignadas), dominio


if __name__ == "__main__":
    locations = [SudokuLocation(row=row, column=column) for row in range(9) for column in range(9)]
    domains: Dict[SudokuLocation, List[Numero_1_al_9]]
    domains = {location: [1, 2, 3, 4, 5, 6, 7, 8, 9] for location in locations}

    '''aquí añadiríamos las propias condiciones del tal'''
    # Ejemplo 1
    assginment_inicial_1: Dict[SudokuLocation, Numero_1_al_9]
    assginment_inicial_1 = {SudokuLocation(row=0, column=0): 5, SudokuLocation(row=0, column=1): 3,
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
    assginment_inicial_2: Dict[SudokuLocation, Numero_1_al_9]
    assginment_inicial_2 = {SudokuLocation(row=0, column=0): 1,
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
  '''

    # Ejemplo 3
    assginment_inicial_3: Dict[SudokuLocation, Numero_1_al_9]
    assginment_inicial_3 = {SudokuLocation(row=0, column=1): 1,
                            SudokuLocation(row=0, column=2): 3,
                            SudokuLocation(row=0, column=3): 9,

                            SudokuLocation(row=1, column=1): 5,
                            SudokuLocation(row=1, column=5): 4,
                            # SudokuLocation(row=1, column=6): 1,
                            # SudokuLocation(row=1, column=5): 5,

                            SudokuLocation(row=2, column=4): 3,
                            SudokuLocation(row=2, column=6): 1,
                            SudokuLocation(row=2, column=7): 5,

                            SudokuLocation(row=3, column=0): 2,
                            SudokuLocation(row=3, column=2): 7,
                            SudokuLocation(row=3, column=3): 4,
                            SudokuLocation(row=3, column=5): 5,
                            SudokuLocation(row=3, column=6): 3,

                            SudokuLocation(row=4, column=4): 1,
                            # SudokuLocation(row=4, column=8): 8,
                            # SudokuLocation(row=4, column=5): 3,
                            # SudokuLocation(row=4, column=8): 1,

                            SudokuLocation(row=5, column=2): 1,
                            SudokuLocation(row=5, column=3): 6,
                            SudokuLocation(row=5, column=5): 9,
                            SudokuLocation(row=5, column=6): 2,
                            SudokuLocation(row=5, column=8): 4,

                            SudokuLocation(row=6, column=1): 2,
                            SudokuLocation(row=6, column=2): 8,
                            SudokuLocation(row=6, column=4): 9,
                            # SudokuLocation(row=6, column=6): 8,

                            SudokuLocation(row=7, column=3): 5,
                            SudokuLocation(row=7, column=7): 6,
                            # SudokuLocation(row=7, column=7): 7,
                            # SudokuLocation(row=7, column=8): 5,

                            SudokuLocation(row=8, column=5): 1,
                            SudokuLocation(row=8, column=6): 8,
                            SudokuLocation(row=8, column=7): 3,
                            }

    csp: CSP[SudokuLocation, Numero_1_al_9] = CSP(locations, domains)
    csp.add_constraint(SudokuConstraint(locations))
    # solution: Optional[Dict[SudokuLocation, Numero_1_al_9]] = csp.backtracking_search(assginment_inicial)
    # cProfile.run('solution = csp.backtracking_search(assginment_inicial)')

    # solution: Optional[Dict[SudokuLocation, Numero_1_al_9]] = csp.backtracking_search(assginment_inicial)
    # solution = csp.backtracking_search_heuristic(heuristic=heuristica,  assignment=assginment_inicial_2)
    # solution = csp.bts_heuristic_con_restriccion(heuristic_restrict=heuristica_con_restriccion,
    #                                              assignment=assginment_inicial_2)
    # solution = csp.bts_heuristic_con_restriccion(heuristic_restrict=heuristica_con_restriccion,
    #                                              assignment=assginment_inicial_3)

    '''
    if solution is None:
        print("No solution found!")
    else:
        for row in range(9):
            fila = ''.join(str(solution[SudokuLocation(row=row, column=c)]).center(3) for c in range(9))
            print(fila)
    sys.exit()
    '''
    # cProfile.run('csp.backtracking_search(assginment_inicial_1)')
    # Ejemplo 1: 11_739_020 function calls (11734812 primitive calls) in 9.864 seconds
    # cProfile.run('csp.backtracking_search_heuristic(heuristic=heuristica,  assignment=assginment_inicial_1)')
    # Ejemplo 1: 307677 function calls (307609 primitive calls) in 0.229 seconds
    # En concreto, en la función heurística casi no tarda nada, 0.008 segundos!!
    # 1975    0.008    0.000    0.099    0.000 sudoku_solver_ex_3.py:58(heuristica)
    # cProfile.run('csp.backtracking_search(assginment_inicial_2)')
    # Ejemplo 2: 194_569_966 function calls (194500610 primitive calls) in 167.131 seconds
    # cProfile.run('csp.backtracking_search_heuristic(heuristic=heuristica,  assignment=assginment_inicial_2)')
    # Ejemplo 2: 2874801 function calls (2874328 primitive calls) in 2.124 seconds
    # En concreto, la heurística consume poco, 0'072 segundos
    # 18484    0.072    0.000    0.897    0.000 sudoku_solver_ex_3.py:58(heuristica)
    # cProfile.run('csp.bts_heuristic_con_restriccion(heuristica_con_restriccion, assginment_inicial_2)')
    # 2050200 function calls (2049727 primitive calls) in 1.501 seconds

    # Ejemplo 3
    # Método 1, algoritmo clásico backsearch...
    cProfile.run('csp.backtracking_search(assginment_inicial_3)')
    # >>> 125260256 function calls (125222633 primitive calls) in 108.425 seconds

    # Método 2, algoritmo backsearch con heurística para elegir la siguiente celda a asignar
    cProfile.run('csp.backtracking_search_heuristic(heuristic=heuristica,  assignment=assginment_inicial_3)')
    # >>> 2781175 function calls (2780636 primitive calls) in 2.138 seconds

    # Método 3, con huerística para elegir la siguiente celda, y que limita el dominio de cada celda
    cProfile.run('csp.bts_heuristic_con_restriccion(heuristica_con_restriccion, assginment_inicial_3)')
    # >>> 1880378 function calls (1879839 primitive calls) in 1.351 seconds


