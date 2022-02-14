"""
Instead of each animal class inheriting directly, from Animal, define several new
classes, ZeroLeggedAnimal, TwoLeggedAnimal, and FourLeggedAnimal, all of which inherit from Animal,
and dictate the number of legs on each instance.

Now modify Wolf, Sheep, Snake, and Parrot such that each class inherits from one of these new classes,
rather than directly from Animal.
How does this affect your method definitions?
"""


# Esto es sólo un ejercicio, para practicar, creo más lógico el enfoque que hicimos en 43
class Animal:
    # No usar, es sólo como base!!
    def __init__(self, color, number_of_legs):
        self.number_of_legs = number_of_legs
        self.species = self.__class__.__name__.lower()
        # o sea, saca la especie de la clase derivada que la llama!!!
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class FourLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        # Se llama a Animal dando el color y el número de patas...
        # ya coge animal la especie del nombre clase del objeto
        super().__init__(color, 4)


class TwoLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        super().__init__(color, 2)


class ZeroLeggedAnimal(Animal):
    # No llamar tampoco directamente!!!
    def __init__(self, color):
        super().__init__(color, 0)


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