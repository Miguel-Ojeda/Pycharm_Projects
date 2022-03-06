from typing import List, Dict, Generic, TypeVar, Optional, Callable
from abc import ABC, abstractmethod

V = TypeVar('V')  # tipo variable
D = TypeVar('D')   # tipo valores del dominio

Domain = List[D]
Domains = Dict[V, Domain]
Assignment = Dict[V, D]


class Constraint(ABC, Generic[V, D]):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Assignment) -> bool:
        ...

Constraints: Dict[V, List[Constraint]]



class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Domains) -> None:
        self.variables: List[V] = variables
        self.domains: Domains = domains
        self.constraints: Constraints = {}
        for variable in variables:
            if variable not in domains:
                raise LookupError('Cada variable debe tener definido su dominio!!!')
            self.constraints[variable] = []

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        # Añade una restricción aplicable a una lista de variables...
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError('Está restringiendo variables desconocidas')
            else:
                self.constraints[var].append(constraint)

    def consistent(self, variable: V, assignment: Assignment) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Assignment = {}) -> Optional[Assignment]:
        # algoritmo recursivo...
        if len(assignment) == len(self.variables):
            return assignment
        # Si llegamos hasta aquí, es que queda alguna por asignar...
        unassigned: List[V] = [var for var in self.variables if var not in assignment]
        '''
        if unassigned == []:
            print('asignadas y totales', len(assignment), len(self.variables))
            print('variables en self.var')
            for index, var in enumerate(self.variables, 1):
                print(var)
            print('variables asignadas')
            for index, var in enumerate(assignment, 1):
                print(var)
            print('Uffff')
        '''
        first_un: V = unassigned[0]
        # Ahora a ver que valor asignamos de su dominio..
        for value in self.domains[first_un]:
            local_assignment = assignment.copy()
            local_assignment[first_un] = value
            if self.consistent(first_un, local_assignment):
                resultado = self.backtracking_search(local_assignment)
                if resultado is not None:
                    return resultado
        return None  # no haría falta, se sobreentiende... pero por claridad...


    def backtracking_search_heuristic(self, heuristic: Callable[[V, Assignment], float],
                                      assignment: Assignment = {}) -> Optional[Assignment]:
        '''
        Modificamos el algoritmo anterior para utilizar una función de heurística...
        La función heurística nos ayuda a decidir a qué variable vamos a asignar valor
        En el modo normal, se asigna a la primera variable
        Aquí utilizaremos la función de heurística asignará a cada una de las variables no asignadas
        un peso... la que tenga mayor peso, será la que cojamos...
        '''
        # algoritmo recursivo...
        if len(assignment) == len(self.variables):
            return assignment
        # Si llegamos hasta aquí, es que queda alguna por asignar...
        unassigned_vars: List[V] = [var for var in self.variables if var not in assignment]
        unassigned_pesos: List[float] = [heuristic(var, assignment) for var in unassigned_vars]
        peso_maximo = max(unassigned_pesos)
        indice = unassigned_pesos.index(peso_maximo)
        first_un: V = unassigned_vars[indice]

        # Ahora a ver que valor asignamos de su dominio..
        for value in self.domains[first_un]:
            local_assignment = assignment.copy()
            local_assignment[first_un] = value
            if self.consistent(first_un, local_assignment):
                resultado = self.backtracking_search_heuristic(heuristic, local_assignment)
                if resultado is not None:
                    return resultado
        return None  # no haría falta, se sobreentiende... pero por claridad...


    def bts_heuristic_con_restriccion(self, heuristic_restrict: Callable[[V, Assignment], tuple[float, Domain]],
                                      assignment: Assignment = {}) -> Optional[Assignment]:
        '''
        Esta heurística es más potente, además de asignar un peso a la variable
        devuelve el dominio de valores actualizados que debería tener...
        Con lo que cada vez más se va restringiendo todo mucho más rápido
        '''
        # algoritmo recursivo...
        if len(assignment) == len(self.variables):
            return assignment
        # Si llegamos hasta aquí, es que queda alguna por asignar...
        unassigned_vars: List[V] = [var for var in self.variables if var not in assignment]
        unassigned_pesos: List[float] = []
        for var in unassigned_vars:
            peso, dominio = heuristic_restrict(var, assignment)
            unassigned_pesos.append(peso)
            # Actualizamos el dominio!!!!
            self.domains[var] = dominio

        peso_maximo = max(unassigned_pesos)
        indice = unassigned_pesos.index(peso_maximo)
        first_un: V = unassigned_vars[indice]

        # Ahora a ver que valor asignamos de su dominio..
        for value in self.domains[first_un]:
            local_assignment = assignment.copy()
            local_assignment[first_un] = value
            if self.consistent(first_un, local_assignment):
                resultado = self.bts_heuristic_con_restriccion(heuristic_restrict, local_assignment)
                if resultado is not None:
                    return resultado
        return None  # no haría falta, se sobreentiende... pero por claridad...