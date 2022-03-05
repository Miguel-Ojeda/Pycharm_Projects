'''
 SEND
+MORE
______
MONEY
'''
from typing import List, Dict
from  csp_repetido import CSP, Constraint, Assignment, Optional
import cProfile

class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Assignment) -> bool:
        # if there are duplicate values, then it's not a solution
        if len(set(assignment.values())) < len(assignment):
            return False
        '''
        variables_asignadas = assignment.keys()
        if 'D' in variables_asignadas and 'E' in variables_asignadas and 'Y' in variables_asignadas:
            if (assignment['D'] + assignment['E']) % 10 != assignment['Y']:
                return False
        '''
        # if all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            s: int = assignment['S']
            e: int = assignment['E']
            n: int = assignment["N"]
            d: int = assignment["D"]
            m: int = assignment["M"]
            o: int = assignment["O"]
            r: int = assignment["R"]
            y: int = assignment["Y"]

            send = 1000 * s + 100 * e + 10 * n + d
            more = 1000 * m + 100 * o + 10 * r + e
            money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
            return money == send + more
        else:
            return True


if __name__ == "__main__":
    letters: List[str] = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits["M"] = [1] # so we don't get answers starting with a 0
    csp: CSP[str, int] = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)

# {'S': 2, 'E': 8, 'N': 1, 'D': 7, 'M': 0, 'O': 3, 'R': 6, 'Y': 5}

    cProfile.run('csp.backtracking_search()')

