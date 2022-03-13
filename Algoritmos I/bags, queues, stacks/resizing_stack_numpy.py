"""
Lo mismo, pero se utiliza el redimensionamiento para optimizar, ya que,
a veces no sabemos realmente el tamaño que nos hace falta, y tampoco es óptimo
reservar un tamaño grandísimo si no se va a utilizar...
"""
import numpy as np
from typing import Optional

class ResizingStack:
    def __init__(self):
        # Inicialmente creamos un array sólo con capacidad para un ítem
        # Aunque podríamos empezar con tamaño 5 quizás mejor, por ejemplo...
        self._data = np.zeros(1, dtype=object)
        self._ocupados: int = 0
        # Nos lleva el número de ocupados
        # Este índice nos indica donde deberemos añadir los nuevos...
        # Y el índice anterior nos indica el último elemento

    @property
    def empty(self):
        return self._ocupados == 0

    @property
    def capacity(self):
        return self._data.size

    @property
    def full(self):
        return self._ocupados == self.capacity

    @property
    def size(self):
        return self._ocupados

    def push(self, item: object) -> None:
        if self.full:
            self.resize(2 * self.capacity)
        self._data[self._ocupados] = item
        self._ocupados += 1

    def pop(self) -> Optional[object]:
        if self.empty:
            return
        self._ocupados -= 1
        item = self._data[self._ocupados]
        if self._ocupados > 0 and self._ocupados == self.capacity // 4:
            self.resize(self.capacity // 2)
        return item

    def resize(self, nueva_capacidad: int) -> None:
        temporal = np.empty(shape=nueva_capacidad, dtype=object)
        for i in range(self._ocupados):
            temporal[i] = self._data[i]
        self._data = temporal

    def __repr__(self):
        cadena = f'La pila tiene ocupados {self.size} de {self.capacity} elementos\n'
        cadena += '\n'.join(self._data[i] for i in reversed(range(self._ocupados)))
        return cadena

if __name__ == '__main__':
    # PRUEBA 1
    '''
    cadenas: FixedCapacityStack = FixedCapacityStack(5)
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
    '''
    # PRUEBA 2
    stack: ResizingStack = ResizingStack()
    cadena = 'to be or not to - be - - that - - - is'
    cadena = cadena.split()
    print(cadena)
    for item in cadena:
        if item != '-':
            print(f'Metiendo -> {item}')
            stack.push(item)
        else:
            print(f'Sacando -> {stack.pop()}')
    print(stack)
