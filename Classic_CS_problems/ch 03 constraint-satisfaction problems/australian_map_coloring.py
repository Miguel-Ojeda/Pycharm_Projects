import pprint

from csp_repetido import Constraint, CSP
from typing import Dict, List, Optional

# Tenemos que extender la base clase para añadir las peculiaridades
# y también definir el método para comprobar si se cumplen las restricciones...
class MapColoringConstraint(Constraint[str, str]):

    def __init__(self, place1: str, place2: str) -> None:
        self.place_1 = place1
        self.place_2 = place2
        super().__init__([place1, place2])

    def satisfied(self, assignment: dict[str, str]) -> bool:
        # Tenemos una restricción sobre dos places...
        # supuestamente pq son vecinos claro!!! si no no tiene sentido la restricción!!!
        # Si alguno de los dos lugares no está en la asignación, pues lógicamente
        # no incumplimos la restricción...
        if self.place_1 not in assignment or self.place_2 not in assignment:
            return True
        # Tenemos dos sitios vecinos... la restricción se satisfará si ambos son de distinto valor
        return assignment[self.place_1] != assignment[self.place_2]



if __name__ == '__main__':
    zone_1 = 'Western Australia'
    zone_2 = 'Northern Territory'
    zone_3 = 'South Australia'
    zone_4 = 'Queensland'
    zone_5 = 'New South Wales'
    zone_6 = 'Victoria'
    zone_7 = 'Tasmania'
    variables = [zone_1, zone_2, zone_3, zone_4, zone_5, zone_6, zone_7]
    dominios = {var: ["red", "green", "blue"] for var in variables}
    csp: CSP[str, str] = CSP(variables, dominios)
    csp.add_constraint(MapColoringConstraint(zone_1, zone_2))
    csp.add_constraint(MapColoringConstraint(zone_1, zone_3))
    csp.add_constraint(MapColoringConstraint(zone_3, zone_2))
    csp.add_constraint(MapColoringConstraint(zone_4, zone_2))
    csp.add_constraint(MapColoringConstraint(zone_4, zone_3))
    csp.add_constraint(MapColoringConstraint(zone_4, zone_5))
    csp.add_constraint(MapColoringConstraint(zone_5, zone_3))
    csp.add_constraint(MapColoringConstraint(zone_6, zone_3))
    csp.add_constraint(MapColoringConstraint(zone_6, zone_5))
    csp.add_constraint(MapColoringConstraint(zone_6, zone_7))


    resultado = csp.backtracking_search()
    pprint.pprint(resultado)
