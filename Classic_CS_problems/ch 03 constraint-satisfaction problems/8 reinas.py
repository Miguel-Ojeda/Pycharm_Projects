from csp_repetido import CSP, Constraint
from typing import Dict, List, Optional
import pprint


# Tenemos que extender la base clase para añadir las peculiaridades
# y también definir el método para comprobar si se cumplen las restricciones...
class OchoReinas(Constraint[int, int]):
    def __init__(self, columnas: List[int]) -> None:
        super().__init__(columnas)
        # self.columns = columnas NO HACE FALTA, lo tenía el libro!!!

    def satisfied(self, assignment: dict[int, int]) -> bool:
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.variables) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]  # q2r = queen 2 row
                    if q1r == q2r:  # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):  # same diagonal?
                        return False
        return True  # no conflict



if __name__ == '__main__':
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)

    csp.add_constraint(OchoReinas(columns))
    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)

# SOLUCIÓN: {1: 1, 2: 5, 3: 8, 4: 6, 5: 3, 6: 7, 7: 2, 8: 4}