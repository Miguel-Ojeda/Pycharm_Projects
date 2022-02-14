# La versión de Reuven es mejor, pq asigna directamente las patas en las clases TwoLegged, etc
class Animal:
    # No usar, es sólo como base!!
    def __init__(self, color):
        self.species = self.__class__.__name__.lower()
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class FourLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        # Se llama a Animal dando el color y el número de patas...
        # ya coge animal la especie del nombre clase del objeto
        super().__init__(color)
        # Reuven el cambio que hace es asignar ya aquí el número de patas
        # es lo lógico ya que es justo la razón de ser de estas clases!!!
        self.number_of_legs = 4


class TwoLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2


class ZeroLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0


class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)
        # Aquí invocamos el init de fourlegged dando, simplemente, el color


class Wolf(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Snake(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Parrot(TwoLeggedAnimal):

    def __init__(self, color):
        super().__init__(color)


parrot = Parrot('blue')
lobo = Wolf('gray')
serpiente = Snake('green')
oveja = Sheep('white')

print(parrot)
print(lobo)
print(serpiente)
print(oveja)
'''Resultado --->
Blue parrot, 2 legs
Gray wolf, 4 legs
Green snake, 0 legs
White sheep, 4 legs
'''