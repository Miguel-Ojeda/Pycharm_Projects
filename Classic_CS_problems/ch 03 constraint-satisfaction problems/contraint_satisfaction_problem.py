from typing import TypeVar, Generic, List, Dict, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


# Base class para definir restricciones
class Constraint(Generic[V, D], ABC):
    # iniciamos la restricción dándole las variables q vamos a restringir
    def _init_(self, variables: List[V]) -> None:
        self.variables = variables

    # Las subclases deben definir su propio método (pq es abstracto)
    # devuelve True si las variables cumplen las condiciones impuestas
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

'''
The centerpiece of our constraint-satisfaction framework will be a class called CSP.
CSP is the gathering point for variables, domains, and constraints. In terms of its type
hints, it uses generics to make itself flexible enough to work with any kind of variables
and domain values (V keys and D domain values).

Within CSP, the variables, domains, and constraints collections are of types that you would expect.
* The variables collection is a list of variables,
* domains is a dict mapping variables to lists of possible values (the domains of those variables),
* constraints is a dict that maps each variable to a list of the constraints imposed on it.
'''

# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        # Variables que habrá que restringir
        self.variables: List[V] = variables
        # Diccionario que asocia a cada variable un listado de dominios con varlores posibles
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                # O sea, la variable no tiene definido un dominio de valores.... ufff, malo
                raise LookupError('Cada variable debe tener un dominnio asignado')

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                # O sea, la variable que nos pasan no es conocida por el problema
                raise LookupError('La variable a restringir no está en el CSP')
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment
        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if we're still consistent, we recurse (continue)
            if self.consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
            # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
            return None

