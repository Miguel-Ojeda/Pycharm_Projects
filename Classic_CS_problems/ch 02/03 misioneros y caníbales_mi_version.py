"""
3 misioneros y 3 caníbales en la orilla izquierda, tienen que pasar a la orilla
derecha utilizando un barco en el que caben 2 personas, con las típicas
restricciones...
(caben 2 personas como mucho en el barco, no puede haber más caníbales que
personas en ninguna orilla...)
"""
# https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem
'''
Variations
An obvious generalization is to vary the number of jealous couples (or missionaries and cannibals),
the capacity of the boat, or both.
If the boat holds 2 people, then 2 couples require 5 trips;
with 4 or more couples, the problem has no solution.[6]
If the boat can hold 3 people, then up to 5 couples can cross;
if the boat can hold 4 people, any number of couples can cross.[4], p. 300.
'''

from typing import NamedTuple, Optional, List
from dataclasses import dataclass
from generic_search import dfs, bfs, astar, Node, node_to_path, astar
import sys


class misioneros_y_canibales(NamedTuple):
    canibales: int
    misioneros: int


@dataclass(frozen=True)
class juego_misioneros_y_canibales:
    izquierda: misioneros_y_canibales
    derecha: misioneros_y_canibales
    barco_iz: bool
    capacidad_barco: int

    def display(self):
        print(f'En la orilla izq. hay {self.izquierda.misioneros} misioneros y {self.izquierda.canibales} caníbales')
        print(f'En la orilla derecha hay {self.derecha.misioneros} misioneros y {self.derecha.canibales} caníbales')
        if self.barco_iz:
            print('El barco está en la izquierda del río')
        else:
            print('El barco está a la derecha del río')

    def display_resumido(self):
        print(f'mis_iz: {self.izquierda.misioneros}, can_iz: {self.izquierda.canibales}, ', end='')
        print(f'barco_iz: {self.barco_iz}, ', end='')
        print(f'mis_der: {self.derecha.misioneros}, can_iz: {self.derecha.canibales}')


def is_valid(*grupos: misioneros_y_canibales) -> bool:
    for grupo in grupos:
        if grupo.canibales < 0 or grupo.misioneros < 0:
            return False
        elif grupo.canibales > grupo.misioneros > 0:
            return False

    return True


def embarcar(juego: juego_misioneros_y_canibales,
             grupo: misioneros_y_canibales) -> Optional[juego_misioneros_y_canibales]:
    """
    Esta función simplemente pasa de un lado a otro, no hace comprobaciones...
    Las comprobaciones sobre la validez las hace is_valid
    """
    if juego.barco_iz:
        can_iz = juego.izquierda.canibales - grupo.canibales
        mis_iz = juego.izquierda.misioneros - grupo.misioneros
        can_der = juego.derecha.canibales + grupo.canibales
        mis_der = juego.derecha.misioneros + grupo.misioneros
    else:
        can_iz = juego.izquierda.canibales + grupo.canibales
        mis_iz = juego.izquierda.misioneros + grupo.misioneros
        can_der = juego.derecha.canibales - grupo.canibales
        mis_der = juego.derecha.misioneros - grupo.misioneros
    izquierda = misioneros_y_canibales(can_iz, mis_iz)
    derecha = misioneros_y_canibales(can_der, mis_der)
    barco_iz = not juego.barco_iz
    if is_valid(izquierda, derecha):
        return juego_misioneros_y_canibales(izquierda=izquierda, derecha=derecha,
                                            barco_iz=barco_iz, capacidad_barco=juego.capacidad_barco)
    return None   # no hace falta realmente poner el return Final

def display_transition(juego1: juego_misioneros_y_canibales, juego2: juego_misioneros_y_canibales) -> None:
    """simplemente imprime una línea mostrando lo que ha pasado, el embarque para pasar
    del estado juego1 al estado juego 2
    Supuestamente deben ser dos estados consecutivos.. y válidos, eso no lo miramos
    suponemos que hemos pasado, embarcando, de un estado a otro... pero no haremos las
    comprobaciones...."""
    if juego1.barco_iz:
        canibales_embarcados = juego1.izquierda.canibales - juego2.izquierda.canibales
        misioneros_embarcados = juego1.izquierda.misioneros - juego2.izquierda.misioneros
        frase = 'Embarcamos de la orilla izq. a la derecha a '
    else:
        canibales_embarcados = juego2.izquierda.canibales - juego1.izquierda.canibales
        misioneros_embarcados = juego2.izquierda.misioneros - juego1.izquierda.misioneros
        frase = 'Embarcamos de la orilla derecha. a la izq a '

    frase += f'{canibales_embarcados} caníbales y {misioneros_embarcados} misioneros'
    print(frase)


def successors(juego: juego_misioneros_y_canibales) -> List[juego_misioneros_y_canibales]:
    sucesores: List[juego_misioneros_y_canibales] = []
    # Como mucho pueden embarcar dos personas!!!
    for canibales, misioneros in ((1, 0), (2, 0), (1, 1), (0, 1), (0, 2)):
        grupo = misioneros_y_canibales(canibales=canibales, misioneros=misioneros)
        resultado = embarcar(juego, grupo)
        if resultado:
            sucesores.append(resultado)
    return sucesores


def successors_general(juego: juego_misioneros_y_canibales) -> List[juego_misioneros_y_canibales]:
    sucesores: List[juego_misioneros_y_canibales] = []
    for canibales in range(juego.capacidad_barco + 1):
        for misioneros in range(juego.capacidad_barco + 1):
            if 0 < misioneros + canibales <= juego.capacidad_barco:
                grupo = misioneros_y_canibales(canibales=canibales, misioneros=misioneros)
                resultado = embarcar(juego, grupo)
                if resultado:
                    sucesores.append(resultado)
    return sucesores


def display_path(path: List[juego_misioneros_y_canibales]) -> None:
    juego_anterior = path[0]
    juego_anterior.display()
    for index, juego_actual in enumerate(path[1:]):
        display_transition(juego_anterior, juego_actual)
        juego_actual.display()
        juego_anterior = juego_actual


def display_path_debug(path: List[juego_misioneros_y_canibales]) -> None:
    for index, juego in enumerate(path):
        print(index, ': ', end='')
        juego.display_resumido()


def exito(juego) -> bool:
    """
    Para que sirva para el número de caníbales y misioneros que quiera...
    la condición para el éxito es que no quede nadie en la orilla izquierda...
    """
    if juego.izquierda.canibales == juego.izquierda.misioneros == 0:
        return True
    else:
        return False


def restante(juego: juego_misioneros_y_canibales) -> float:
    """
    Usaremos esta función de heurística para el algoritmo A* (astar)
    Es más sencillo que con el laberinto, donde teníamos que crear una función para que
    en función del goal, nos devolviera otra función...
    """
    return (juego.izquierda.misioneros + juego.izquierda.canibales) / 2




if __name__ == '__main__':
    '''
    izquierda = misioneros_y_canibales(canibales=1, misioneros=2)
    derecha = misioneros_y_canibales(canibales=2, misioneros=0)
    if is_valid(izquierda, derecha):
        print('válido')
    else:
        print('no válido')
    sys.exit()
    '''
    orilla_izquierda: misioneros_y_canibales = misioneros_y_canibales(canibales=42, misioneros=42)
    orilla_derecha: misioneros_y_canibales = misioneros_y_canibales(canibales=0, misioneros=0)
    juego = juego_misioneros_y_canibales(izquierda=orilla_izquierda, derecha=orilla_derecha,
                                         barco_iz=True, capacidad_barco=4)
    solucion_1: Optional[Node[juego_misioneros_y_canibales]]
    estados_recorridos, solucion_1 = dfs(juego, exito, successors_general)
    if solucion_1 is None:
        print('No tiene solución DFS el problema de misioneros y caníbales')
    else:
        print('\nTiene solución DFS el problema de misioneros y caníbales; estados_recorridos', estados_recorridos)
        path_1 = node_to_path(solucion_1)
        print('Los pasos de la solución son:', len(path_1))
        display_path_debug(path_1)

    solucion_2: Optional[Node[juego_misioneros_y_canibales]]
    estados_recorridos, solucion_2 = bfs(juego, exito, successors_general)
    if solucion_2 is None:
        print('No tiene solución BFS el problema de misioneros y caníbales')
    else:
        print('\nTiene solución BFS el problema de misioneros y caníbales; estados_recorridos:', estados_recorridos)
        path_2 = node_to_path(solucion_2)
        print('Los pasos de la solución son:', len(path_2))
        display_path_debug(path_2)

    solucion_3: Optional[Node[juego_misioneros_y_canibales]]
    estados_recorridos, solucion_3 = astar(juego, exito, successors_general, restante)
    if solucion_3 is None:
        print('No tiene solución A* el problema de misioneros y caníbales')
    else:
        print('\nTiene solución A* el problema de misioneros y caníbales; estados_recorridos:', estados_recorridos)
        path_3 = node_to_path(solucion_3)
        print('Los pasos de la solución son:', len(path_3))
        display_path_debug(path_3)
