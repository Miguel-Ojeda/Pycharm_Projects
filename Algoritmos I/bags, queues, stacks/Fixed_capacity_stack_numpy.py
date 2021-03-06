"""
No me sirvió con generics... pq por ejemplo, si creo un array de str, sólo tienen un carácter
por eso pasé de generics y utilizo simplemente arrays de dtype= object
No sirve nada de esto!!
"""
import numpy as np


class FixedCapacityStack:
    def __init__(self, capacity: int):
        self._data = np.zeros(shape=capacity, dtype=object)
        self._capacity: int = capacity
        self._ocupados: int = 0
        # Nos lleva el número de ocupados
        # Este índice nos indica donde deberemos añadir los nuevos...
        # Y el índice anterior nos indica el último elemento

    @property
    def empty(self):
        return self._ocupados == 0

    @property
    def size(self):
        return self._ocupados

    @property
    def full(self):
        return self._ocupados == self._capacity

    def push(self, item: object) -> None:
        if self.full:
            print('Stack está lleno, lo siento')
            return
        self._data[self._ocupados] = item
        self._ocupados += 1

    def pop(self) -> object:
        if self.empty:
            return
        self._ocupados -= 1
        return self._data[self._ocupados]

    def __repr__(self):
        cadena = f'La pila tiene ocupados {self.size} de {self._capacity} elementos\n'
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
    stack: FixedCapacityStack = FixedCapacityStack(10)
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
