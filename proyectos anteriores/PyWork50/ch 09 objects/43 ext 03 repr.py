"""
Let’s say that each class’s __repr__ method should print the animal’s sound,
as well as the standard string we implemented previously. In other words,
str(sheep) would be Baa—white sheep, 4 legs.
How would you use inheritance to maximize code reuse?
"""

# Esta es mi versión, ver luego la de Reuven que es mucho mejor!!
# La de Reuven está en ex_43_ext_03_repr_Reuven

class Animal:
    # No usar, es sólo como base!!
    def __init__(self, color):
        self.species = self.__class__.__name__.lower()
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class Sheep(Animal):
    number_of_legs = 4

    def __repr__(self):
        return f'"Beeee" --> {super().__repr__()}'

class Wolf(Animal):
    number_of_legs = 4

    def __repr__(self):
        return f'"Auuuuu" --> {super().__repr__()}'

class Snake(Animal):
    number_of_legs = 0

    def __repr__(self):
        return f'"Sisssss" --> {super().__repr__()}'


class Parrot(Animal):
    number_of_legs = 2

    def __repr__(self):
        return f'"Cuaaaa" --> {super().__repr__()}'


if __name__ == '__main__':
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