from __future__ import annotations

import sys
from typing import List, Optional, Any
from generic_search import bfs, Node, node_to_path, dfs

MAX_NUM: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries  # west bank missionaries
        self.wc: int = cannibals  # west bank cannibals
        self.em: int = MAX_NUM - self.wm  # east bank missionaries
        self.ec: int = MAX_NUM - self.wc  # east bank cannibals
        self.boat: bool = boat
    '''
    Importante: para que todo esto funcione, la búsqueda utiliza pertenencia a conjuntos
    para ello debe implementar un hash basado en el contenido, claro
    y debe implementar una igualdad, basado tb. en contenido...
    Si no la búsqueda no servirá... esto no hacía falta en dataclasses
    No sé porqué este no hace falta para utilizar bds
    Pero si no lo hacemos no sirve dfs'''
    def __hash__(self):
        return hash((self.wm, self.wc, self.boat))

    def __eq__(self, other: Any) -> bool:
        return self.__class__ == other.__class__ and hash(self) == hash(other)


    def __str__(self) -> str:
        frase_1 = f'On the west bank there are {self.wm} missionaries and {self.wc} cannibals.\n'
        frase_2 = f'On the east bank there are {self.em} missionaries and {self.ec} cannibals.\n'
        if self.boat:
            frase_3 = f'The boat is on the west bank.\n'
        else:
            frase_3 = f'The boat is on the east bank.\n'
        return frase_1 + frase_2 + frase_3

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self) -> bool:
        # if self.wm < self.wc and self.wm > 0:
        if self.wc > self.wm > 0:
            return False
        # if self.em < self.ec and self.em > 0:
        if self.ec > self.em > 0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:  # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
        if self.wm > 0:
            sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
        if self.wc > 1:
            sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
        if self.wc > 0:
            sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
        if (self.wc > 0) and (self.wm > 0):
            sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:  # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
        if self.em > 0:
            sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
        if self.ec > 1:
            sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
        if self.ec > 0:
            sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
        if (self.ec > 0) and (self.em > 0):
            sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]


def display_solution(path: List[MCState]):
    if len(path) == 0:  # sanity check
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            misioneros = old_state.em - current_state.em
            canibales = old_state.ec - current_state.ec
            print(f'{misioneros} missionaries and {canibales} cannibals moved from the east bank to the west bank.')
        else:
            misioneros = old_state.wm - current_state.wm
            canibales = old_state.wc - current_state.wc
            print(f'{misioneros} missionaries and {canibales} cannibals moved from the west bank to the east bank.')
        print(current_state)
        old_state = current_state


if __name__ == "__main__":

    start: MCState = MCState(MAX_NUM, MAX_NUM, True)

    solution: Optional[Node[MCState]]
    pasos, solution = dfs(start, MCState.goal_test, MCState.successors)
    if solution is None:
        print("No solution found!")
    else:
        path: List[MCState] = node_to_path(solution)
        print('La solución encontrada tiene pasos:', pasos, '\n')
        display_solution(path)
