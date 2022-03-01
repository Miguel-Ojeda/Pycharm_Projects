"""
3 misioneros y 3 caníbales en la orilla izquierda, tienen que pasar a la orilla derecha
utilizando un bote con capacidad máxima para 2 personas, con las típicas restricciones...
https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem
Variations: número de caníbales, misioneros iniciales, capacidad del bote, etc
If the boat holds 2 people:
then 2 couples require 5 trips; 3 couples: 11 trips, with 4 or more couples, the problem has no solution.
If the boat can hold 3 people, then up to 5 couples can cross;
if the boat can hold 4 people, any number of couples can cross.
"""
from __future__ import annotations

from typing import NamedTuple, Optional, List, Any
from generic_search import dfs, bfs, astar, Node, node_to_path, astar
import sys


class MCState:
    def __init__(self, mis_iz: int, can_iz: int, mis_der: int, can_der: int,
                 barco_iz: bool, capacidad_barco: int) -> None:
        self.mis_iz = mis_iz
        self.can_iz = can_iz
        self.mis_der = mis_der
        self.can_der = can_der
        self.barco_iz = barco_iz
        self.capacidad_barco = capacidad_barco

    '''
       Importante: para que todo esto funcione, la búsqueda utiliza pertenencia a conjuntos
       para ello debe implementar un hash basado en el contenido, claro
       y debe implementar una igualdad, basado tb. en contenido...
       Si no la búsqueda no servirá... esto no hacía falta en dataclasses
       No sé porqué este no hace falta para utilizar bds
       Pero si no lo hacemos no sirve dfs'''
    def __hash__(self):
        return hash((self.can_iz, self.mis_iz, self.barco_iz))
        # aunque hay más campos, si estos tres son iguales, suponiendo que
        # no hemos cambiado las condiciones del juego, pues van a ser iguales tb.

    def __eq__(self, other: Any) -> bool:
        return self.__class__ == other.__class__ and hash(self) == hash(other)

    def __str__(self) -> str:
        frase_1 = f'En la orilla izq. hay {self.mis_iz} misioneros y {self.can_iz} caníbales\n'
        frase_2 = f'En la orilla derecha hay {self.mis_der} misioneros y {self.can_der} caníbales\n'
        if self.barco_iz:
            frase_3 = 'El barco está en la izquierda del río'
        else:
            frase_3 = 'El barco está a la derecha del río'
        return frase_1 + frase_2 + frase_3

    def mini_repr(self) -> str:
        frase_1 = f'mis_iz: {self.mis_iz}, can_iz: {self.can_iz} /// '
        frase_2 = f'mis_der: {self.mis_der}, can_der: {self.can_der} /// '
        frase_3 = f'Barco iz -> {self.barco_iz}'
        return frase_1 + frase_2 + frase_3

    def is_valid(self) -> bool:
        if self.can_iz < 0 or self.can_der < 0 or self.mis_iz < 0 or self.mis_der < 0:
            return False
        elif self.can_iz > self.mis_iz > 0:
            return False
        elif self.can_der > self.mis_der > 0:
            return False
        return True

    def goal_test(self) -> bool:
        # Lo habremos conseguido cuando no quede nadie en la orilla izquierda...
        return self.mis_iz == self.can_iz == 0

    def successors(self) -> List[MCState]:
        sucesores: List[MCState] = []
        for canibales in range(self.capacidad_barco + 1):
            for misioneros in range(self.capacidad_barco + 1):
                if 0 < misioneros + canibales <= self.capacidad_barco:
                    if self.barco_iz:
                        mis_iz = self.mis_iz - misioneros
                        can_iz = self.can_iz - canibales
                        mis_der = self.mis_der + misioneros
                        can_der = self.can_der + canibales
                    else:
                        mis_iz = self.mis_iz + misioneros
                        can_iz = self.can_iz + canibales
                        mis_der = self.mis_der - misioneros
                        can_der = self.can_der - canibales

                    nuevo = MCState(mis_iz=mis_iz, can_iz=can_iz, mis_der=mis_der, can_der=can_der,
                                    capacidad_barco=self.capacidad_barco, barco_iz=not self.barco_iz)
                    if nuevo.is_valid():
                        sucesores.append(nuevo)
        return sucesores

    def restante(self) -> float:
        """
        Usaremos esta función de heurística para el algoritmo A* (astar)
        Es más sencillo que con el laberinto, donde teníamos que crear una función para que
        en función del goal, nos devolviera otra función...
        Aquí ya el propio objeto lo sabe, por eso lo definimos dentro del objeto
        """
        return (self.mis_iz + self.can_iz) / self.capacidad_barco


def display_transition(estado_1: MCState, estado_2: MCState) -> None:
    """simplemente imprime una línea mostrando lo que ha pasado, el embarque para pasar
    del estado juego1 al estado juego 2
    Supuestamente deben ser dos estados consecutivos.. y válidos, eso no lo miramos
    suponemos que hemos pasado, embarcando, de un estado a otro... pero no haremos las
    comprobaciones...."""
    if estado_1.barco_iz:
        canibales_embarcados = estado_1.can_iz - estado_2.can_iz
        misioneros_embarcados = estado_1.mis_iz - estado_2.mis_iz
        frase = 'Embarcamos de la orilla izq. a la derecha a '
    else:
        canibales_embarcados = estado_2.can_iz - estado_1.can_iz
        misioneros_embarcados = estado_2.mis_iz - estado_1.mis_iz
        frase = 'Embarcamos de la orilla derecha. a la izq a '

    frase += f'{canibales_embarcados} caníbales y {misioneros_embarcados} misioneros'
    print(frase)


def display_solucion(path: List[MCState]) -> None:
    juego_anterior = path[0]
    print(juego_anterior)
    print(80 * '-')
    for index, juego_actual in enumerate(path[1:]):
        display_transition(juego_anterior, juego_actual)
        print(80*'-')
        print(juego_actual)
        print(80*'-')
        juego_anterior = juego_actual


def display_path_debug(path: List[MCState]) -> None:
    for index, juego in enumerate(path):
        print(index, ': ', end='')
        print(juego.mini_repr())


if __name__ == '__main__':

    juego = MCState(mis_iz=3, can_iz=3, mis_der=0, can_der=0, barco_iz=True, capacidad_barco=2)
    solucion_1: Optional[Node[MCState]] = bfs(juego, MCState.goal_test, MCState.successors)
    if solucion_1 is None:
        print('No tiene solución DFS el problema de misioneros y caníbales')
    else:
        print('Tiene solución DFS el problema de misioneros y caníbales')
        path_1 = node_to_path(solucion_1)
        display_path_debug(path_1)

    solucion_2: Optional[Node[MCState]] = bfs(juego, MCState.goal_test, MCState.successors)
    if solucion_2 is None:
        print('No tiene solución BFS el problema de misioneros y caníbales')
    else:
        print('Tiene solución BFS el problema de misioneros y caníbales')
        path_2 = node_to_path(solucion_2)
        display_path_debug(path_2)

    solucion_3: Optional[Node[MCState]] = astar(juego, MCState.goal_test, MCState.successors, MCState.restante)
    if solucion_3 is None:
        print('No tiene solución A* el problema de misioneros y caníbales')
    else:
        print('Tiene solución A* el problema de misioneros y caníbales')
        path_3 = node_to_path(solucion_3)
        display_path_debug(path_3)

