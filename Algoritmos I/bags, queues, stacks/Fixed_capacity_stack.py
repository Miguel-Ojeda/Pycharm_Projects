from typing import TypeVar, Generic, Optional, List

# Esto es cutre, pero implementaré stack con una lista accediendo por índices...
# como si fuera un array (no me sirvió lo de numpy

V = TypeVar('V')


class FixedCapacityStack(Generic[V]):
    def __init__(self, capacity: int):
        self._data: List[V] = [None for _ in range(capacity)]
        self._capacity: int = capacity
        self._ocupados:int = 0
        # Nos lleva el número de ocupados
        # Este índice nos indica donde deberemos añadir los nuevos...
        # Y el índice anterior nos indica el último elemento


    @property
    def empty(self):
        return self._ocupados == 0

    @property
    def full(self):
        return self._ocupados == self._capacity

    def push(self, item: V) -> None:
        if self.full:
            print('Stack está lleno, lo siento')
            return
        self._data[self._ocupados] = item
        self._ocupados += 1

    def pop(self) -> Optional[V]:
        if self.empty:
            return
        self._ocupados -= 1
        return self._data[self._ocupados]

    def __repr__(self):
        cadena = f'La pila tiene ocupados {self._ocupados} de {self._capacity} elementos\n'
        cadena += '\n'.join(self._data[i] for i in reversed(range(self._ocupados)))
        return cadena

if __name__ == '__main__':
    cadenas: FixedCapacityStack[str] = FixedCapacityStack(5)
    cadenas.push('uno')
    cadenas.push('dos')
    print(cadenas)
    cadenas.push('tres')
    cadenas.push('cuatro')
    print(cadenas)

    cadenas.push('cinco')
    print(cadenas)

    cadenas.push('seis')
    print(cadenas)

    cadenas.push('siete')
    cadenas.push('ocho')
    cadenas.push('nueve')
    cadenas.push('diez')
    print(cadenas)
    cadenas.pop()
    print(cadenas)





